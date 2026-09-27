"""
Module 2 — Lesson 4: Functions
Student: Bundalian, Clarence James L.
Date: 09/27/2026

[A function is a block of code that does one job.
Instead of writing the same code many times, we
write it once and call it whenever we need it.
Functions can receive input using parameters and
send back a result using return.]

- function: a reusable block of code
- parameter: input a function receives
- argument: the value passed into a function
- return: sends a result back
- def: keyword used to create a function
"""
def calculate_total(price, quantity):
    total = price * quantity
    return total

bill = calculate_total(45, 3)
print("Total:", bill)

"""
I forgot to use the return keyword. The function
ran, but I could not save the answer in a variable.
"""