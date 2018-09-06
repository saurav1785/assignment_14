#Question.1- Write a python program to print the cube of each value of a list using list comprehension.
#Answer
n=int(input('Enter size of list:'))
lst=[int(input()) for i in range (n)]
print('Input List:',lst)
lst2=[j**3 for j in lst]
print('Cubed List:',lst2)

#Question.2- Write a python program to get all the prime numbers in a specific range using list comprehension.
#Answer
low=int(input('Enter the lower limit:'))
high=int(input('Enter the upper limit:'))
lst=[i for i in range(low,high+1) if i>1 if all(i%j!=0 for j in range(2,i))]
print('Prime List:',lst)

#Question.3- Write the main differences between List Comprehension and Generator Expression.
#Answer
'''
LIST COMPREHENSIONS:It allows you to create lists with a for loop and conditional statements with less code and executes immediately.
1.The comprehensions are not limited to lists.
2.You can create tuples,sets and dictionaries comprehensions as well.
GENERATOR EXPRESSION:Generator is an iterable created using a function with a yield statement.
1.is terminated whenever it encounters a return statement.
2.In a function with a yield statement the state of the function is “saved” from the last call and can be picked up the next time you call a generator function.
DIFFERENCES:
1.Parenthesis are used in generators in place of square brackets that are used in list comprehensions.
2.The generator yields one item at a time and generates item only when in demand.
3.Generator expressions are faster than list comprehension and hence time efficient.
'''

#LAMBDA & MAP
#Question.4- Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.
#Answer
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit=list(map(lambda c:((c*9)/5)+32,Celsius))
print('Temperature in Fahrenheit:',Fahrenheit)

#Question.5- Apply an anonymous function to square all the elements of a list using map and lambda.
#Answer
def square(s):
    return s*s

n=int(input('Enter Size Of List:'))
lst=[int(input()) for i in range (n)]
lst2=list(map(lambda x:square(x),lst))
print('Input List:',lst)
print('Squared List:',lst2)

#FILTER & REDUCE
#Question.6- Filter out all the primes from a list.
#Answer
def prime(num):
    if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               return False
       else:
           return True
n=int(input('Enter Size Of List:'))
lst=[int(input()) for i in range (n)]
pr=list(filter(prime,lst))
print('Input List:',lst)
print('Prime List:',pr)

#Question.7- Write a python program to multiply all the elements of a list using reduce.
#Answer
from functools import *
n=int(input('Enter Size Of List:'))
lst=[int(input()) for i in range (n)]
m=reduce(lambda x,y:x*y ,lst)
print('Input List:',lst)
print('Multiplication of all elements:',m)
