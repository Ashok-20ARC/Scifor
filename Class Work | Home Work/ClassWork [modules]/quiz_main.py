from quiz_questions import questions,options,answers

def start_quiz():
    score=0
    for i in range(len(questions)):
        print(f"Q{i+1}: {questions[i]}")
        for option in options[i]:
            print(option)
        user_ans=int(input("Enter you choice (1-4): "))
        
        if user_ans==answers[i]:
            print("Correct!")
            score+=1
        else:
            print("Wrong!")
            
        print()
    print(f"Your final score is {score}/{len(questions)}.")
            
print("Welcome to the Quiz Program!")
print("Answer the following questions by selecting the correct option.")
print()

start_quiz()