import argparse
import json

def file_1():
    file = open("user_database.json", 'w')
    file.write(json.dumps([]))
    file.close()
    return open("user_database.json", 'r')

def user_1_create(users):
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="username")
    parser.add_argument("-e", "--email", help="email")
    parser.add_argument("-s", "--status", help="status")
    args = parser.parse_args()
    try:
        users["username"] = args.username
        users["email"] = args.email
        users["status"] = args.status
    except IndexError:
        raise Exception("Not the correct command!")

    def check_user(user, users_info):
        for users in users_info:
            if user["username"] == users["username"] or user["email"] == users["email"]:
                return True
        return False

    def add_user(user):
        try:
            read_files = open("user_database.json", "r")
        except FileNotFoundError:
            read_files = user_1_create()
        try:
            user_database = json.loads(read_files.read())
        except ValueError:
            with open("user_database.json", 'w') as w_file:
                w_file.write(json.dumps([]))
            user_database = []
        read_files.close()

        if not check_user(user, user_database):
            user_database.append(user)
            with open("user_database.json", "w") as w_file:
                w_file.write(json.dumps(user_database, indent=4, sort_keys=True))
        else:
            raise "User with user or email"

        if __name__ == "__main__":
            new_user = {}
            user_1_create(new_user)
            add_user(new_user)

