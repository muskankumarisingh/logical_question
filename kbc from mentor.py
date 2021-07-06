question_list = [
    "How many continents are there?",   
    "What is the capital of India?",    
    "NG mei kaun se course padhaya jaata hai?"   
]

options_list = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
solution_list = [3, 4, 1] 
help_list=[[3,4],[1,4],[1,2]]
i=0
life_line=0
while i<len(question_list):
    print("Your question is")
    print()
    print(question_list[i])
    j=0
    print("your options are")
    while j<len(options_list[i]):
        print(j+1,options_list[i][j])
        j=j+1
    solution=(input("enter the answer/life_line"))
    if solution=="life_line":
        if life_line==0:
            print(help_list[i])
            life_line=life_line+1
            check=int(input("enter the right answer"))
            if check==solution_list[i]:
                print("congrats,your answer is correct")
            else:
                print("sadly,your answer is wrong")
                break
        else:
            print("you already used lifeline")
            user=int(input("enter your answer"))
            if user==solution_list[i]:
                print("congrats,your answer is correct")
            else:
                print("sadly,your answer is wrong")
                break
    elif int(solution)==solution_list[i]:
        print("congrats,your answer is correct")
    else:
        print("sadly your answer is wrong")
        break
    
    i=i+1