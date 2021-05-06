# -*- coding: utf-8 -*-
'''
certificate_pkg.py
*******************************************************************
Purpose: A generic utility that can be used across the modules.

                      Revision history

Version  Author           Date(yyyy/mm/dd)   Version
1.0      Saurabh Kirar    2020/04/20         Initial creation
1.1      Saurabh Kirar    2020/04/30        commented hardcodings
*******************************************************************

'''

## start of the project.

import os
project_path='/content/drive/MyDrive/EPAI/Capstone/Codes/'
image_path='/content/drive/MyDrive/EPAI/Capstone/Data/'
data_file=image_path+'learner_data.csv'
out_path='/content/drive/MyDrive/EPAI/Capstone/Out/'
log_path='/content/drive/MyDrive/EPAI/Capstone/Log/'
Image_name=image_path+'Cert.jpg'
subject = "Congratutations on course completion!!"
os.chdir(project_path)

import cv2
import smtplib
from PIL import Image, ImageDraw, ImageFont
from datetime import date
import os
import validation
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
import os
import re
import json
import cv2
#import img2pdf
import getpass
from datetime import datetime
import time
from collections import namedtuple
from functools import partial,wraps

def create_or_locate_cert(p_course,p_name,p_recreate):

    '''This functions creates the certificate for a given user and the course 
     and stores the certificates in the out directory
     If for a user and the course the certificate already exists then the function fectes the certificate 
     from the out directory and returns the cert, if not then fuction goes on to make a new certificate
     '''
    course = p_course
    name = p_name
    color = 'rgb(0, 0, 0)' # black color
       # if exists and overwrite is False simply return with certificate path
    img=out_path+name+course+'cert.jpg'
    if (not p_recreate) and (os.path.exists(img)):
            print(f'Certificate already exists,resending')
            return img

    # create Image object with the input image
    image = Image.open(Image_name)
    # initialise the drawing context with the image object as background
    draw = ImageDraw.Draw(image)
    # create font object with the font file and specify desired size   
    font_course = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Bold.ttf", size=20)
    # starting position of the message
    (x, y) = (450, 270)
    # draw the message on the background
    draw.text((x, y), course, fill=color,font=font_course)

    font_name = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Bold.ttf", size=30)
    (x, y) = (450, 420)
    draw.text((x, y), name, fill=color,font=font_name)


    font_date = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Bold.ttf", size=30)
    (x, y) = (235, 500)
    today = date.today()
    today=str(today)
    draw.text((x, y), today, fill=color,font=font_name)

    font_sign = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSansNarrow-Bold.ttf", size=30)
    (x, y) = (650, 500)
    admin_name = 'School of AI'
    draw.text((x, y), admin_name, fill=color,font=font_name)
    
    # save the edited image
    img=out_path+name+course+'cert.jpg'
    #print('saving..')
    #print(img)
    image.save(img)

    #I=cv2.imread(img)
    #plt.imshow(I)
    
    return img

