import json
import os


data_file = 'data/users.json'
questions_file = 'data/questions.json'

if not os.path.exists('data'):
    os.makedirs('data')

if not os.path.exists(data_file):
    with open(data_file, 'w') as f:
        json.dump({}, f)

if not os.path.exists(questions_file):
    with open(questions_file, 'w') as f:
        json.dump({}, f)

# Utility functions
def load_users():
    with open(data_file, 'r') as file:
        return json.load(file)

def save_users(users):
    with open(data_file, 'w') as file:
        json.dump(users, file, indent=4)

def load_questions():
    with open(questions_file, 'r') as file:
        return json.load(file)

def save_questions(questions):
    with open(questions_file, 'w') as file:
        json.dump(questions, file, indent=4)
