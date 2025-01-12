import json
from category import CategoryManager
class QuestionManager:
    def __init__(self, file_path):
        self.file_path=file_path
        ## since we already have methods we need implemented in categorymanager we can use them

        self.categorymanager=CategoryManager(file_path=self.file_path)

    def add_question(self,category,level,question_text, options, answer):

        # Args:
        #     category (str): The category to add the question to.
        #     question_text (str): The question text.
        #     options (list): A list of answer options.
        #     answer (int): The index of the correct answer in the options list.

        # if the category doesn't exist we add it 
        result=self.categorymanager.create_category(name=category)

        #then we load the data to add the question
        questions=self.categorymanager._load_data()



        # we generate an id for the question by adding 1 to the max id
        ids=[q["id"] for cat in questions["categories"] for lvl in cat["levels"] for q in lvl["questions"]]
        id=max(ids,default=0)+1
        print(ids)
        print(id)

        # we load the category
        cat=self.categorymanager.read_category(name=category)

        #we load the level
        level_obj = next((lvl for lvl in cat["levels"] if lvl["level"] == level), None)

        print(level_obj)

    
        new_question={
            "id":id,
            "question": question_text,
            "options": options,
            "correct": answer
        }

        level_obj["questions"].append(new_question)

         # Update the original data with the modified category
        for cat_entry in questions["categories"]:
            if cat_entry["name"] == category:
                for lvl in cat_entry["levels"]:
                    if lvl["level"] == level:
                        lvl["questions"] = level_obj["questions"]
                        break  
        
        # we added the question now we need to update in in the questions_1.json file
        self.categorymanager._save_data(questions)
        print("question added succesfully")
        return id

    def load_question(self,id):
        data=self.categorymanager._load_data()

        question = False
        for category in data["categories"]:
            for level in category["levels"]:
                for q in level["questions"]:
                    if q["id"] == id:
                        print(f"Question found: {question}")
                        question=q
                        break
        
        if question:
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

                    if user_answer==question["correct"]+1:
                        print("correct answer")
                        return True
                    else:
                        print("wrong answer")
                        return False
                    
        # we haven't found the qst
        print(f"Question with ID {id} not found.")

    def edit_question(self, id, new_question_text=None, new_options=None, new_correct=None):
        """
        Edit an existing question by its unique ID.

        Args:
            id (int): The unique ID of the question to edit.
            new_question_text (str): The new question text (optional).
            new_options (list): The new list of options (optional).
            new_correct (int): The new correct option index (optional).

        Returns:
            None
        """
        data = self.categorymanager._load_data()
        question_found = False

        # Iterate through categories, levels, and questions to find the question by ID
        for category in data["categories"]:
            for level in category["levels"]:
                for question in level["questions"]:
                    if question["id"] == id:
                        question_found = True
                        # Update the question fields if provided
                        if new_question_text:
                            question["question"] = new_question_text
                        if new_options:
                            question["options"] = new_options
                        if new_correct is not None:
                            if 0 <= new_correct < len(question["options"]):
                                question["correct"] = new_correct
                            else:
                                print("Error: New correct answer index is out of range.")
                                return

                        print(f"Question with ID {id} updated successfully.")
                        self.categorymanager._save_data(data)
                        return

        if not question_found:
            print(f"Question with ID {id} not found.")

    def delete_question(self, id):
        """
        Delete a question by its unique ID.

        Args:
            id (int): The unique ID of the question to delete.

        Returns:
            None
        """
        data = self.categorymanager._load_data()
        question_found = False

        # Iterate through categories and levels to find and delete the question
        for category in data["categories"]:
            for level in category["levels"]:
                for question in level["questions"]:
                    if question["id"] == id:
                        level["questions"].remove(question)
                        question_found = True
                        print(f"Question with ID {id} deleted successfully.")
                        self.categorymanager._save_data(data)
                        return

        if not question_found:
            print(f"Question with ID {id} not found.")