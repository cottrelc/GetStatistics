"""
    Name: state_check.py
    Author: Carson Cottrell
    Created: 9/14/2023
    Purpose: This file is to check states for a video game I play
"""

from rich.console import Console
from rich.panel import Panel
import math
import speech_recognition as sr

from sys import exit

import pyttsx3

import wikipedia

console = Console()
# TODO: Print creative program title
console.print(
    Panel.fit(
    "     State Calculator      ",
    style="bold red",
    subtitle="By Carson Cottrell"
    )
)
class math:
#TODO: Give choice to plus or minus number
    

    def __init__(self) -> None:

        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()

    def main(self):
        number = float(input("Enter number here: "))
        while True:
            print("What would you like to do (plus or minus or times or divide or square or root): ")

            self.user_input()

            if self.query == "plus":
                add = float(input("Enter number: "))
                number += add
                console.print(f"[bold red]Result[/bold red]: {number}")
            elif self.query == "minus":
                minus = float(input("Enter number: "))
                number -= minus
                console.print(f"[bold red]Result[/bold red]: {number}")
            elif self.query == "times":
                multiply = float(input("Enter number: "))
                number *= multiply
                console.print(f"[bold red]Result[/bold red]: {number}")
            elif self.query == "divide":
                divide = float(input("Enter number: "))
                number /= divide
                console.print(f"[bold red]Result[/bold red]: {number}")
            elif self.query == "square":
                square = int(input("How many times would you like to times it by itself: "))
                answer = number
                for i in range(square - 1):
                    number= answer * number
                console.print(f"[bold red]Result[/bold red]: {number}")
            elif self.query =="root":
                number = math.sqrt(number)
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

    def user_input(self):


        with sr.Microphone() as source:
            print('Listening....')

            audio = self.r.listen(source)

            try:
                print('Recognizing . . .')

                recognized_words = self.r.recognize_google(
                    audio,
                    language='en-US',
                    show_all=True
                )

                self.query = recognized_words['alternative'][0]['transcript']
                print(self.query)
                self.engine.say(self.query)
                self.engine.runAndWait()
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")

            except sr.RequestError as e:
                print(f"Google Speech did not respond: {e}")
#More info
    

ma = math()
ma.main()



    


