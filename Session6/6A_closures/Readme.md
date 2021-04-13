This excercise is an assignment for closures.

Closures in python are functions that can access the variable not defined into their scopes.
A closure allows you to bind variables into a function without passing them as parameters.
Closures are often returned as a function and hence if a function is defined as the sub function and enclosed as a closure the return of the outer function as the innner function stress
the very point that the inner function now can be called outside the scope of the outer function as well.
so the three main characterstics of the closure are.
-> it is a nested function. 
->it has access to a free variable in outer scope. 
-> it is returned from the enclosing function.

Lets take an example how it works. Here we have defined an outer function that returns a function (inner) and has a variable defined as var1.
the closure inner access the variable var1 and now powerful to edit the variable as well.
def outer():
    var1='hi'
    def inner():
        non local var1
        var1='hello'
     return inner
     
Next dcall the outer function, the outer function is executed and it returns a function, ideally speaking all the variables which are defined in the outer function scope 
should have been vanished as the execution of outer function is over but thats not the case as we have defined a closure that can access the variable defined on outer function.

 outer_call= outer() 
 
 now since we are calling this object the inner function will get executed and we can access the var1.
 outer_call() 
 
 Hence closure helps to access the variables which are defined by the parent function even though the function execution is over.
