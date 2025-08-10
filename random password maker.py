import random
print("this is a random password maker")
print ("please fill the blanks bellow")

first_name = input('first name: ')
last_name = input('last name: ')
full_name = first_name + last_name

name_list = list(full_name)
random.shuffle(name_list)

shuffle_name = ''.join(name_list)
random_number = random.randint(1000, 9999)

final_password = shuffle_name + str(random_number)

print ('your password is: ', final_password)
print('have a nice day! <3')


