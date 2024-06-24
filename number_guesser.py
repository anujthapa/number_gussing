import random

user_input_count= 0

top_range =  input("Type a number: ")
if top_range.isdigit():
    top_range= int(top_range)
    if top_range <=0:
        print("Pelase type number largen than 0 Next time")
        quit()

ran_num = random.randrange(top_range)

while True:
    user_input_count = user_input_count +1
    user_answer = input("please guess number")
    if user_answer.isdigit():
        user_answer=int(user_answer)
    if user_answer != ran_num:
        print("Wrong guess, please try again")
    else:
        print(f"Yes, You gueesed it correctly in {user_input_count} Time")
        break


