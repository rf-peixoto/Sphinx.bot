import sqlite3

class Manager:
    # Initialize:
    def __init__(self):
        print("Connecting to the database.")
        try:
            self.db = sqlite3.connect("database.db")
            self.cursor = self.db.cursor()
        except Exception as error:
            print("Error while openning the database: {0}".format(error))

    # Get Data:
    def get_data(self, email):
        try:
            self.cursor.execute("SELECT password FROM accounts WHERE email='{0}'".format(email))
            return self.cursor.fetchone()[0]
        except Exception as error:
            print("Error while searching for {0}: {1}".format(email, error))

    # Remove Data:
    def remove(self, email):
        command = "UPDATE accounts SET password = '[REMOVED]' WHERE email='{0}'".format(email)
        try:
            self.cursor.execute(command)
            return True
        except Exception as error:
            print("Error while trying to remove {0}: {1}".format(email, error))

    # Save Database:
    def save_changes(self):
        try:
            self.db.commit()
            return True
        except Exception as error:
            print('Error while saving: {0}'.format(error))

