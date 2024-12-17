class Phone:
    def __init__(self):
        self.is_on = False 
        self.secret_password = 301
        self.unlocked = False
    
    def turn_on(self):
        self.is_on = True
    
    def unlock(self, password):
        partial = 0
        for c in password:
            partial += ord(c) ^ 14
        
        if partial == self.secret_password:
            self.unlocked = True
        else:
            print("Incorrect password")
    
    def is_unlocked(self):
        return self.unlocked

p1 = Phone()
print(p1.is_on)
p1.turn_on()
print(p1.is_on)
print(p1.is_unlocked())
p1.unlock("1")
p1.unlock("12345")
print(p1.is_unlocked())