def parse_task(user_input):
    email = user_input.split()[-1]

    if "create" in user_input and "assign" in user_input:
        return {"action": "create_and_assign", "email": email}

    elif "create" in user_input:
        return {"action": "create_user", "email": email}

    elif "reset" in user_input:
        return {"action": "reset_password", "email": email}

    elif "assign" in user_input:
        return {"action": "assign_license", "email": email}