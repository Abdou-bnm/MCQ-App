from category import CategoryManager
from QuestionManager import QuestionManager

cat=CategoryManager(file_path="question1.json")



qm=QuestionManager(file_path="question1.json")
new_quest=qm.add_question("new","easy","what is 1+2",[1,4,6,3],2)
qm.load_question(new_quest)
qm.edit_question(new_quest,new_correct=3)
qm.load_question(new_quest)
qm.delete_question(new_quest)
qm.load_question(new_quest)




