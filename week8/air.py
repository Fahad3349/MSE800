# ============================================
# Domestic Flight System - Air New Zealand
# Demonstrating Single Inheritance
# ============================================

# Parent class
class Flight:
    """
    This parent class represents a general flight.
    It contains common attributes and methods that can be shared
    by different types of flights.
    """

    def __init__(self, flight_number, airline, departure_city, arrival_city, departure_time, ticket_price):
        # Shared attributes
        self.flight_number = flight_number
        self.airline = airline
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = departure_time
        self.ticket_price = ticket_price

    # Shared method inherited by child class
    def display_flight_info(self):
        print("Flight Information")
        print("------------------")
        print(f"Flight Number: {self.flight_number}")
        print(f"Airline: {self.airline}")
        print(f"From: {self.departure_city}")
        print(f"To: {self.arrival_city}")
        print(f"Departure Time: {self.departure_time}")
        print(f"Ticket Price: NZD {self.ticket_price}")

    # Shared method inherited by child class
    def calculate_discount(self):
        discount = self.ticket_price * 0.10
        final_price = self.ticket_price - discount
        return final_price


# Child class
class DomesticFlight(Flight):
    """
    This subclass represents a domestic flight operated by Air New Zealand.
    It inherits common flight details from the Flight parent class
    and also includes domestic-flight-specific attributes and methods.
    """

    def __init__(self, flight_number, departure_city, arrival_city, departure_time, ticket_price, region, baggage_allowance):
        # Calling the parent class constructor using super()
        # Airline is fixed as Air New Zealand for this system
        super().__init__(
            flight_number,
            "Air New Zealand",
            departure_city,
            arrival_city,
            departure_time,
            ticket_price
        )

        # Attributes specific to DomesticFlight
        self.region = region
        self.baggage_allowance = baggage_allowance

    # Method specific to DomesticFlight
    def display_domestic_flight_info(self):
        # Reusing inherited method from Flight class
        self.display_flight_info()

        print(f"Region: {self.region}")
        print(f"Baggage Allowance: {self.baggage_allowance} kg")

        discounted_price = self.calculate_discount()
        print(f"Discounted Price: NZD {discounted_price}")

    # Method specific to DomesticFlight
    def check_baggage_allowance(self, passenger_baggage):
        if passenger_baggage <= self.baggage_allowance:
            print("Baggage is within the allowed limit.")
        else:
            extra = passenger_baggage - self.baggage_allowance
            print(f"Baggage exceeds the limit by {extra} kg.")


# ============================================
# Main Program
# ============================================

# Creating an object of DomesticFlight
domestic_flight_1 = DomesticFlight(
    flight_number="NZ143",
    departure_city="Auckland",
    arrival_city="Wellington",
    departure_time="10:30 AM",
    ticket_price=180,
    region="North Island",
    baggage_allowance=23
)

# Display domestic flight information
domestic_flight_1.display_domestic_flight_info()

print()

# Check baggage allowance
domestic_flight_1.check_baggage_allowance(25)