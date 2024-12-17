class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f"{self.rate_per_km}, {self.distance}, {self.fare}")

def main():
    # your program
    t1 = TaxiRide(20)
    t2 = TaxiRide(10)
    t1.calculate_fare(11)
    t2.calculate_fare(30)

    t1.print_receipt()
    t2.print_receipt()
if __name__ == "__main__":
    main()
