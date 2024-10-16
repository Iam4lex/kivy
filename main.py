<<<<<<< HEAD
import random
import os
import sys

def guess_number_game():
    # Set the range for guessing
    number_to_guess = random.randint(1, 10)
    attempts = 3  # Player gets 3 attempts
    
    print("Welcome to the Guessing Game!")
    print("You need to guess a number between 1 and 10.")
    
    # Loop through the number of attempts
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts}: What's your guess? "))
            
            if guess == number_to_guess:
                print("Congratulations! You've guessed the correct number!")
                return
            
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print("Too low!")
        
        except ValueError:
            print("Please enter a valid number.")
    
    # If the player runs out of attempts, they lose
    print("Sorry, you lost! The correct number was:", number_to_guess)
    simulate_os_removal()

def simulate_os_removal():
    print("Oh no! You lost the game...")
    print("The OS is being removed... just kidding! 😅")
    
    # Simulate some "OS removal" drama
    for i in range(5, 0, -1):
        print(f"Removing OS in {i} seconds...")
        sys.stdout.flush()
        # time.sleep(1)  # Pause for dramatic effect
    
    print("Your OS is safe! This was just a game after all. Play again?")
    
if __name__ == "__main__":
    guess_number_game()
=======
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        #returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # image widget
        self.window.add_widget(Image(source="logo.png"))

        # label widget
        self.greeting = Label(
                        text= "Please enter your username to login",
                        font_size= 18,
                        color= '#00FFCE'
                        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
                    multiline= False,
                    padding_y= (20,20),
                    size_hint= (1, 0.5)
                    )

        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
                      text= "Login",
                      size_hint= (1,0.5),
                      bold= True,
                      background_color ='#00FFCE',
                      #remove darker overlay of background colour
                      # background_normal = ""
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        # change label text to "Hello + user name!"
        self.greeting.text = "Welcome " + self.user.text + "!"

# run Say Hello App Calss
if __name__ == "__main__":
    SayHello().run()
>>>>>>> 0d9f42133ab8e186f7146227e2e82be81e0ef701
