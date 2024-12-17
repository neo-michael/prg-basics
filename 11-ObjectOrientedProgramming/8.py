class Contact:
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone

    def __str__(self):
        return f"{self.name}: {self.email} -> {self.telephone}"   
    
class ContactList:
    def __init__(self):
        self.contacts = []
    
    def add_new(self, con):
        self.contacts.append(con)
    
    def display(self):
        for con in self.contacts:
            print(con)
        