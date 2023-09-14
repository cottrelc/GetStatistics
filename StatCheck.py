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
    "State Check",
    style="bold red",
    subtitle="By Carson Cottrell"
    )
)



ATK = float(input("Enter Damage: "))
DEF = float(input("Enter Defence: "))
SPE = float(input("Enter Speed: "))

print(f"Your Attack is {ATK}")
print(f"Your Defense is {DEF}")
print(f"Your Speed is {SPE}")



    


