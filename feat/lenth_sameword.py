# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 15:46:37 2017

@author: lijiawen
"""
#file_dir = 'C:\\Users\\lijiawen\\Desktop\\lkp\\code\\test\\dmesg_0_sameword.txt'

import re

def lenSameWord(file_dir):
    lenth = 0
    with open(file_dir) as f:
        sameword = f.readlines()
    for line in sameword:
        lenth = lenth +1
    print(lenth)
    return lenth

def lenSameWithout(file_dir):
    wordlist = ['TS123','NUM55aa','ADDRf80','and','for','the','to','in','by'\
                ,'of','at','on','with','about','as','1','2','this']
    lenth = 0
    lenmi = 0
    with open(file_dir) as f:
        sameword = f.readlines()
    for line in sameword:
        linesplit = re.split(':| |',line)
        lenth = lenth + 1
        for i in range(len(wordlist)):
            if wordlist[i] == linesplit[0]:
                lenmi = lenmi +1
    print(lenth)
    print(lenth - lenmi)            
    return(lenth - lenmi)            
        