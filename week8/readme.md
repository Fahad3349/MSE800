# Air New Zealand Domestic Flight System

## Overview

This project demonstrates the concept of **Single Inheritance** in Python. A parent class named `Flight` contains common flight attributes and methods, while a child class named `DomesticFlight` inherits these features and adds domestic flight-specific functionality.

## Classes

### Flight (Parent Class)

Attributes:

* flight_number
* airline
* departure_city
* arrival_city
* departure_time
* ticket_price

Methods:

* display_flight_info()
* calculate_discount()

### DomesticFlight (Child Class)

Additional Attributes:

* region
* baggage_allowance

Additional Methods:

* display_domestic_flight_info()
* check_baggage_allowance()

## Inheritance

```text
Flight
   ↑
DomesticFlight
```

The `DomesticFlight` class inherits all common attributes and methods from the `Flight` class and extends them with additional domestic flight features.

## Technology Used

* Python 3
* Object-Oriented Programming (OOP)

