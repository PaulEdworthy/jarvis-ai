def check_input(user_input):
    replacements = {
        "Jays": "Toronto Blue Jays",
        "Notre Dame": "University of Notre Dame football",
        "Oilers": "Edmonton Oilers",
        "Sens": "Ottawa Senators",
        "Celtics": "Boston Celtics",
        "Bears": "Chicago Bears",
    }

    for old, new in replacements.items():
        user_input = user_input.replace(old, new)
        # print(user_input)

    return user_input
