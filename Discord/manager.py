class Manager:
    # Initialize Manager:
    def __init__(self):
        self.users = {}

    # Initialize Database:
    def dump(self):
        try:
            with open("accounts.txt", "r") as fl:
                tmp_data = fl.read().split("\n")
                fl.close()
            for p in tmp_data:
                #print(p)
                if p.split(":")[0] in self.users.keys():
                        if self.users[p.split(":")[0]] == p.split(":")[1]
                            print("This record is already in the database: {0}".format(p))
                        else:
                            self.users[p.split(":")[0]].update(self.users[p.split(":")[0]] + "," + p.split(":")[1]
                else:
                    try:
                        user = p.split(":")[0].lower()
                        passwd = p.split(":")[1]
                        self.users.update({user:passwd})
                    except Exception as error:
                        print(error)
                        print("Error in {0}".format(p))
                        continue
            print("Database updated.")
        except Exception as error:
            print("An error has occurred!")
            print(error)

    # Get Database size:
    def get_lenght(self):
        return len(self.users.keys())

    # Get Statement:
    def get_data(self, email):
        try:
            return self.users.get(email)
        except Exception as error:
            print(error)

    # Remove data:
    def remove(self, email):
        try:
            self.users.pop(email)
            return 0
        except Exception as error:
            print(error)
            return 1
