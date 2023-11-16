"""
    Name: state_check.py
    Author: Carson Cottrell
    Created: 9/14/2023
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
number = float(input("Enter number here: "))
while True:
    y = input("What would you like to do (+ or - or * or / or square): ")

    if y == "+":
        add = float(input("Enter number: "))
        number += add
        console.print(f"[bold red]Result[/bold red]: {number}")
    elif y == "-":
        minus = float(input("Enter number: "))
        number -= minus
        console.print(f"[bold red]Result[/bold red]: {number}")
    elif y == "*":
        multiply = float(input("Enter number: "))
        number *= multiply
        console.print(f"[bold red]Result[/bold red]: {number}")
    elif y == "/":
        divide = float(input("Enter number: "))
        number /= divide
        console.print(f"[bold red]Result[/bold red]: {number}")
    elif y == "square":
        square = int(input("How many times would you like to times it by itself: "))
        answer = number
        for i in range(square - 1):
            number= answer * number
        console.print(f"[bold red]Result[/bold red]: {number}")
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


    


