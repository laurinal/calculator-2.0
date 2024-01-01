# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 22:38:13 2024

@author: iyino
"""

import math 
class Calculator:
    def __init__(self):
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }
        
    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if x == 0 or y == 0:
            print('Cannot divide a number by 0')
            raise ValueError #used this to handles errors that may arise during run time
        else:
            return x / y
        
    def get_user_input(self):
        try:
            x = float(input("Enter the first number (x): "))
            y = float(input("Enter the second number (y): "))
            return x, y
        except (ValueError, TypeError) as e: #used this to handles errors that may arise during run time
            if isinstance(e, ValueError):
                print(f"ValueError: {e}\nInvalid input. Please enter valid numeric values.")
                # Handle TypeError
            elif isinstance(e, TypeError):
                print(f"TypeError: {e}")
                # Handle other exceptions if needed
            else:
                print(f"An unexpected error occurred: {e}")
            
    def add_operation(self, operation_symbol, operation_function):
        self.operations[operation_symbol] = operation_function
        
    
    def calculate(self, x, operation_symbol, y):
        try:
            if operation_symbol in self.operations:
                if operation_symbol == 'log':
                    return self.logarithm(x,y)
                elif operation_symbol == 'sqrt':
                    return self.square_root(x)
                elif operation_symbol == '^':
                    return self.exponentiation(x,y)
                elif isinstance(x, (int, float)) and isinstance(y, (int, float)):
                    return self.operations[operation_symbol](x, y) 
                else:
                    raise ValueError('Invalid input \nPlease enter a real number')
            else:
                 raise ValueError("Please enter any of the operations; '+', '-', '*', '/':\n")
        except ValueError as e:
            print(f"Error: {e}")
            return None 
    
    def exponentiation(self, x, y=None):
        return f'{x} raised to the power {y} is {x**y}'
                 
    def square_root(self, x):
        return f'The square root of {x} is {math.sqrt(x)}'
                 
    def logarithm(self, x, y):
        if x > 0 and y > 0:
            return f'Logarithm of {x} with base {y} is {math.log(x, y)}'
        else:
            print('Invalid input for logarithm. Both x and y must be greater than 0')
            return None

            
calc_obj = Calculator()

while True:
    x, y = calc_obj.get_user_input()
    operation_symbol = input("Enter the operation: ")
    try:
        if operation_symbol.lower() in ['^', 'sqrt', 'log']:
            calc_obj.add_operation('^', Calculator.exponentiation)
            calc_obj.add_operation('sqrt', Calculator.square_root)
            calc_obj.add_operation('log', Calculator.logarithm)
        result = calc_obj.calculate(x, operation_symbol, y)
    except TypeError as e:
        print('PLEASE INPUT A VALID OPERATION')
    if result is not None:
        print(f'The result is: {result}')

    # Add an option to exit the loop
    exit_choice = input("Do you want to continue? (yes/no): ")
    if exit_choice.lower() != 'yes':
        break  