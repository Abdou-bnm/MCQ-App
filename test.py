from category import CategoryManager
from QuestionManager import QuestionManager

cat=CategoryManager(file_path="question1.json")

# liist=cat.read_category("databases")
# print(liist)

qm=QuestionManager(file_path="question1.json")
qm.add_question("new","hard","what is 1+2",[1,4,6,3],3)



