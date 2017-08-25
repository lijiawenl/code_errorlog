# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 13:10:22 2017

author: lijiawen
This function should be used in the last step when filtering the file

Args:
    file_dir: the root of target file needed to count.
    
    
Return:
    serialize the count result in json format and saved as ***.json
"""
import re
import json


def countWords(file_dir): 
    with open(file_dir) as diff:
        diff_log = diff.readlines()
    result = {}
    for i in range(len(diff_log)):
        diff_log_split = re.split(' ',diff_log[i].strip(' '))
        for j in range(len(diff_log_split)):
            if diff_log_split[j] == '' or diff_log_split[j] == '\n':
                pass
            else:
                addWord(result,diff_log_split[j]) 
            if re.search('_',diff_log_split[j]) != None:
                diff_log_split_s = re.split('_',diff_log_split[j].strip())
                for k in range(len(diff_log_split_s)):
                    if diff_log_split_s[k] == '' or diff_log_split_s[k] == '\n':
                        pass
                    else:
                        addWord(result,diff_log_split_s[k])      
    countSave = re.sub(r'.patch','.json',file_dir)
    with open(countSave,'w') as cp:
        json.dump(result,cp) # save the dict to the local


def addWord(result,diff_log_split):
    if diff_log_split in result:
        result[diff_log_split] += 1
    else:
        result[diff_log_split] = 1

    
