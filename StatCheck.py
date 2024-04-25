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
            self.org = self.numb
            self.user_input()

            if self.query == "Plus" or self.query == "plus":
                print("Say a number here: ")
                self.user_input()

                self.number()
                self.org += self.numb
                console.print(f"[bold red]Result[/bold red]: {self.org}")
            elif self.query == "Minus" or self.query == "minus":
                print("Say a number here: ")
                self.user_input()

                self.number()
                self.org -= self.numb
                console.print(f"[bold red]Result[/bold red]: {self.org}")
            elif self.query == "Times" or self.query == "times":
                print("Say a number here: ")
                self.user_input()

                self.number()
                self.org *= self.numb
                console.print(f"[bold red]Result[/bold red]: {self.org}")
            elif self.query == "Divide" or self.query == "divide":
                print("Say a number here: ")
                self.user_input()

                self.number()
                self.org /= self.numb
                console.print(f"[bold red]Result[/bold red]: {self.org}")
            elif self.query == "Square" or self.query == "square":
                print("Say a number here: ")
                self.user_input()

                self.number()
                print("How many times would you like to times it by itself: ")
                square = self.numb
                answer = self.org
                for i in range(square - 1):
                    self.org= answer * self.org
                console.print(f"[bold red]Result[/bold red]: {self.org}")
            elif self.query =="Root" or self.query == "root---------":
                self.org = math.sqrt(self.org)
                console.print(f"[bold red]Result[/bold red]: {self.org}")
            else:
                print("Please put in a sign.")
            t = input("Would you like to do more math more (y/n): ")
            if t == "n":
                break
            elif t == "y":
                continue
            else:
                print("Please Enter y or n")

        console.print(f"[bold green]Answer[/bold green]: {self.org}")

    def user_input(self):


        with sr.Microphone() as source:
            print('Listening....')

            audio = self.r.listen(source)

            try:
                print('Recognizing . . .')

                self.recognized_words = self.r.recognize_google(
                    audio,
                    language='en-US',
                    show_all=True
                )

                self.query = self.recognized_words['alternative'][0]['transcript']
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
            try:
                float(self.query)
                self.numb = self.query
            except ValueError:
                print("wrong value")
#More info
    

ma = math()
ma.main()



    


