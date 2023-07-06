import random 

def generate_password():
    letters = "qwertyuiopasdfghjklzxcvbnm"
    result = ""
    for i in range(8):
        random_letter = random.choice(letters)
        result += random_letter
    print(result)
generate_password()