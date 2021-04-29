**Abstract.**
This is the read me for the project which aims to use concepts of python with minimal usage of out of the box libraries.
The aim of the project is to harvest the concepts of python and accumulate, consolidate and execute the concepts at one place.
The project also aims to educate the fact that nauances are very necessary for any project whihc includes validation, testing corner cases 
and making a modular and a high performing scalable code.

**Project Decription and assumptions.**
You are going to build a Python app that can:
read a CSV file that has NAME, SCORE and EMAIL (10+, use the fact that admin@theschoolofai.in and ad.min@theschoolofai.in are the same email ids, so you can use your own for testing)
loads this image (Links to an external site.) (you can use OpenCV, PIL, or anything else you want)
copies each name from the CSV file and adds it to the image (again use OpenCV and font support there to write it on the image) along with other details. The certificate should finally read:
Award of Excellence for "COURSE NAME" Awarded to "NAME". Date 24th April 2021. Signature "FIXED NAME". You must make sure that the items are placed exactly at the location they should be and with the appropriate font size. 
learn how to send emails using Python using this tutorial (Links to an external site.). 
Then compose an email that:
will send the final certificate to the email address
reads another file where this email content is written:
**Dear NAME,

Congratulations! You have cleared the COURSE NAME with SCORE marks out of TOTAL marks!

We are excited to share the attached Award of Excellence for your performance!

Regards**

These are the things that are expected:
your code is well documented
your code has at least 50 test cases that test various problems that might be there. Some tests that are expected:
regex check for emails
can handle 1000+ emails without getting crashed 
check if names have only characters
checks if internet connection exists
checks if all required (including external) packages are installed
NAME, COURSE NAME, SCORE, TOTAL are variables and can be changed while calling your Python App
you are using at least 2 different custom modules
you are using at least 1 or more packages
you are NOT using while or for loop anywhere
you are use generators and NOT list comprehension anywhere
you are using your OWN Iterator class for creating your name, email and scores database.
you are using:
named tuples
Python's datetime module
at least 2 decorators (eg, a decorator that "knows" if internet connection is there, etc).
the certificates you attach have a proper name (not image1, etc)
all certificates are finally stored in a folder
checks internet connection before doing anything
checks if the external packages that are required (like PIL, OpenCV are already installed)
checks if the certificate already exists in the folder, and if yes, then do not create it again
emails must be sent out at a gap of 30-60 seconds (selectable while running the app)
your code automatically converts names to their "proper form", e.g. ROHAN SHRAVAN to Rohan Shravan
your app can be called from the command line while providing the variable details as well as the CSV file location
your app first runs "some of the tests" before actually sending emails
In your final submission, you need to send emails to yourself 10+ times, then add the 10+ certificates in the folder on Github along with the code, as well as the screenshot of your Gmail box showing these 10+ email along with the time stamp

**Technical topics covered.**
  Basics: Python Type Hierarchy, Multi-line statements and strings, Variable Names, Conditionals, Functions, The While Loop, Break Continue and the Try Statement, The For Loop and Classes
  Object Mutability and Interning: Variables and Memory References, Garbage Collection, Dynamic vs static Typing, Variable Re-assignment, Object Mutability, Variable Equailty, Everything is an Object and Python Interning
  Numeric Types I: Integers, Constructors, Bases, Rational Numbers, Floats, rounding, Coercing to Integers and equality
  Numeric Types II: Decimals, Decimal Operations, Decimal Performance, Complex Numbers, Booleans, Boolean Precedence and Comparison Operators
  Functional Parameters: Argument vs Parameter, Positional and keyword Arguments, Unpacking Iterables, Extended Unpacking, __*args_, Keyword Arguments, __**kwags_, Args and Kwargs together, Parameter Defaults and Application
  First Class Functions Part I: Lambda Expressions, Lambdas and Sorting, Functional Introspection, Callables, Map, Filter, Zip and List Comprehension
  First Class Functions Part II: List Comprehension, Reducing functions, Partial Functions, Operator Module, Docstrings and Annotations.
  Scopes and Closures: Global and Local Scopes, Nonlocal scopes, Closures, and Closure Applications
  Decorators: Decorators and Decorator applications (timers, logger, stacked decorators, memoization, decorator class and dispatching)
  Tuples and Named Tuples: Tuples, Tuples as data structures, named Tuples, DocStrings, and Application
  Modules, Packages and Namespaces: Module, Python Imports, importlib, import variants, reloading modules, __main__, packages, structuring, and namespaces
  fStrings, Timing Functions and Command Line Arguments: Dictionary Ordering, kwargs, tuples, fStrings, Timing Functions and Command Line Arguments
  Sequence Types I: Sequence Types, Mutable Sequence Types, List vs Tuples, Index Base and Slice Bounds, Copying Sequence and Slicing
  Sequence Types II and Advanced List Comprehension: Custom Sequences, In-place Concatenation and Repetition, Sorting Sequences, List Comprehensions + Small Project
  Iterables and Iterators: Iterating Collections, Iterators, Iterables, Cyclic Iterators, in-built Iterators, iter() function and iterator applications
  Generators and Iteration Tools: Yielding and Generator Functions, Generator Expressions, Yield
