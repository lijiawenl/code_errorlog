# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 13:10:22 2017

author: lijiawen
This function is used to filter the num and 
should be used in the last step when filtering the file.

Args:
    file_dir: the root of target file needed to filter
    ex:file_dir = 'C:\\Users\\lijiawen\\Desktop\\lkp\\code\\test\\dmesg_0_diff.log'
    
Return:
    save the filter result directly to the original file
"""
import re

def numToNUM55aa(file_dir):	
	with open(file_dir,'r+') as diff:
		diff_log = diff.readlines()
		for i in range(len(diff_log)):
			new = ''
			diff_log_split = re.split('\\\|\t|\||@|\"|\\|<|>|!|{|}|\&|\~|\;|\#|\'|\>|\-|\=|\)|\(|:|\?|\*|/|\,|\$|\+|\.| |',diff_log[i].strip( ))
			for j in range(len(diff_log_split)):
				if diff_log_split[j].isdigit():
					new = new +' ' +'NUM55aa'+ ' '
				else :
					new = new + '' + diff_log_split[j] + ' '
			diff_log[i] = new + '\n'
	with open(file_dir,'w+') as diff_filter:
		diff_filter.writelines(diff_log)
        

				
			
		
	
			
			
	
