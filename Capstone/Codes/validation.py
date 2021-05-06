# -*- coding: utf-8 -*-
'''
Validation.ipynb
*******************************************************************
Purpose: A generic utility that can be used across the modules.

                      Revision history

Version  Author           Date(yyyy/mm/dd)   Version
1.0      Saurabh Kirar    2020/04/20         Initial creation
1.1      Saurabh Kirar    2020/04/30        Added password helper class
*******************************************************************

'''
import logging
import os
import socket
from datetime import datetime
import getpass
from functools import wraps
import email, smtplib, ssl
context = ssl.create_default_context()
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ntpath
import os
import re
log_path='/content/drive/MyDrive/EPAI/Capstone/Log/'
log_file=log_path+'EPAI.log'

__all__ = ['logging_decorator','internet_check_decorator','PasswordHelper','authentication_decorator']

class PasswordHelper:
    """
    A class to manage user password.
    ...
    Attributes
    ----------
    sender_email : str
        Sender's email id
    password: str
        Sender's password
    Methods
    -------
    __init__():
        Class constructor 
    """
    def __init__(self,sender_email=None):
        """
        Class constructor. Asks user for email password and saves it.
        Parameters:
            sender_mail(str): Sender email id
        Returns:
            class object
        """
        self.sender_email = sender_email
        self.password = None
        if self.sender_email:
            self.password = getpass.getpass(f"Please Enter Password for {self.sender_email}...")

def file_logging(file_name,msg):
    """
    This function appends given message to given log file.
    Parameters:
        file_name(str): Log file name
        msg(str): Message to be appended to log file
    Returns:
        None
    """
    # Get current time and date in the form of string
    date_time_str = datetime.now().strftime("[%d/%m/%Y, %H:%M:%S.%f] ")
    # Open file in append mode and write message into it with proper datetime stamp
    with open(file_name,mode="a+") as fid:
        fid.write("\n" + date_time_str + msg+"\n")


def logging_decorator(log_file_name=log_file):
    """
    Usage - This is a decoraor factory for logging.
    this utility would be used across the functions for logging.
    Parameters:
        log_file_name(str): Log file name defaults to EPAI.log
    Returns:
        decorator: decorator to log function(logging_func)
    """
    def logging_func(function):
        @wraps(function)
        def func_to_be_lgd(*args,**kwargs):
            file_logging(log_file_name,f"{function.__name__} - {args} - {kwargs}")
            try:
                output = function(*args,**kwargs)
                file_logging(log_file_name,f"{function.__name__} returned: {output}")
                return output
            except Exception as e:
                file_logging(log_file_name,f"ERROR: {function.__name__}: Exception:{e}")
                raise e
        return func_to_be_lgd
    return logging_func

def is_connected():
    import socket
    '''This is a function that is used to check if the iternet is up and responsing
     Usage - This would be used as a decorator for other functions'''
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True,'hi'
    except OSError:
        pass
    return False,'hello'

def internet_check_decorator() -> 'decorator':
    """
    Decorator factory to check if internet is connected before calling
    a function.
    """
    def internet_working_deco(fn):
        '''decorator for a working connection'''
        @wraps(fn)
        def inner(*args, **kwargs):
            return fn(*args, **kwargs)
        return inner

    def internet_failure_deco(fn):
        '''decorator for a non working connection'''
        @wraps(fn)
        def inner(*args, **kwargs):
            msg= "No internet connection"
            return False,msg
        return inner

    if (is_connected()):
        return internet_working_deco
    else:
        return internet_failure_deco

def is_authenticated(p_email,p_key):
  '''This function will check if the sender is authenticated or not'''
  if "@gmail." not in p_email:
        msg="you are not authenticated,Only Gmail is allowed"
        return False
  try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(p_email, p_key)
        msg="Authentication Sucessful"
        return True
  except smtplib.SMTPAuthenticationError as serr:
        msg="Invalid credentials"
        return False

def authentication_decorator():
  '''Factory decorator for the authentication'''

  def auth_succes(fn):
    ''' decorator for the Success '''
    @wraps(fn)
    def func_to_be_executed(*args,**kwargs):
       return fn(*args,**kwargs)
    return func_to_be_executed

  def auth_failure(fn):
    ''' decorator for the Success '''
    @wraps(fn)
    def func_to_be_executed(*args,**kwargs):
       return  False,'Authentication Failure'
    return func_to_be_executed
   
  if is_authenticated(p_email,p_key):
    return auth_succes
  else:
    return auth_failure

@logging_decorator()
def check_mail_format(p_mail,**kwargs):
    """
    Function to check if given email id is valid.
    Parameters:
        email (str): Email id to be checked
    Returns:
        validity(bool): Email id is valid or not
    """
    # Create regex pattern for valid email id.
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    # if structure defined in regex is found email id is valid
    if(re.search(regex, p_mail)):
        msg='email sucessfully validated'
        return True,msg
    else:
        msg='Please check the email format'
        return False,msg

def validate_name(p_name):
  '''
  This function validates the name and calls out any abmibuity
    Parameters:
        name (str): name to be verified
    Returns:
        validity(bool): name  is valid or not
  '''
  if   len(re.findall("[@_!#$%^&*()<>?/\|}{~:]", p_name)) > 0:
                msg ="Special characters are not allowed in student name."
                return False,msg
  elif len(re.findall("[0-9]", p_name)) > 0:
                msg="Numeric characters are not allowed in student name."
                return False,msg
  else :
                msg='Name Sucessfully validated'
                return True,msg

def validate_score(p_score,p_total):
  '''This function validates the scores
  Parameters:
        name (str): name to be verified
    Returns:
        validity(bool): name  is valid or not
  '''
  if p_score > p_total:
    msg='Vaidation error,score can not be greater than total'
    return False,msg
  
  elif p_score<0:
    msg='Score can not be negative, no provision for negative marking'
    return False, msg
  
  elif p_total <= 0:
    msg='Total marks has to be greater than zero'
    return False, msg
  
  else :
    msg='Score and total marks validated sucessfully.'
    return True, msg