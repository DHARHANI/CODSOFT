import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    """
    Generate a random password with specified complexity.
    
    Args:
        length (int): Length of the password (default: 12)
        use_uppercase (bool): Include uppercase letters (default: True)
        use_digits (bool): Include digits (default: True)
        use_special (bool): Include special characters (default: True)
    
    Returns:
        str: Generated password
    """
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special = '!@#$%^&*()_+-=[]{}|;:,.<>?' if use_special else ''
    
    # Combine all allowed characters
    all_chars = lowercase + uppercase + digits + special
    
    # Ensure at least one character from each selected set is included
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special))
    
    # Fill the rest with random characters
    remaining_length = length - len(password)
    password.extend(random.choice(all_chars) for _ in range(remaining_length))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

def get_user_input():
    """
    Prompt user for password requirements.
    
    Returns:
        tuple: (length, use_uppercase, use_digits, use_special)
    """
    print("Password Generator")
    print("------------------")
    
    try:
        length = int(input("Enter password length (8-128): "))
        if not 8 <= length <= 128:
            print("Length must be between 8 and 128. Using default 12.")
            length = 12
    except ValueError:
        print("Invalid input. Using default length 12.")
        length = 12
    
    use_upper = input("Include uppercase letters? (Y/n): ").lower() != 'n'
    use_digits = input("Include digits? (Y/n): ").lower() != 'n'
    use_special = input("Include special characters? (Y/n): ").lower() != 'n'
    
    return (length, use_upper, use_digits, use_special)

def main():
    # Get user preferences
    length, upper, digits, special = get_user_input()
    
    # Generate password
    password = generate_password(length, upper, digits, special)
    
    # Display the password
    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()
