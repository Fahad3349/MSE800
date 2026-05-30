# ==================================================
# Air New Zealand Flight Management System
# Demonstrating Hybrid Inheritance
# ==================================================

# Parent class
class Flight:
    def __init__(self, flight_number, airline, departure_city, arrival_city, departure_time, ticket_price):
        self.flight_number = flight_number
        self.airline = airline
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = departure_time
        self.ticket_price = ticket_price

    def display_flight_info(self):
        print(f"Flight Number: {self.flight_number}")
        print(f"Airline: {self.airline}")
        print(f"From: {self.departure_city}")
        print(f"To: {self.arrival_city}")
        print(f"Departure Time: {self.departure_time}")
        print(f"Ticket Price: NZD {self.ticket_price}")

    def calculate_discount(self):
        return self.ticket_price * 0.90

    def update_ticket_price(self, new_price):
        self.ticket_price = new_price
        print(f"Updated Ticket Price: NZD {self.ticket_price}")


# Child class 1
class DomesticFlight(Flight):
    def __init__(self, flight_number, departure_city, arrival_city, departure_time, ticket_price, region, baggage_allowance):
        super().__init__(flight_number, "Air New Zealand", departure_city, arrival_city, departure_time, ticket_price)
        self.region = region
        self.baggage_allowance = baggage_allowance

    def display_domestic_details(self):
        self.display_flight_info()
        print(f"Region: {self.region}")
        print(f"Baggage Allowance: {self.baggage_allowance} kg")

    def check_baggage_allowance(self, baggage_weight):
        if baggage_weight <= self.baggage_allowance:
            print("Baggage is within the allowed limit.")
        else:
            print("Baggage exceeds the allowed limit.")

    def calculate_domestic_tax(self):
        tax = self.ticket_price * 0.15
        return tax


# Child class 2
class InternationalFlight(Flight):
    def __init__(self, flight_number, departure_city, arrival_city, departure_time, ticket_price, country, passport_required, visa_required):
        super().__init__(flight_number, "Air New Zealand", departure_city, arrival_city, departure_time, ticket_price)
        self.country = country
        self.passport_required = passport_required
        self.visa_required = visa_required

    def display_international_details(self):
        self.display_flight_info()
        print(f"Destination Country: {self.country}")

    def check_passport_requirement(self):
        if self.passport_required:
            print("Passport is required for this flight.")
        else:
            print("Passport is not required.")

    def check_visa_requirement(self):
        if self.visa_required:
            print("Visa is required for this flight.")
        else:
            print("Visa is not required.")


# Second parent class for multiple inheritance
class LoyaltyProgram:
    def __init__(self, member_id, points):
        self.member_id = member_id
        self.points = points

    def add_points(self, new_points):
        self.points += new_points
        print(f"Points Added. Total Points: {self.points}")

    def redeem_points(self, used_points):
        if used_points <= self.points:
            self.points -= used_points
            print(f"Points Redeemed. Remaining Points: {self.points}")
        else:
            print("Not enough points.")

    def display_loyalty_info(self):
        print(f"Member ID: {self.member_id}")
        print(f"Loyalty Points: {self.points}")


# Hybrid inheritance class
class PremiumInternationalFlight(InternationalFlight, LoyaltyProgram):
    def __init__(self, flight_number, departure_city, arrival_city, departure_time, ticket_price,
                 country, passport_required, visa_required, member_id, points,
                 lounge_access, meal_preference):

        InternationalFlight.__init__(
            self,
            flight_number,
            departure_city,
            arrival_city,
            departure_time,
            ticket_price,
            country,
            passport_required,
            visa_required
        )

        LoyaltyProgram.__init__(self, member_id, points)

        self.lounge_access = lounge_access
        self.meal_preference = meal_preference

    def display_premium_details(self):
        self.display_international_details()
        self.display_loyalty_info()
        print(f"Lounge Access: {self.lounge_access}")
        print(f"Meal Preference: {self.meal_preference}")

    def check_lounge_access(self):
        if self.lounge_access:
            print("Passenger has lounge access.")
        else:
            print("Passenger does not have lounge access.")

    def set_meal_preference(self, meal):
        self.meal_preference = meal
        print(f"Meal preference updated to: {self.meal_preference}")


# Main program
domestic = DomesticFlight("NZ101", "Auckland", "Wellington", "09:30 AM", 180, "North Island", 23)
domestic.display_domestic_details()

print("\n----------------------\n")

premium = PremiumInternationalFlight(
    "NZ289",
    "Auckland",
    "Shanghai",
    "11:00 PM",
    1200,
    "China",
    True,
    True,
    "MEM123",
    500,
    True,
    "Vegetarian"
)

premium.display_premium_details()
premium.check_passport_requirement()
premium.check_visa_requirement()
premium.add_points(100)