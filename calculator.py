num_a = int(input('Pick a number '))
operand = input ('Select an operand ')
num_b = int(input('Pick a number '))
def add(a,b):
      if operand == '+':
            print(a+b)
sum_both = add(num_a,num_b)
def subtract(a,b):
      if operand == '-':
            print (a-b)
sub_both = subtract(num_a,num_b)
def multiply(a,b):
      if operand == '*':
            print (a*b)
mult_both = multiply(num_a,num_b)
def divide(a,b):
      if operand == '/':
            print (a/b)
div_both = divide(num_a,num_b)



