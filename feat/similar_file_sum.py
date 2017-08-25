# -*- coding: utf-8 -*-
"""
Created on Wed Oc 2 13:10:22 2017

author: lijiawen
This function is used to create the similarity  between the patch and the log files 

Args:
    data_dir: the root of target file,see gen_diff.py
    usage:python similar.py -d good ;
    
Return:
    save the cal result directly to the original file directory
"""

import math
import sys
import getopt
import os
import re


cur_dir = '/home/jiawen/lkp-ml/data/'
#cur_dir = 'C:\\Users\\lijiawen\\Desktop\\lkp\\code\\'
def processSimilarAll(data_dir):
    cosresultlist = []
    for file in os.listdir(cur_dir+data_dir):
        print(file)
        for logfile in os.listdir(cur_dir + data_dir+file):
            #print(logfile)
            if re.search('.*without.txt',logfile):
                file_dir = cur_dir + data_dir+file+'/'+logfile#get the patch json
                print(file_dir)
                cosresult = calaverage(file_dir)
                print(cosresult)
                cosresultlist.append(cosresult)
            else:
                pass
        sim_dir = cur_dir  + data_dir + 'resultwithout.txt'#can fix according to the feature
    with open(sim_dir,'w') as resu:
        for i in range(len(cosresultlist)):
            resu.write(str(cosresultlist[i]) + '\n')#save the result

        
		
def calaverage(result_dir):
    sumresult = 0.0
    indev = 0
    with open(result_dir) as resu:
        try :
            result = resu.readlines()
        except :
            print('result error')
    for line in result:
        if float(line) > 0:
            sumresult = sumresult + float(line)
            indev = indev + 1
        else:
            pass
    if indev == 0:
        return -1
    else :
        return sumresult/indev
            
        

                
            
    
    
    		
	
if __name__ =="__main__":

        if  len(sys.argv)<3:
            print("[usage]:diff_create -d <data_dir>")
            sys.exit(0)

        opts, args = getopt.getopt(sys.argv[1:],"d:")
        for op, value in opts:
            if op == '-d':
                data_dir = value
	
        data_dir=data_dir + '/'
        processSimilarAll(data_dir)
	
