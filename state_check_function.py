"""
    Name: state_check_function.py
    Author: Carson Cottrell
    Created: 2/22/2024
    Purpose: This file is to check states for a video game I play
"""

from rich.console import Console
from rich.panel import Panel

console = Console()
# TODO: Print creative program title
console.print(
    Panel.fit(
    "     State Calculator      ",
    style="bold red",
    subtitle="By Carson Cottrell"
    )
)

#TODO: Give choice to plus or minus number
import math
def main():
    number = float(input("Enter number here: "))
    while True:
        y = input("What would you like to do (+ or - or * or / or square or root): ")

        if y == "+":
            number = add(number)
        elif y == "-":
            number = sub(number)
        elif y == "*":
            number = times(number)
        elif y == "/":
            number = divide(number)
        elif y == "square":
            number = square(number)
        elif y =="root":
            number = root(number)
        else:
            print("Please put in a sign.")
        t = input("Would you like to do more math more (y/n): ")
        if t == "n":
            break
        elif t == "y":
            continue
        else:
            print("Please Enter y or n")

    console.print(f"[bold green]Answer[/bold green]: {number}")
#More info
    

def add(number):
    add = float(input("Enter number: "))
    number += add
    console.print(f"[bold red]Result[/bold red]: {number}")
    return number

def sub(number):
    minus = float(input("Enter number: "))
    number -= minus
    console.print(f"[bold red]Result[/bold red]: {number}")
    return number

def times(number):
    multiply = float(input("Enter number: "))
    number *= multiply
    console.print(f"[bold red]Result[/bold red]: {number}")
    return number

def divide(number):
    divide = float(input("Enter number: "))
    number /= divide
    console.print(f"[bold red]Result[/bold red]: {number}")
    return number

def square(number):
    square = int(input("How many times would you like to times it by itself: "))
    answer = number
    for i in range(square - 1):
        number= answer * number
    console.print(f"[bold red]Result[/bold red]: {number}")
    return number

def root(number):
    number = math.sqrt(number)
    console.print(f"[bold red]Result[/bold red]: {number}")
    return number
    
    
main()