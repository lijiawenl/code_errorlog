# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 13:10:22 2017

author: lijiawen
This function is used to filter the timeStamp and 
should be used in the first step when filtering the file.

Args:
    file_dir: the root of target file needed to filter
    ex:file_dir = 'C:\\Users\\lijiawen\\Desktop\\lkp\\code\\test\\dmesg_0_diff.log'
    
Return:
    save the filter result directly to the original file
"""
import re

def timeStampToTS123(file_dir):	
	with open(file_dir,'r+') as diff:
		diff_log = diff.readlines()
		i = -1
		for line in diff_log:
			i += 1
			diff_log[i] =  re.sub(r'\[(.*?)\]','-TS123-',line)
	with open(file_dir,'w+') as diff_filter:
		diff_filter.writelines(diff_log)
				
			
		

			
			
	
