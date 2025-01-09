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
        
        # we added the question now we need to update in in the questions.json file
        self.categorymanager._save_data(questions);

        