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

# this function will be used to load a question by its id (we will use it after getting the id of a question the user hasn't already solved) and it will return true (if he chose the correct answer ) or false
def load_question(id):
   try:
        with open("questions.json", "r") as file:
            questions = json.load(file)
        
        #search for the question by ID
        for category, question_list in questions.items():
            for question in question_list:
                if question["id"] == id:
                    # we found the question now we print it , and its options
                    print(f"Question: {question['question']}")
                    print("Options:")
                    for idx, option in enumerate(question["options"], 1):
                        print(f"{idx}. {option}")
                    # now we ask for the user's input(answer)
                    while True:
                        try:
                            user_answer = int(input("Enter the number of your answer: "))
                            if 1 <= user_answer <= len(question["options"]):
                                break
                        except ValueError:
                            print("Invalid input. Please enter a number.")

                    if user_answer==question["answer"]+1:
                        return True
                    else:
                        return False
                        
        # we haven't found the qst
        print(f"Question with ID {id} not found.")
                

   except Exception as e:
       print(f"Error loading the questions file: {e}")
       return -1


#returns the selected category as a string
def select_category():
    try:
        with open("questions.json", "r") as file:
            questions = json.load(file) 
    except Exception as e:
        print(f"Error opening the questions file {e}")
        return
    
    print("Available categories:")
    categories = list(questions.keys())
    for idx, category in enumerate(categories, 1):
        print(f"{idx}. {category}")
    
    # we get the user's choice
    while True:
        try:
            user_choice = int(input("Select a category (enter the number): "))
            if 1 <= user_choice <= len(categories):
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    selected_category = categories[user_choice - 1]
    return selected_category
    


   
#print(load_question(1))
print(select_category())

