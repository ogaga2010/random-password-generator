import random
import string

def generate_password(length):
    # Define the possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range (length))

    return password

# Example usage
if __name__ == "__main__":
    # Ask the user for the desired password length
    length = int(input("Enter the desired password length: "))

    # Generate the password
    password = generate_password(length)

    # Print the generated password
    print(f"Generated password: {password}")