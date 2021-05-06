# -*- coding: utf-8 -*-
'''
Biz_validation.py
*******************************************************************
Purpose: A generic utility to run business specific test cases

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



# Test whether app rejects data file without header.
def check_header():

    with open('temp_data.csv',"w") as f:
        writer = csv.writer(f)
        writer.writerow(["Saurabh Kirar","4500","saurabh.kirar09@gmail.com"])

    result = certificate_pkg.send_certificate(csv_file_name='temp_data.csv',course_name="EPAi2",
    sign_name= "School of AI",total_marks=5000,sender_email="gaurav4664.test@gmail.com",mail_interval=2,
    certi_dir='./certificates',overwrite=False,create_certi_only=True,verbose=False)
    assert result==False," file doesn't have a header"

# Test whether app rejects data file with invalid header. Invalid header means minimum required 
# fields (name,score,email) not found 
def check_missing_data():

    with open('temp_data.csv',"w") as f:
        writer = csv.writer(f)
        writer.writerow(["name","score"])
        writer.writerow(["Saurabh Kirar","4500","saurabh.kirar09@gmail.com"])

    result = certificate_pkg.send_certificate(csv_file_name='temp_data.csv',course_name="EPAi2",
    sign_name= "School of AI",total_marks=5000,sender_email="saurabh.kirar09@gmail.com",mail_interval=2,
    certi_dir='./certificates',overwrite=False,create_certi_only=True,verbose=False)
    assert result==False,"Incomplete header"

# Test whether app rejects empty data file.
def check_data_file():

    with open('temp_data.csv',"w") as f:
        writer = csv.writer(f)

    result = certificate_pkg.send_certificate(csv_file_name='temp_data.csv',course_name="EPAi2",
    sign_name= "School of AI",total_marks=5000,sender_email="saurabh.kirar09@gmail.com",mail_interval=2,
    certi_dir='./certificates',overwrite=False,create_certi_only=True,verbose=False)
    assert result==False,"Data file empty"

# Test whether app rejects data file with only header and no data.
def check_records():

    with open('temp_data.csv',"w") as f:
        writer = csv.writer(f)
        writer.writerow(["name","score","email"])

    result = certificate_pkg.send_certificate(csv_file_name='temp_data.csv',course_name="EPAi2",
    sign_name= "School of AI",total_marks=5000,sender_email="saurabh.kirar09@gmail.com",mail_interval=2,
    certi_dir='./certificates',overwrite=False,create_certi_only=True,verbose=False)
    assert result==False,"Invalid records"


# Test whether app rejects invalid data. Invalid data could be more data on certain rows 
# than the header mentions.
def test_reject_invalid_data_file():

    with open('temp_data.csv',"w") as f:
        writer = csv.writer(f)
        writer.writerow(["name","score","email"])
        writer.writerow(["Saurabh Kirar","4500","saurabh.kirar09@gmail.com","12345678"])

    result = certificate_pkg.send_certificate(csv_file_name='temp_data.csv',course_name="EPAi2",
    sign_name= "School of AI",total_marks=5000,sender_email="saurabh.kirar09@gmail.com",mail_interval=2,
    certi_dir='./certificates',overwrite=False,create_certi_only=True,verbose=False)
    assert result==False,"Invalid records"



def check_name():

    first_name = "sample"
    last_name = "sample_sample"
    with open('temp_data.csv',"w") as f:
        writer = csv.writer(f)
        writer.writerow(["name","score","email"])
        writer.writerow([first_name+" "+last_name,"4500","saurabh.kirar09@gmail.com"])

    certi_dir = "test_certificates"

    # remove directory if already exists. The app will create the directory and put certificates there.
    dirpath = Path('.', certi_dir)
    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)

    result = certificate_pkg.send_certificate(csv_file_name='temp_data.csv',course_name="EPAi2",
    sign_name= "School of AI",total_marks=5000,sender_email="saurabh.kirar09@gmail.com",mail_interval=2,
    certi_dir=certi_dir,overwrite=False,create_certi_only=True,verbose=False)

    created_file = glob.glob("./"+certi_dir+"/*.jpg")[0]

    assert first_name in created_file
    assert last_name in created_file



def check_course():

    first_name = "Saurabh"
    last_name = "Kirar"
    course_name = "EPAi2"

    with open('temp_data.csv',"w") as f:
        writer = csv.writer(f)
        writer.writerow(["name","score","email"])
        writer.writerow([first_name+" "+last_name,"4500","saurabh.kirar09@gmail.com"])

    certi_dir = "test_certificates"

    # remove directory if already exists. The app will create the directory and put certificates there.
    dirpath = Path('.', certi_dir)
    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)

    result = certificate_pkg.send_certificate(csv_file_name='temp_data.csv',course_name=course_name,
    sign_name= "School of AI",total_marks=5000,sender_email="saurabh.kirar09@gmail.com",mail_interval=2,
    certi_dir=certi_dir,overwrite=False,create_certi_only=True,verbose=False)

    created_file = glob.glob("./"+certi_dir+"/*.jpg")[0]

    assert course_name in created_file



# test if it can handle more than 1000 student data
def check_volume():
    # Since sending so many mails is not feasible. We will just test whether app is
    # able to generate more than 1000 student certificate.
    num_students = 1000
    # lets first create a csv file containing 1001 fake student data
    with open('large_data.csv',"w") as f:
        writer = csv.writer(f)
        writer.writerow(["name","score","email"])
        fake = Faker()
        for i in range(num_students):
            fake_profile = fake.profile()
            random_subscript = ''.join(random.choice(string.ascii_letters) for x in range(5))
            writer.writerow([fake_profile['name']+ random_subscript,str(random.randint(100,1000)),fake_profile['mail']])
    certi_dir = "test_certificates"

    # remove directory if already exists. The app will create the directory and put certificates there.
    dirpath = Path('.', certi_dir)
    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)

    result = certificate_pkg.send_certificate(csv_file_name='large_data.csv',course_name="EPAi2",
    sign_name= "School of AI",total_marks=5000,sender_email="saurabh.kirar09@gmail.com",mail_interval=2,
    certi_dir=certi_dir,overwrite=True,create_certi_only=True,verbose=False)

    # Find out how many certificates have been created.
    assert len(glob.glob("./"+certi_dir+"/*.jpg"))==num_students, f"check for volume(1000) records atleast."

# test to check regex in emails
def test_regex_email_1():
    # lets first create a csv file containing invalid email id
    with open('temp_data.csv',"w") as f:
        writer = csv.writer(f)
        writer.writerow(["name","score","email"])
        writer.writerow(["Saurabh Kirar","4500","saurabh.kirar09@gmail.com"])
        writer.writerow(["sample sample2,"25","junk_gmail.com"])

    certi_dir = "test_certificates"
    # remove directory if already exists. The app will create the directory and put certificates there.
    dirpath = Path('.', certi_dir)
    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)

    result = certificate_pkg.send_certificate(csv_file_name='temp_data.csv',course_name="EPAi2",
    sign_name= "School of AI",total_marks=5000,sender_email="saurabh.kirar09@gmail.com",mail_interval=2,
    certi_dir=certi_dir,overwrite=False,create_certi_only=True,verbose=False)

    # Only one certificate should be created
    assert len(glob.glob("./"+certi_dir+"/*.jpg"))==1, f"App should reject invalid email id."




def check_name_for_numbers():

    # lets first create a csv file containing invalid email id
    with open('temp_data.csv',"w") as f:
        writer = csv.writer(f)
        writer.writerow(["name","score","email"])
        writer.writerow(["Saurabh Kirar","4500","saurabh.kirar09@gmail.com"])
        writer.writerow(["sample sample2","4500","Saurabh4664@yahoo.com"])

    certi_dir = "test_certificates"

    # remove directory if already exists. The app will create the directory and put certificates there.
    dirpath = Path('.', certi_dir)
    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)

    result = certificate_pkg.send_certificate(csv_file_name='temp_data.csv',course_name="EPAi2",
    sign_name= "School of AI",total_marks=5000,sender_email="saurabh.kirar09@gmail.com",mail_interval=2,
    certi_dir=certi_dir,overwrite=False,create_certi_only=True,verbose=False)

    # Only one certificate should be created
    assert len(glob.glob("./"+certi_dir+"/*.jpg"))==1, f"Reject if numbers found in the name."  

def test_student_name_special_char_check():

    # lets first create a csv file containing invalid email id
    with open('temp_data.csv',"w") as f:
        writer = csv.writer(f)
        writer.writerow(["name","score","email"])
        writer.writerow(["Saurabh@Kirar","4500","saurabh.kirar09@gmail.com"])

    certi_dir = "test_certificates"

    # remove directory if already exists. The app will create the directory and put certificates there.
    dirpath = Path('.', certi_dir)
    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)

    result = certificate_pkg.send_certificate(csv_file_name='temp_data.csv',course_name="EPAi2",
    sign_name= "School of AI",total_marks=5000,sender_email="saurabh.kirar09@gmail.com",mail_interval=2,
    certi_dir=certi_dir,overwrite=False,create_certi_only=True,verbose=False)

    # Only one certificate should be created
    assert len(glob.glob("./"+certi_dir+"/*.jpg"))==1, f"Reject if  special characters found in the name"


def check_totals():

    with open('temp_data.csv',"w") as f:
        writer = csv.writer(f)
        writer.writerow(["name","score","email"])
        writer.writerow(["Saurabh Kirar","45000","saurabh.kirar09@gmail.com"])

    certi_dir = "test_certificates"

    # remove directory if already exists. The app will create the directory and put certificates there.
    dirpath = Path('.', certi_dir)
    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)

    result = certificate_pkg.send_certificate(csv_file_name='temp_data.csv',course_name="EPAi2",
    sign_name= "School of AI",total_marks=5000,sender_email="saurabh.kirar09@gmail.com",mail_interval=2,
    certi_dir=certi_dir,overwrite=False,create_certi_only=True,verbose=False)

    # Only one certificate should be created
    assert len(glob.glob("./"+certi_dir+"/*.jpg"))==1, f"marks obtained cant be greater than total marks."


def check_sender_mail():

    csv_file_name = "test_data.csv"
    certi_dir = "test_certificates"
    sign_name = "School of AI"
    course_name = "EPAi2"
    total_marks = 5000
    sender_email = "saurabh.kirar09@gmail"

    result = certificate_pkg.send_certificate(csv_file_name=csv_file_name,course_name=course_name,
    sign_name= sign_name,total_marks=total_marks,sender_email=sender_email,mail_interval=2,
    certi_dir=certi_dir,overwrite=False,create_certi_only=True,verbose=False)

    assert result == False,"App should check for invalid sender email id"

