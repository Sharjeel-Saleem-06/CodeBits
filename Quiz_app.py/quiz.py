questions=[
        {"question":"Who is the founder of Pakistan?","answer":"Muhammad Ali Jinnah"},
        {"question":"who is the founder of this proram?", "answer":"Sharjeel"}
          ]



def quiz():
    correc_answers=0

    for i in questions:
        answers=input(i["question"])
        if answers.lower().strip()==i["answer"].lower():
            correc_answers+=1
        
    total_questios=len(questions)    
    percentage=(correc_answers/total_questios)*100


    print(f"Out of {total_questios} questions you successfully solved {correc_answers}")
    print(f"Your percentage is {percentage}%")


if __name__=="__main__":
    quiz()



