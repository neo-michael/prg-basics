import random

class Thermometer:
    def __init__(self):
        self.temp = 34
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False

    def measure(self):
        self.temp = random.randint(340, 420) / 10
    
    def display(self):
        if self.temp > 41:
            print(f"CRITICAL TEMPERATURE")
        elif self.temp > 37:
            print(f"Temperature: {self.temp}C (fever)")
        else:
            print(f"Temperature: {self.temp}C")


def main():
    th = Thermometer()
    th.turn_on()
    th.measure()
    th.display()
    th.turn_off()

if __name__ == "__main__":
    main()