#Imported os (to find text file) and other file to use their functions
import os
import lbloaddata

#takes username and password as initallizer
def signup(username, password):
    if not os.path.exists('users.txt'): #checks if file does not exist so it can create file
        with open('users.txt', 'w') as file:
            pass
    with open('users.txt', 'r') as file:
        content = file.read()
        if username == "" or password == "": #if user enters no info
            return "Empty Parameters"
        elif f"{username} :" in content: #checks if already user exits or not
            return "Username already exists"
    with open('users.txt', 'a') as file: 
        file.write("\n")
        file.write(f"{username} : {password} : 0")#if username is unique data is entered with intial points zero
    return "User registered successfully"
#checks login detials and work accordingly
def login(username, password):
    try:
        with open('users.txt', 'r') as file:
            content = file.read()
            if f"{username} : {password} :" in content: #checks if username and password is correct
                users = lbloaddata.Leaderboardloaddata('users.txt')
                points = users.retrieve(username)
                return ["Logged in successfully",points]
            elif username== "" or password == "": #check if user enter no info
                return ["Empty Paramters", "False"]
            else:
                return ["Wrong details", "False"]
    except FileNotFoundError: #throws error if file is not found
        return "No users found. Please signup first."