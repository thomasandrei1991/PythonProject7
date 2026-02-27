def ask_question(question, choices, correct_choice, print_score):
    print(question)
    print(choices)
    correct_ans = input("Answer (A/B/C): ")
    ask_answer(correct_ans, correct_choice)
    print_score += 20
def ask_answer(correct_answer, correct_choice):
    if correct_answer ==  correct_choice:
        print("Correct!\n")
    else:
        print("Wrong!\n")


#Main Menu
print_score = 0
ask_question("Q1: What does 'len()' return?", "A) Length of object   B) Type of object   C) Memory address", "A", print_score)
ask_question("Q2: What does 'len()' return?", "A) Length of object   B) Type of object   C) Memory address", "A", print_score)
ask_question("Q3: What does 'len()' return?", "A) Length of object   B) Type of object   C) Memory address", "A", print_score)
ask_question("Q4: What does 'len()' return?", "A) Length of object   B) Type of object   C) Memory address", "A", print_score)
ask_question("Q5: What does 'len()' return?", "A) Length of object   B) Type of object   C) Memory address", "A", print_score)



#score
#total score
#percentage score
