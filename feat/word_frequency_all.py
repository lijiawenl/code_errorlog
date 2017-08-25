# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:10:22 2017

author: lijiawen
This function is used to create the difference log between the two log files 

Args:
    data_dir: the root of target file,see gen_diff.py
    usage:python create.py -d good -t .log ;choose to deal with the log file or patch file 
    
Return:
    save the filter result directly to the original file directory
"""

import count_words
import sys
import getopt
import os
import re

cur_dir = '/home/jiawen/lkp-ml/data/'
def process_filter_all(data_dir,difftype):
    for file in os.listdir(cur_dir+data_dir):
        for logfile in os.listdir(cur_dir + data_dir+file):
            if re.search(difftype,logfile):
                file_dir = cur_dir + data_dir+file+'/'+logfile
                count_words.countWords(file_dir)
                print('word count' + file + '/'+ logfile +'is done')
        print('word count' + cur_dir+data_dir +'is done')
		
		
	
if __name__ =="__main__":

        if  len(sys.argv)<3:
            print("[usage]:diff_create -d <data_dir>")
            sys.exit(0)

        opts, args = getopt.getopt(sys.argv[1:],"d:t:")
        for op, value in opts:
            if op == '-d':
                data_dir = value
            if op == '-t':
                difftype = value
	
        data_dir=data_dir+'/'
        process_filter_all(data_dir,difftype)
	
