# Hangman
Welcome to the Hangman Game, a web-based game developed using Django for the backend and JavaScript for the frontend. In this game, players guess letters to uncover a hidden word. Each incorrect guess progressively draws a stickman figure. The player wins if they guess the word correctly before the figure is fully drawn.

Features
Django Backend: The game dynamically selects words from a list on the backend using Django.

Interactive Gameplay: A virtual keyboard is used for making guesses, and the game visually represents the progress.
Responsive Design: The game works well on desktop and mobile devices.

Dynamic Word Handling: The word for each game is selected at random from the backend.


# Getting Started
Prerequisites
Before you can run the project, make sure you have the following installed on your local machine:

Python 3.x: Download and install Python.
Django: Django is required to run the backend. Install it using pip:
pip install django


# Installation
Follow these steps to set up the project locally on your machine:
Clone the repository:

Open a terminal window and run:
`git clone https://github.com/sankalp021/Hangman.git`

Navigate to the project directory:
`cd Hangman`

Get in base directory
`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

Open the game in your browser:

Once the server is running, open your web browser and go to:

`http://127.0.0.1:8000/words/`

 # How to Play
Objective: Guess the hidden word by selecting letters. Each incorrect guess reveals part of a stickman figure. The game ends if the word is guessed or the figure is fully drawn.
Making Guesses: Click on the letters from the virtual keyboard displayed on the screen to make guesses.
Winning: Guess all the letters in the word before the stickman is fully drawn.
Losing: If the stickman is fully drawn before the word is guessed, the game is over.
