#Project Description
"""
Magic 8-Ball
The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.
Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.
"""
import random 

answers = [
  "Yes - definitely", "It is decidedly s", "Without a doubt",
  "Reply hazy, try again", "Ask again later", "Better not tell you now",
  "My sources say no", "Outlook not so good", "Very doubtful",
]

name = "WashiWash"
question = "Will I finish this project?"
random_number = random.choice(answers)
print (str(random_number))