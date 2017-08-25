# -*- coding: utf-8 -*-
"""
Created on Wed Oc 7 13:10:22 2017

author: lijiawen
This function is used to create the similarity  between the patch and the log files 

Args:
    data_dir: the root of target file,see gen_diff.py
    usage:python feature.py -d good ;
    
Return:
    save the cal result directly to the original file directory
"""
import sys
import getopt
import os
import re
import json

cur_dir = '/home/jiawen/lkp-ml/data/'
#cur_dir = 'C:\\Users\\lijiawen\\Desktop\\lkp\\code\\Ne'
def saveSameWord(data_dir):
    for file in os.listdir(cur_dir+data_dir):
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
                patchsame,testsame = sameWord(patchjson,testjson)
                same_dir = re.sub('_diff.json','_sameword.txt',logfile)
                sameword_dir = cur_dir + data_dir+file + '/' +same_dir
                saveTxt(sameword_dir,patchsame,testsame)
            else:
                pass
                

def sameWord(patch,diff):
    patchsame = {}
    testsame = {}
    for key in patch.keys():
        if key in diff:
            patchsame[key] = patch[key]
            testsame[key] = diff[key]
    #patchsame = sorted(patchsame.items(), key=lambda patchsame: patchsame[1],reverse = True)
    #testsame = sorted(testsame.items(), key=lambda testsame: testsame[1],reverse = True) 
    return patchsame,testsame

def saveTxt(sim_dir,patchsame,testsame):
    with open(sim_dir,'w') as resu:
        for key in patchsame.keys():
            resu.write(key + ':'+ str(patchsame[key]) + ' '+ key + ':'+ str(testsame[key]) + '\n')#save the result

if __name__ =="__main__":

        if  len(sys.argv)<3:
            print("[usage]:diff_create -d <data_dir>")
            sys.exit(0)

        opts, args = getopt.getopt(sys.argv[1:],"d:s:")
        for op, value in opts:
            if op == '-d':
                data_dir = value
	
        data_dir=data_dir+'/'
        saveSameWord(data_dir)


