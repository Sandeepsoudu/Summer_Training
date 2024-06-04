print("Please set your login username and password:")
user = input("Set username: ")
password = input("Set password: ")
print("\nEnter username and password to login:")
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    use1 = input("Username: ")
    pass1 = input("Password: ")
    if user == use1 and password == pass1:
        print("Welcome to the account")
        break
    else:
        attempts += 1
        if attempts < max_attempts:
            print(f"Invalid username or password. Please try again. Attempt {attempts} of {max_attempts}.")
        else:
            print("Your account is blocked.")
