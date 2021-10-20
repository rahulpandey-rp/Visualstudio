class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return(f"{self. email}")


user1 = User("abc", "abc@gmail.com")
user2 = User("def", "def@gmail.com")
user3 = User("ghi", "ghi@gmail.com")
user4 = User("jkl", "jkl@gmail.com")
print(user1)
