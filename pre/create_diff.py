# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:10:22 2017

author: lijiawen
This function is used to create the difference log between the two log files 

Args:
    data_dir: the root of target file,see gen_diff.py
    usage:python create.py -d good ;
    
Return:
    save the filter result directly to the original file directory
"""
import gen_diff
import sys
import getopt
import os

cur_dir = '/home/jiawen/lkp-ml/data/'
def diffCreate(data_dir):
	for file in os.listdir(cur_dir+data_dir):
		gen_diff.generate_diff(cur_dir + data_dir+file)
		
		
	
if __name__ =="__main__":

        if  len(sys.argv)<3:
            print("[usage]:diff_create -d <data_dir>")
            sys.exit(0)

        opts, args = getopt.getopt(sys.argv[1:],"d:")
        for op, value in opts:
            if op == '-d':
                data_dir = value
	
        data_dir=data_dir+'/'
        diffCreate(data_dir)
	
