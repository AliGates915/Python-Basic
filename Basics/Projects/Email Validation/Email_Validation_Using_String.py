email = input("Enter Your Email : ")  # Example: g@gmail.com
k, d = 0, 0

if len(email) > 6:
    if email[0].isalpha():
        if "@" in email and email.count("@") == 1:
            domain = email.split("@")[-1]  # Extract the domain part
            if domain.endswith("gmail.com"):  # Check if the domain is "gmail.com"
                if email[-4] == "." or email[-3] == ".":  # Correct dot position check
                    for i in email:
                        if i.isspace():  # Fixed space check
                            k = 1
                        elif not i.isalnum() and i not in {"_", ".", "@"}:
                            d = 1

                    if k == 1 or d == 1:
                        print("Wrong Email Format ❌")
                    elif ".." in email or ".@" in email or "_@" in email:
                        print("Invalid Special Character Placement ❌")
                    else:
                        print("Right Email 😊")
                else:
                    print("Email must have '.' at the correct position ❌")
            else:
                print("Email must be a Gmail address (e.g., example@gmail.com) ❌")
        else:
            print("Email must include '@' exactly once ❌")
    else:
        print("First character must be an alphabet ❌")
else:
    print("Email is too short ❌")


# Dry Run the code through the ChatGPT url
# https://chatgpt.com/c/67cf14b5-0fbc-8012-8e84-93bc7e0aae8e