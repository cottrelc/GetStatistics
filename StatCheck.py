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
        print("Say a number here: ")
        self.user_input()

        self.number()

        while True:
            print("What would you like to do (plus or minus or times or divide or square or root): ")

            self.user_input()

            if self.query == "Plus":
                add = float(input("Enter number: "))
                self.numb += add
                console.print(f"[bold red]Result[/bold red]: {self.numb}")
            elif self.query == "Minus":
                minus = float(input("Enter number: "))
                self.numb -= minus
                console.print(f"[bold red]Result[/bold red]: {self.numb}")
            elif self.query == "Times":
                multiply = float(input("Enter number: "))
                self.numb *= multiply
                console.print(f"[bold red]Result[/bold red]: {self.numb}")
            elif self.query == "Divide":
                divide = float(input("Enter number: "))
                self.numb /= divide
                console.print(f"[bold red]Result[/bold red]: {self.numb}")
            elif self.query == "Square":
                square = int(input("How many times would you like to times it by itself: "))
                answer = self.numb
                for i in range(square - 1):
                    self.numb= answer * number
                console.print(f"[bold red]Result[/bold red]: {self.numb}")
            elif self.query =="Root":
                self.numb = math.sqrt(self.numb)
                console.print(f"[bold red]Result[/bold red]: {self.numb}")
            else:
                print("Please put in a sign.")
            t = input("Would you like to do more math more (y/n): ")
            if t == "n":
                break
            elif t == "y":
                continue
            else:
                print("Please Enter y or n")

        console.print(f"[bold green]Answer[/bold green]: {self.numb}")

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
                self.user_input()

            except sr.RequestError as e:
                print(f"Google Speech did not respond: {e}")


    def number(self):

        if self.query == "one":
            self.numb = 1
        elif self.query == "two":
            self.numb = 2
        elif self.query == "three":
            self.numb = 3
        elif self.query == "four":
            self.numb = 4
        elif self.query == "five":
            self.numb = 5
        elif self.query == "six":
            self.numb = 6
        elif self.query == "seven":
            self.numb = 7
        elif self.query == "eight":
            self.numb = 8
        elif self.query == "nine":
            self.numb = 9
        else:
            int: self.numb = self.query
#More info
    

ma = math()
ma.main()



    


