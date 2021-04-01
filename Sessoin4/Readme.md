
This is an excerise to understand numerical types and functional arguments.
Arguments are positoional and keywords and python provides the flexibility to put any number of positional or keyword arguments provided a norm is followed.
Single asteric * is used to denote the postional arguments like * args and double asteric is uded to denote the key word arguments **kwargs.

In this excercise we aim to write a generic function that can time the different function.
which means a meta function which would be used as a driver to drive the various functions.

So in simple words if we have to get the performance of any function we need the start and end time plus no of iterations and then the total time would be divided by no of iterations to get the mean time.

Few of the functions are.

1. squared_power_list - to calculate the square given any list.
2. polygon_area - to calculate the area of any given polygon.
3. temp_converter - convert the temperature from one scale to another.
4. speed_converter - to convert the speed from one scale to other.


**time_it** - This would be a generic function that takes the above said function as one of the argument and also the arguments needed by the other functions so essentially the signature of the time_if function would be.
time_it(fn, *args, repetitons= 1, **kwargs):
