>>>print(' hello world') #Basic syntax for printing hello world!
hello world
>>> a=12            # addition of two numbers and printing the result in different formats using % , {}.format funtion!
>>> b= 13
>>> c =a+b
>>> print ('sum is ', c)
sum is  25
>>> print (' sum of ', a, 'and', b, 'is', c)
sum of  12 and 13 is 25
>>> print (' sum of %d and %d is %d ' %(a,b,c))
sum of 12 and 13 is 25 
>>> print (' sum of {} and {} is {}.'.format(a,b,c))
sum of 12 and 13 is 25.
>>> print (f'sum of {a} and {b} is {c}')
sum of 12 and 13 is 25
# taking input from user syntax and printing it on screen.
>>> name = input ('enter your name:')
enter your name: Mohini Vaish
>>> print ('Hello', name)
Hello  Mohini Vaish
# dealing with data types like int, float and string!
>>>  sal = int(input('enter your salary:'))
 
SyntaxError: unexpected indent # extra intendation is an error!
>>> sal = int(input('enter your salary:'))
enter your salary: 345678
>>> incentive = 2300
>>> totalsal= incentive
>>> totalsal = incentive + sal # using expressions here simple addition of variables.
>>> print(" your total salary is =",totalsal)
 your total salary is = 347978
>>> msg = input('enter your message:')
enter your message: total 3 five
>>> msg = msg.lower
>>> if msg=='hello':
	print('hi there!')
else:
	print('i dont understand')

	
i dont understand
>>> 2 + 2
4
>>> 2
2
>>> 'mohini'*3
'mohinimohinimohini'
>>> 'mohini ' * 3
'mohini mohini mohini '
>>> ' hello' + 'mohini' * 2
' hellomohinimohini'
>>> spam = 'Mohini '
>>> spam + 'Vaish'
'Mohini Vaish'
>>> spam
'Mohini '
>>> str(int(1234)) # string and int data types have to be converted first, int can't be concatenated with string or else it will show an eror as follows.
'1234'
>>> '45' +1
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    '45' +1
TypeError: can only concatenate str (not "int") to str
>>> int('45') + 1
46
>>> str('24') + 1
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    str('24') + 1
TypeError: can only concatenate str (not "int") to str
>>> str('hello') + 1
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    str('hello') + 1
TypeError: can only concatenate str (not "int") to str
>>> str('45') + "years"
'45years'