@validation.logging_decorator()
@validation.internet_check_decorator()
def send_certificate(p_sender_email,p_receiver_email,p_key,p_user_name,p_course_name,p_score,p_total,p_recreate=False):
    '''This is a function which will send the certificate and can be called with the below params
    p_receiver_email-> Receiver email address.
    p_key-> Password for email account (sender)
    p_user-> User to whom the certificate should go
    p_course_name-> the name of the course for which the certs are being awarded
    p_score/p_total -> marks obtained/total marks
    p_recreate->Re create the certficiate even if it exists(chances of correction)
    '''

    sender_email=p_sender_email
    print(sender_email)
    receiver_email = p_receiver_email
    password = p_key
      # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    '''
    Before constructing the certificate lets validate the parameters first.
    Lets also get all the errors in one go and inform upstream so that one can rectify at once.
    '''
    mail_res,mail_msg=validation.check_mail_format(p_receiver_email)

    name_res,name_msg=validation.validate_name(p_user_name)

    score_res,score_msg=validation.validate_score(p_score,p_total)

    if not (mail_res and name_res and score_res):
      err_msg=mail_msg+' - '+name_msg+' -'+score_msg
      raise Exception(err_msg)
    else:
      body='''
          Dear {name},

          Congratulations!

          You have cleared the {course_name} with {score} marks out of {total} marks! 
          
          We are excited to share the attached Award of Excellence for your performance!

          Regards
          '''.format(name=p_user_name,course_name=p_course_name,score=p_score,total=p_total)

  # Add body to email
    message.attach(MIMEText(body, "plain"))

    #filename = "BroadBandAug20.pdf"  # In same directory as script
    filename=create_or_locate_cert(p_course_name,p_user_name,p_recreate)

    with open(filename, "rb") as attachment:
      # Add file as application/octet-stream
      # Email client can usually download this automatically as attachment
      part = MIMEBase("application", "octet-stream")
      part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

#send_certificate(p_receiver_email='saurabh.kirar09@gmail.com'
#                 ,p_key='Pwd@gmailold2210'
#                 ,p_user_name='SK'
#                 ,p_course_name='EPAI'
#                 ,p_score=98
#                 ,p_total=990
#                 ,p_recreate=False)

## load the data from the csv file.
class data_loader:
  '''This class will read the csv file and load the data.
  purpose - to read and validate the data for certificate mailer
  arguments - file.
  methods - 
  '''
  def __init__(self,p_file):
    '''
    This is the initialization function which wil be used to initialize the values
    the values initialzed are the name of the data file, the header and data lenght
    '''
    self.data_file=p_file
    self.learner_counter=0
    self.file_header=None

    #print('hi')
    try:
      with open(self.data_file) as data_file:
        learners=csv.reader(data_file)
        self.learner_header=next(learners)   ## This gives the first row which is headers.
        self.learner_header = list(map(lambda x:x.strip().lower().replace(' ','_'),self.learner_header))  ## convert into lower and handle space
       
        res,val =self.check_header()  ## check the header format for any anomaly 
        msg=val
        ## Check the result and raise an alarm for False condition.
        if not res:
          raise Exception(msg)
        ## continue as header is in good format.
        self.learner_list=list(learners)
        ## exclude the header
        #self.learner_data=learner_list[1:]
      ## check number of learners.
      self.num_learners=len(self.learner_list)
      '''
       with open(self.csv_file_name) as f:
                    csv_reader = csv.reader(f)
                    self.csv_header = next(csv_reader)
                    self.csv_header = list(map(lambda x:x.strip().lower().replace(' ','_'),self.csv_header))
                    if not self.is_header_valid():
                        self.csv_header = None
                        raise Exception("Invalid Header!!!")
                    self.csv_data = list(csv_reader)
                self.data_length = len(self.csv_data)
      '''
      if self.num_learners < 1:
        err='Empty file. no learner details present'
        raise Exception(err)
    except FileNotFoundError as FNF:
      msg='Invalid file path.'
      raise FNF
    except:
      raise

  def __iter__(self):
    return self

  def __next__(self):
    print('num_learners',self.num_learners)
    print('learner counter',self.learner_counter)
    if self.learner_counter >= self.num_learners:
      raise StopIteration
    else:
      data = self.learner_list[self.learner_counter]
      self.learner_counter += 1
    return data


  def check_header(self):
    '''
    This function is used to check the header to ensure file provided is of correct format.
    If the file is not in the correct format then we do not proceed and ask the user to correct the file.
    '''
    #print(self.learners)
    if not ('first_name' in self.learner_header):
      err='Invalid format, missing " first name".'
      return False,err

    elif not ('last_name' in self.learner_header):
      err='Invaild format,missing "score".'
      return False,err
     
    elif not ('score' in self.learner_header):
      err='Invaild format,missing "score".'
      return False,err

    elif not ('email' in self.learner_header):
      err='Invalid format,missing "email".'
      return False,err

    else:
      err='Header validated'
      return True,err