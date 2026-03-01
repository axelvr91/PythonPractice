
#Define a function that takes as parameter a list that
#contains decimal numbers as strings and returns
#the sum of those numbers.

def foo(lst):
    return sum(float(i) for i in lst)