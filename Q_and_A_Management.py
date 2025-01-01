import json
def add_question(category, question_text, options, answer):
    """
    Args:
        category (str): The category to add the question to.
        question_text (str): The question text.
        options (list): A list of answer options.
        answer (int): The index of the correct answer in the options list.
    """
    try:
        with open("questions.json", "r") as file:
            questions = json.load(file) 
    except Exception as e:
        print(f"Error opening the questions file {e}")
        return
    
    # if the category doesn't exist we add it 
    if category not in questions:
        questions[category]=[]

    # we generate an id for the question by adding 1 to the max id
    ids=[item["id"] for key in questions for item in questions[key]]
    id=max(ids,default=0)+1
    print(ids)
    print(id)

 
    new_question={
        "id":id,
        "question": question_text,
        "options": options,
        "answer": answer
    }

    questions[category].append(new_question)
    print(questions)   
    
     # we added the question now we need to update in in the questions.json file
    try:
        with open("questions.json", "w") as file:
            json.dump(questions, file, indent=4)
        print(f"Question added successfully to category '{category}' with ID {id}.")
    except Exception as e:
        print(f"Error saving the updated questions file: {e}")

