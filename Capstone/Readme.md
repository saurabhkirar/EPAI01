**Abstract.**
This is the read me for the project which aims to use concepts of python with minimal usage of out of the box libraries.
The aim of the project is to harvest the concepts of python and accumulate, consolidate and execute the concepts at one place.
The project also aims to educate the fact that nauances are very necessary for any project whihc includes validation, testing corner cases 
and making a modular and a high performing scalable code.

**Project Decription and assumptions.**
we are going to build a Python app that can:
1. read a CSV file that has NAME, SCORE and EMAIL and send out the certificates to the students.
2. compose an email with the predefined subject and placeholders for name, email, total marks and score.


**Expectations.**
1. Should run for multiple users in the csv file.
2. Scalable app that can run with minimum concurrency.
3. OS agnostic app.
4. No additonal 3 party procurement should be completely on python.
5. Easily deployable and OS agnostic.

**Custom restrictions(May not be applicable to you)**
1. Do not use loops.
2. Do not use list comprehensions.
3. Use two different custom modules.
4. Use of one or more package.
5. Use own iterator class for creating the data base.

**Repository**
The directory has the following structures with the names and the files present are.
1. Codes - contains the working python codes.
2. Data - 
         2.1 The data folder contains of the csv file which would be uploaded.
         2.2 The blank image of the certificate which would be feteched.
3. Test_Scripts.
          3.1 test_coding_standards.py-> This script predominantly does the nonmenclature and standard checks.
          3.2 Buss_validation.py-> check some of the corner cases and business validations that may very project to project.
4. Results.
           4.1 Results of few sample certificates.
           4.2 Screen shot of emails sent.
5. Out   
           5.1 Shows the certificates which once generated are stored,this is prudent to store the certs as can be very handy in resending the scenario.
6. Log.
            6.1 Log folder that contains the log file to capture variuos activities at different timestamp.
          
**Testing done**
Testing was done to capture some of the common, obvious and also rare of the corner cases like.
1. checks internet connection before doing anything.
2. checks if the certificate already exists in the folder, and if yes, then do not create it again.
3. Validtes the name, marks and email.
4. checks for authentication.

**Calling**
1. project can be called by uploading the data in the csv file(please see the data for file format under data folder)
2. Project can be called by giving the details from command line.
3. For both the cases there is a provision for recreate certificate is given, if you want to correct any certificate, please choose recreate as yes
