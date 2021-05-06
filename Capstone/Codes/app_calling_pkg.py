# -*- coding: utf-8 -*-
'''
app_calling_pkg.py
*******************************************************************
Purpose: A generic utility that can be used across the modules.

                      Revision history

Version  Author           Date(yyyy/mm/dd)   Version
1.0      Saurabh Kirar    2020/04/20         Initial creation
*******************************************************************

'''

import os
project_path='/content/drive/MyDrive/EPAI/Capstone/Codes/'
image_path='/content/drive/MyDrive/EPAI/Capstone/Data/'
data_file=image_path+'learner_data.csv'
out_path='/content/drive/MyDrive/EPAI/Capstone/Out/'
log_path='/content/drive/MyDrive/EPAI/Capstone/Log/'
Image_name=image_path+'Cert.jpg'
sender_email='souravkirar@gmail.com'
subject = "Congratutations on course completion!!"
os.chdir(project_path)

pwd

import os
import validation
import certificate_pkg
from functools import partial

'''get the key'''
key=validation.PasswordHelper(sender_email)

key.password

certificate_pkg.send_certificate()

'''create the parials for quick processing'''
EAPI_resend=partial(certificate_pkg.send_certificate,p_sender_email=sender_email,p_key=key.password,p_course_name='EPAI',p_total=1000,p_recreate=True)
EAPI_create=partial(certificate_pkg.send_certificate,p_sender_email=sender_email,p_key=key.password,p_course_name='EPAI',p_total=1000,p_recreate=False)

certificate_pkg.data_loader

'''Load the file , make sure that the path is correct'''
fil=certificate_pkg.data_loader(data_file)
fil_iter=iter(fil)
header=fil_iter.learner_header

'''This step will  create the iterator'''
iterable_value = fil_iter.learner_list
iterable_obj = iter(iterable_value)

'''
The below step is use to send the email in bulk.
This is the advantage of creating the partial functions as we can only have less arguments to be passed
while remaining are defaulted
'''
list(map(lambda rec:EAPI_create(
                                p_user_name=rec[0]
                                ,p_score=int(rec[2])
                                ,p_receiver_email=rec[3]),fil_iter.learner_list))