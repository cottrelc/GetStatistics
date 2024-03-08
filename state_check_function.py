"""
    Name: state_check_function.py
    Author: Carson Cottrell
    Created: 2/22/2024
    Purpose: This file is to check states for a video game I play
"""

from rich.console import Console
from rich.panel import Panel

import pyttsx3
import math


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


    #More info
# this right here is the class with all the information for the calculations
class calculate():

    def __init__(self):
        # The init holds the ability for the computer to speak to you
        self.engine = pyttsx3.init()       

    def add(self, number):
        add = float(input("Enter number: "))
        number += add
        console.print(f"[bold red]Result[/bold red]: {number}")
        # Right here I have the system say what the number you got was.
        self.engine.say(number)
        self.engine.runAndWait()
        return number

    def sub(self, number):
        minus = float(input("Enter number: "))
        number -= minus
        console.print(f"[bold red]Result[/bold red]: {number}")
        self.engine.say(number)
        self.engine.runAndWait()
        return number

    def times(self, number):
        multiply = float(input("Enter number: "))
        number *= multiply
        console.print(f"[bold red]Result[/bold red]: {number}")
        self.engine.say(number)
        self.engine.runAndWait()
        return number

    def divide(self, number):
        divide = float(input("Enter number: "))
        number /= divide
        console.print(f"[bold red]Result[/bold red]: {number}")
        self.engine.say(number)
        self.engine.runAndWait()
        return number

    def square(self, number):
        square = int(input("How many times would you like to times it by itself: "))
        answer = number
        for i in range(square - 1):
            number= answer * number
        console.print(f"[bold red]Result[/bold red]: {number}")
        self.engine.say(number)
        self.engine.runAndWait()
        return number

    def root(self, number):
        number = math.sqrt(number)
        console.print(f"[bold red]Result[/bold red]: {number}")
        self.engine.say(number)
        self.engine.runAndWait()
        return number

def main():
    cal = calculate()
        
    number = float(input("Enter number here: "))
    while True:
        y = input("What would you like to do (+ or - or * or / or square or root): ")

        if y == "+":
            number = cal.add(number)
        elif y == "-":
            number = cal.sub(number)
        elif y == "*":
                number = cal.times(number)
        elif y == "/":
                number = cal.divide(number)
        elif y == "square":
            number = cal.square(number)
        elif y =="root":
                number = cal.root(number)
        else:
            print("Please put in a sign.")
        t = input("Would you like to do more math more (y/n): ")
        if t == "n":
            break
        elif t == "y":
            continue
        else:
            print("Please Enter y or n")
    
    
main()