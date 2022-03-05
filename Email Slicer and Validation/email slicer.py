# Ask user to enter any email and remove any unnecessary white spaces
email = input("Enter Your Email: ").strip()

#Get the index of @
username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f"Your username is {username} & domain is {domain}")

