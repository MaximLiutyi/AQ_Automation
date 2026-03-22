# w+ - для редагування і + для створення файлу якщо немає
# r = read
# a = append

user_data = input("Enter your name: ")
file = open('myfile.txt', 'a')
file.write(user_data)

file.close()