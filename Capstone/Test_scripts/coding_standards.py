# -*- coding: utf-8 -*-
'''
coding_standards.py
*******************************************************************
Purpose: A generic utility that can be used to test basic coding standards.

                      Revision history

Version  Author           Date(yyyy/mm/dd)   Version
1.0      Saurabh Kirar    2020/04/20         Initial creation
*******************************************************************

'''
# -*- coding: utf-8 -*-
import pytest
import random
import string
import certificate_pkg
import os
import glob
import inspect
import re
import math
import pkgutil
import csv
from pathlib import Path
import shutil
from faker import Faker



README_CONTENT_CHECK_FOR = [
    'Usage',
    'template',  
]

def check_readme():
    assert os.path.isfile("README.md"), "README.md file missing!"


def check_readme_format():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10  

def check_readme_lenght():
    readme_words=[word for line in open('README.md', 'r', encoding="utf-8") for word in line.split()]
    assert len(readme_words) >= 500, "Less Read me, please elaborate the project

def check_func_name():
    functions = inspect.getmembers(certificate_mailer, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def check_inden_formatting():
    # list all the files is current directory
    files = glob.glob("./" + '/**/*.py', recursive=True)
    # Now for each of the files check if line starts with 'for' or 'while' and ends with ':'.
    for f in files:
        print("Testing ",f)
        with open(f) as fid:
            contents = fid.read()
            spaces = re.findall('\n +.', contents)
            for i,space in enumerate(spaces):
                print(i,space,len(space))
                assert len(space) % 4 == 2, f"Your script contains misplaced indentations"
                assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"    

def check_datetime():
    files = glob.glob("./" + '/**/*.py', recursive=True)
    datetime_used = False
    for f in files:
        if f.find('test') == -1:
            with open(f) as fid:
                contents = fid.read()
                datetime_used = datetime_used or ('datetime' in contents)

    assert datetime_used, "datetime not used"

def check_loops():
    files = glob.glob("./" + '/**/*.py', recursive=True)
    for f in files:
        if f.find('test') == -1:
            with open(f) as fid:
                for line in fid.readlines():
                    line = line.strip()
                    assert not ((line.startswith('for') and line.endswith(':')) or 
                    (line.startswith('while') and line.endswith(':'))),f'found loops manually see for generaotrs instaed of list comprehensions {f}'
                    
def check_namedtuples():
    files = glob.glob("./" + '/**/*.py', recursive=True)
    namedtuple_used = False
    for f in files:
        if f.find('test') == -1:
            with open(f) as fid:
                contents = fid.read()
                namedtuple_used = namedtuple_used or ('namedtuple' in contents)

    assert namedtuple_used, "namedtuple not used"

def check_list_com():
    files = glob.glob("./" + '/**/*.py', recursive=True)
    print("To be inspected: ",files)
    for f in files:
        if f.find('test') == -1:
            with open(f) as fid:
                for line in fid.readlines():
                    line = line.strip()
                    assert not ((line.find(' for') >=0) and line.endswith(']')),f'Found list comprehensions {f}'

def check_decorators():
    files = glob.glob("./" + '/**/*.py', recursive=True)
    decorator_set = set()
    for f in files:
        with open(f) as fid:
            for line in fid.readlines():
                line = line.strip()
                if line.startswith('@'):
                    decorator_set.add(line)
    assert len(decorator_set)>=2,"There should be atleast 2 decorators"


def check_doc_strings():
    list_functions = inspect.getmembers(certificate_mailer,inspect.isfunction)
    for fn in list_functions:
        print(fn)
        assert fn[1].__doc__ != None , f"{fn[0]}: Doc string Missing"
