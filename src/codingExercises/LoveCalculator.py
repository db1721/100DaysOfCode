while True:
    name1 = str(input("What is your full name? "))
    name2 = str(input("What is your love's full name? "))

    percentage1 = 0 # TRUE
    percentage2 = 0 # LOVE
    combined_names = name1 + name2

    for letter1 in 'true':
        percentage1 += combined_names.lower().count(letter1)
    for letter2 in 'love':
        percentage2 += combined_names.lower().count(letter2)

    love_score = int(f"{percentage1}{percentage2}")
    if love_score < 10 or love_score > 90:
        print(f"Your score is {love_score}%. You go together like coke and mentos")
    elif 40 <= love_score <= 50:
        print(f"Your score is {love_score}%, you are alright together")
    else:
        print(f"Your score is {love_score}%")
