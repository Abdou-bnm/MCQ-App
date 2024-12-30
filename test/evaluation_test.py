import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # needed to import evaluation_system
from evaluation_system import EvaluationSystem

if not os.path.exists('data'):
    os.makedirs('data')
    
    
if not os.path.exists('data/users.json'):
    users_data = {
        "darkoo": {
            "password": "darkoo",
            "history": []
        },
        "abdou": {
            "password": "abdou",
            "history": []
        }
    }
    
    with open('data/users.json', 'w') as f:
        json.dump(users_data, f, indent=4)
    

# Load users data
with open('data/users.json', 'r') as f:
    users_data = json.load(f)
    
user_id = "darkoo"  

if user_id not in users_data:
    print(f"Error: User ID '{user_id}' not found!")
    exit()



if not os.path.exists('data/questions.json'):
    questions_data = {
        "Python_Basics": [
            {
                "question": "What is Python?",
                "options": ["A snake", "A programming language", "A video game", "A movie"],
                "answer": 1
            },
            {
                "question": "Which symbol is used for comments in Python?",
                "options": ["//", "#", "/*", "$$"],
                "answer": 1
            },
            {
                "question": "What is the correct file extension for Python files?",
                "options": [".py", ".python", ".pt", ".pyt"],
                "answer": 0
            }
        ]
    }
    
    with open('data/questions.json', 'w') as f:
        json.dump(questions_data, f, indent=4)


# Load the questions data
with open('data/questions.json', 'r') as f:
    questions_data = json.load(f)
    
    
evaluator = EvaluationSystem()

print("MCQ Test Starting...")
print("-" * 50)


category = "Python_Basics"
questions = questions_data[category]


for i, q in enumerate(questions, 1):
    print(f"\nQuestion {i}: {q['question']}")
    for j, option in enumerate(q['options']):
        print(f"{j}. {option}")
        
    # for simulation 
    user_answer = q['options'][q['answer']] if i % 2 == 0 else q['options'][0]
    
    is_correct = evaluator.evaluate_answer(
        q['question'],
        user_answer,
        q['options'][q['answer']]
    )
    
    print(f"Your answer: {user_answer}")
    print(f"Correct? {'✓' if is_correct else '✗'}")
    
    
final_score = evaluator.calculate_final_score(len(questions))

print("\n" + "=" * 50)
print("Test Results:")
print(f"Score: {final_score['raw_score']}/{final_score['total_questions']}")
print(f"Percentage: {final_score['percentage']}%")

print("\nDetailed Feedback:")
print(evaluator.generate_feedback_summary())


# Update user history
evaluator.update_user_history(user_id, final_score)

# Export results
result_file = evaluator.export_results(user_id, category, final_score)
print(f"\nResults exported to: {result_file}")
