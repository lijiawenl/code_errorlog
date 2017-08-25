# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:11:53 2017

@author: lijiawen
This function is used to create the difference log between the two log files 

Args:
    data_dir: the root of target file,see gen_diff.py
    usage:python create.py -d good -t sameword.txt ;choose to deal with sameword file
    
Return:
    save the filter result directly to the original file directory
"""

import lenth_sameword
import sys
import getopt
import os
import re

cur_dir = '/home/jiawen/lkp-ml/data/'
def word_length_all(data_dir,difftype):
    for file in os.listdir(cur_dir+data_dir):
        for logfile in os.listdir(cur_dir + data_dir+file):
            if re.search(difftype,logfile):
                file_dir = cur_dir + data_dir+file+'/'+logfile
                lenth_sameword.lenSameWithout(file_dir)
                print('word count' + file + '/'+ logfile +'is done')
		
		

	
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
        word_length_all(data_dir,difftype)
