
# ❗ WARNING: This is a simulation. Never store passwords like this in real projects!

USERNAME = "admin"
PASSWORD = "Password"

def authenticate(input_user, input_pass):
    if input_user == USERNAME and input_pass == PASSWORD:
        return "Login successful!"
    else:
        return "Invalid credentials."
    
# Simulate login

user = input("Enter username: ")
pw = input("Enter password: ")

print(authenticate(user, pw))
