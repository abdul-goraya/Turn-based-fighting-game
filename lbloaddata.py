#This class deals with the activites relaeted to leaderboard
class Leaderboardloaddata:
    #takes the filename as intializer where leader board data is stored
    def __init__(self,filename) -> None:
        self.filename = filename 
        self.leaderboard=self.load_data()

    #laods the data of file
    def load_data(self):
        leaderboard=[]
        try:
            with open(self.filename, 'r') as file:
                data = file.readlines()
            for line in data:
                parts = line.split(':') #splits the data in three parts (name, password, points)
                if len(parts) == 3:
                    name, password, points = parts
                    leaderboard.append((name.strip(), int(points.strip())))
            leaderboard.sort(key=lambda x: x[1], reverse=True) #sorts leaderboard in reverse order (descending)
        except Exception as e: #Throws an error if anything happens to files
            print(f"Error reading file: {e}")
        return leaderboard
    
    #reads and retrieves the users
    def load_users(self):
        users=[]
        try:
            with open(self.filename, 'r') as file:
                data = file.readlines()
            for line in data:
                parts = line.split(':')
                if len(parts) == 3: #retreive password and username and append them in users list
                    name, password, points = parts
                    users.append((name.strip(), password.strip(),int(points.strip())))
        except Exception as e: #Throws an error if anything happens to files
            print(f"Error reading file: {e}")
        return users
    #retrieve the points of users
    def retrieve(self,username):
        for user,points in self.load_data():
            if user==username:
                return points
    #Updates the user's points and rewrites the file
    def update(self, username, reward):
        users=self.load_users()
        nlist=[]
        for user,password,points in users:
            if user==username:
                nlist.append((user,password,str(int(points)+int(reward)))) #add points
            else:
                nlist.append((user,password,points))
        try:
            with open(self.filename, 'w') as file: #writes the updates data in file
                for user, password, points in nlist:
                    file.write(f"{user} : {password} : {points}\n")
        except Exception as e:#Throws an error if anything happens to files
            print(f"Error writing to file: {e}")