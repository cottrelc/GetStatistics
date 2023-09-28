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

number = float(input("Enter number here: "))
while True:
    y = input("What would you like to do (+ or -): ")

    if y == "+":
        add = float(input("Enter number: "))
        number += add
    elif y == "-":
        minus = float(input("Enter number: "))
        number -= minus
    else:
        print("Please put in a sign.")
    t = input("Would you like to add or subtract more (y/n): ")
    if t == "n":
        break
    elif t == "y":
        continue
    else:
        print("Please Enter y or n")

print(f"Answer: {number}")



    


