Python 3.3.1 (default, Apr 17 2013, 22:30:32) 
Type "copyright", "credits" or "license" for more information.

IPython 0.13.2 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: 
In [1]: 
In [2]: 
In [3]: Monthly Payment= 50
Number of Months needed: 7
Balance: -30.22

In [4]:   C-c C-c---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-4-bbd07922ef73> in <module>()
----> 1 __pyfile = open('''/tmp/py3482pIk''');exec(compile(__pyfile.read(), '''/home/harry/git/MIT6.00/p-set1-b.py''', 'exec'));__pyfile.close()

/home/harry/git/MIT6.00/p-set1-b.py in <module>()
     16 
     17 
---> 18 
     19 
     20 

KeyboardInterrupt: 

In [5]: Monthly Payment= 40
Number of Months needed: 9
Balance: -12.56

In [6]: Monthly Payment= 39
Number of Months needed: 7
Balance: -34.73

In [7]: Monthly Payment= 48
Number of Months needed: 1
Balance: -0.82

In [8]:   C-c C-c---------------------------------------------------------------------------
KeyboardInterrupt                         Traceback (most recent call last)
<ipython-input-8-96c933f9d337> in <module>()
----> 1 __pyfile = open('''/tmp/py3482CxF''');exec(compile(__pyfile.read(), '''/home/harry/git/MIT6.00/p-set1-b.py''', 'exec'));__pyfile.close()

/home/harry/git/MIT6.00/p-set1-b.py in <module>()
     19         numMonths += 1
     20         interest = monthlyInterest * balance
---> 21         balance -= monthlyPayment
     22         balance += interest
     23 balance = round(balance,2)

KeyboardInterrupt: 

In [9]: who
balance	 initialBalance	 interest	 interestRate	 monthlyInterest	 monthlyPayment	 numMonths	 

In [10]: whois
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-10-1c291a11b5ee> in <module>()
----> 1 whois

NameError: name 'whois' is not defined

In [11]: help
Out[11]: Type help() for interactive help, or help(object) for help about object.

In [12]: 
