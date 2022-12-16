from random import randint

def generate_password():
  uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  letters_and_numbers = [lowercase_letters, uppercase_letters, numbers]
  password = ''

  uppercase_letters_size = int(input('How many uppercase letters would you like in your password? '))
  lowercase_letters_size = int(input('How many lowercase letters would you like in your password? '))
  numbers_size = int(input('How many numbers would you like in your password? '))

  for number in range(0, numbers_size+uppercase_letters_size+lowercase_letters_size):
    letters_and_numbers_at_position = randint(0, 2)
    maximum_position = 0
    if letters_and_numbers_at_position == 0: maximum_position = 25
    elif letters_and_numbers_at_position == 1: maximum_position = 25
    elif letters_and_numbers_at_position == 2: maximum_position = 9

    password += str(letters_and_numbers[letters_and_numbers_at_position][randint(0, maximum_position)])
    
  return password

print(generate_password())