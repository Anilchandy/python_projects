
"""
This quiz program gives 3 options: Georgraphy,History and physics.User can input the choice
The questions and answers are saved as txt file .
The answers that user enters is compared with the answers text file and score is dispalyed
"""

User_input = int(input("Enter the subject you want to try ? Press 1 for Geograpy , 2 for History and 3 for Physics :"))

if User_input == 1:
    with open(r'C:\Users\Study\Python\python_Excercises\Quiz\Georgaphy.txt') as georgaphy:
        geo_question_list = []
        for question in georgaphy:
            geo_question_list.append(question)

    with open(r'C:\Users\Study\Python\python_Excercises\Quiz\Geo_Answers.txt') as geo_answer:
        geo_answer_list = []
        for answer in geo_answer:
            geo_answer_list.append(answer.lower().rstrip('\n'))
    geo_useranswer = []
    for i in range(0, 3):
        print(geo_question_list[i])
        user_answer = input("Enter the Answer :")
        geo_useranswer.append(user_answer.lower())
    score_counter = 0
    for j in range(0,3):
        if geo_useranswer[j] == geo_answer_list[j]:
            score_counter+=1
    print(f"The scrore is {score_counter} ")
elif User_input ==2:
    with open(r'C:\Users\Study\Python\python_Excercises\Quiz\History.txt') as history:
        his_question_list = []
        for question in history:
            his_question_list.append(question)

    with open(r'C:\Users\Study\Python\python_Excercises\Quiz\His_Answers.txt') as his_answer:
        his_answer_list = []
        for answer in his_answer:
            his_answer_list.append(answer.lower().rstrip('\n'))
    his_useranswer = []
    for i in range(0, 3):
        print(his_question_list[i])
        user_answer = input("Enter the Answer :")
        his_useranswer.append(user_answer.lower())
    score_counter = 0
    for j in range(0,3):
        if his_useranswer[j] == his_answer_list[j]:
            score_counter+=1
    print(f"The scrore is {score_counter} ")
else:
    with open(r'C:\Users\Study\Python\python_Excercises\Quiz\Physics.txt') as physics:
        phy_question_list = []
        for question in physics:
            phy_question_list.append(question)

    with open(r'C:\Users\Study\Python\python_Excercises\Quiz\Phy_Answers.txt') as phy_answer:
        phy_answer_list = []
        for answer in phy_answer:
            phy_answer_list.append(answer.lower().rstrip('\n'))
    phy_useranswer = []
    for i in range(0, 3):
        print(phy_question_list[i])
        user_answer = input("Enter the Answer :")
        phy_useranswer.append(user_answer.lower())
    score_counter = 0
    for j in range(0,3):
        if phy_useranswer[j] == phy_answer_list[j]:
            score_counter+=1
    print(f"The scrore is {score_counter} ")
