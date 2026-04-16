users = {}

def create_user(email):
    if email in users:
        return "User already exists"
    users[email] = {"password": "default123", "license": False}
    return "User created"

def reset_password(email):
    if email not in users:
        return "User not found"
    users[email]["password"] = "newpassword123"
    return "Password reset"

def assign_license(email):
    if email not in users:
        return "User not found"
    users[email]["license"] = True
    return "License assigned"