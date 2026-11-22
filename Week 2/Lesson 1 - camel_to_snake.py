# Week 2 - Lesson 1: camelCase to snake_case Converter
# 
# Goal:
# Take user input in camelCase (e.g., 'preferredFirstName')
# and convert it to snake_case (e.g., 'preferred_first_name').
#
# Hint:
# 1. Loop through each character in the string.
# 2. If the character is uppercase (char.isupper()):
#      add an underscore '_' and the lowercase version of the char.
#    Otherwise:
#      just add the character as it is.

def main():
    
    camel_word= input("camelCase: ")

    snake_word = ""
    for c in camel_word:
        if c.isupper():
            snake_word += "_" + c.lower()
        else:
            snake_word += c
    print(f"snake_case: {snake_word}")

if  __name__ == "__main__":
    main()


