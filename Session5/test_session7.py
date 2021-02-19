# -*- coding: utf-8 -*-


import pytest
import session7
import os
import inspect
import re
'''
def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"
 '''   
def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session7)
    spaces = re.findall('\n +.', lines)
    line_no =1
    for space in spaces:
        line_no +=1
        print('=====', line_no, space)
        #print(lines)
        #assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        #assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 
        assert re.search('[a-zA-Z#@=1234\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@=1234\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"
    
def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_check_fibonocci_for_fibonocci_numbers():
    assert session7.check_fibonocci(13), "check_fibonocci function is not working properly in identifying for fibonocci numbers" 

def test_check_fibonocci_for_non_fibonocci_numbers():
    assert not(session7.check_fibonocci(90)), "check_fibonocci function is not working properly in identifying non fibonocci numbers"
    
def test_add_iterables_even_odd():
    assert session7.add_iterables_even_odd([1,22,33,4],(1,3,2,7)) == [25,11], "add_iterables_even_odd function is not working properly"
    
def test_strip_vowels():
    assert session7.strip_vowels('tsai') == 'ts', "strip_vowels function is not working properly"    

def test_relu_func():
    assert session7.relu_func([1,2,3,4,0,-1,-2]) == [1, 2, 3, 4, 0, 0, 0], "relu_func function is not working properly"

def test_sigmoid_func():
    assert session7.sigmoid_func([12,1]) == [0.9999938558253978, 0.7310585786300049], "sigmoid_func function is not working properly"   
 
def test_profanity_check():
    assert session7.profanity_check('ImageDataBunch- Is a helper class for doing ML tasks on a dataset of images easily. It has various helper functions which create PyTorch based objects. I will go more in detail over this in next post'), "profanity_check function is not working properly"
    
def test_add_even_no():
    m1=[2,3,5,6,8,19,12,17,22]
    assert session7.add_even_no(m1) == 50, "add_even_no function is not working properly"    
    
def test_find_biggest_char():
    m1 = "goodbaduglyzz"
    assert session7.find_biggest_char(m1) == 'z', "find_biggest_char function is not working properly" 
    
def test_add_every_third_no():
    m1=[2,3,5,6,8,11,12,15,22]
    assert session7.add_every_third_no(m1) == 38, "add_every_third_no function is not working properly" 

def test_generate_number_plate_hardcoded():
    assert bool(session7.generate_number_plate_hardcoded()), "generate_number_plate_hardcoded function is not working properly"
    
def test_get_number_plate():
    assert bool(session7.get_number_plate("KD")), "get_number_plate function is not working properly"