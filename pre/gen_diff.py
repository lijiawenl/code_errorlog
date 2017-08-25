#!/usr/bin/python

__author__ = "Aubrey Li (aubrey.li@intel.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2017/06/20 10:10:10 $"
__copyright__ = "Copyright (c) 2017 Aubrey Li"
__license__ = "Python"

import sys
import os
import getopt
import difflib

similarity_threshold = 0.5
stop_pattern = "initrds=("
parent_name_pattern = "parent_dmesg"
dmesg_diff_trail = "_diff.log"

def dmesg_diff(parent_name, child_name):
    diff_name = child_name + dmesg_diff_trail
    #if os.path.exists(diff_name) == False:
    pfd = open(parent_name, 'r')
    cfd = open(child_name, 'r')
    dfd = open(diff_name, 'w')
    p_content = pfd.readlines()
    c_content = cfd.readlines()
    for (p_line, c_line) in zip(p_content, c_content):
        if stop_pattern in c_line:
            break
        seq = difflib.SequenceMatcher(None, p_line, c_line)
        if seq.ratio() < similarity_threshold:
            dfd.write(c_line)
    dfd.close()
    print(diff_name + " created")
    pfd.close()
    cfd.close()
    #else:
     #   print(diff_name + " existed")


def generate_diff(data_dir):
    list_dirs = os.walk(data_dir)
    for syspath, dirs, files in list_dirs:
        for f in files:
            if (parent_name_pattern in f):
                parent_trail = f.split("_")[1]
                child_name = parent_trail[:5]+"_"+parent_trail[5:]
                if child_name in files:
                # parent-child pair found
                    parent_name = os.path.join(syspath, f)
                    child_name = os.path.join(syspath, child_name)
                    dmesg_diff(parent_name, child_name)

##############################################
# main()
##############################################
if   __name__  ==  "__main__":

    if len(sys.argv) < 3:
        print("[Usage]: generate_diff -d <data_dir>")
        sys.exit(0)
        
    opts, args = getopt.getopt(sys.argv[1:], "d:")
    for op, value in opts:
        if op == '-d':
            data_dir = value

    generate_diff(data_dir)
