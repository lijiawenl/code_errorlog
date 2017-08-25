# -*- coding: utf-8 -*-
"""
Created on Wed Oc 1 13:10:22 2017

author: lijiawen
This function is used to create the similarity  between the patch and the log files 

Args:
    data_dir: the root of target file,see gen_diff.py
    usage:python similar.py -d good ;
    calCos:line 60. selcet the correct cosfunction
    
Return:
    save the cal result directly to the original file directory
"""

import math
import sys
import getopt
import os
import re
import json


cur_dir = '/home/jiawen/lkp-ml/data/'
#cur_dir = 'C:\\Users\\lijiawen\\Desktop\\lkp\\code\\'
def processSimilar(data_dir):
    for file in os.listdir(cur_dir+data_dir):
        cosresultlist = []
        print(file)
        for logfile in os.listdir(cur_dir + data_dir+file):
            #print(logfile)
            if re.search('.*.json',logfile):
                if re.search('.*matrix.json',logfile):
                    pass
                elif re.search('_diff.json',logfile):
                    pass
                elif re.search('.*martix',logfile):
                    pass
                elif re.search('.*logic.json',logfile):
                    pass
                else:
                    file_dir = cur_dir + data_dir+file+'/'+logfile#get the patch json
                    print(file_dir)
                    with open(file_dir) as pj:
                        try :
                            patchjson = json.load(pj)
                        except  :
                            print("json error")
            else:
                pass
        for logfile in os.listdir(cur_dir + data_dir+file):
            if re.search('_diff.json',logfile):
                file_dir = cur_dir + data_dir+file+'/'+logfile#get the test json
                with open(file_dir) as tj:
                    try:
                        testjson = json.load(tj)
                    except :
                        print('json error')
                result = calCos1(patchjson,testjson)#cal the simi when using the feature 
                print(result)
                cosresultlist.append(result)
            else:
                pass
        sim_dir = cur_dir + data_dir+file + '/' + 'resultwithout.txt'
        with open(sim_dir,'w') as resu:
            for i in range(len(cosresultlist)):
                resu.write(str(cosresultlist[i])+'\n')#save the result
        


        
#cal the cos similar without some words
def calCos1(patchjson,testjson):
    testlist,patchlist = calmatrix(patchjson,testjson)
    return dotcal(testlist,patchlist)


def calmatrix(patchjson,testjson):
    mergejson = patchjson.copy()
    mergejson.update(testjson)
    filterlist = ['ADDRff80','NUM55aa','TS123','to','in','the','for','by','of',\
                  'at','on','with','about','as']
    for i in filterlist:
        try :
            mergejson.pop(i)
        except :
            print('no'+ i)
    testlist = []
    patchlist = []
    for key in mergejson.keys():
        if key in patchjson:
            patchlist.append(patchjson[key])
        else:
            patchlist.append(0)
        if key in testjson:
            testlist.append(testjson[key])
        else:
            testlist.append(0)
    return testlist,patchlist


def dotcal(testlist,patchlist):
    #cal the dot multiply
    dot = 0; testmatrix = 0; patchmatrix = 0
    for i in range(len(testlist)):
        dot = dot + int(int(testlist[i])*int(patchlist[i]))
        testmatrix = testmatrix + int(testlist[i])**2
        patchmatrix = patchmatrix + int(patchlist[i])**2
    if testmatrix == 0 or patchmatrix == 0:
        return -1
    else:
        result = dot/(math.sqrt(testmatrix)*math.sqrt(patchmatrix))
        return result                
            
    
    
    		
	
if __name__ =="__main__":

        if  len(sys.argv)<3:
            print("[usage]:diff_create -d <data_dir>")
            sys.exit(0)

        opts, args = getopt.getopt(sys.argv[1:],"d:")
        for op, value in opts:
            if op == '-d':
                data_dir = value
	
        data_dir=data_dir+'/'
        processSimilar(data_dir)
	
