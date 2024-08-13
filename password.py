import re

def check_password_strength(password):
    strength = 0
    feedback = []
    
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")
    
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")
    
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")
    
    if strength == 5:
        feedback.append("Password strength: Very Strong 💪")
    elif strength == 4:
        feedback.append("Password strength: Strong 👍")
    elif strength == 3:
        feedback.append("Password strength: Moderate 👌")
    else:
        feedback.append("Password strength: Weak ⚠️")
    
    return "\n".join(feedback)

def main():
    while True:
        password = input("Enter your password to check its strength: ")
        result = check_password_strength(password)
        print(result)
        
        again = input("Would you like to check another password? (yes/no): ").lower()
        if again != 'yes':
            print("Exiting the program. Stay secure! 🔐")
            break

if __name__ == "__main__":
    main()
