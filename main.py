user_hobby = int(input("Enter numbers of your hobbies: "))
i = 0
hobby_list = []

while i < user_hobby:
    text = "Enter your hobby: " + str(i + 1) + ": "
    hobby_list.append(input(text))
    i+=1

print("Your hobbies: ", hobby_list)
