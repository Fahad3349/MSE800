# Air New Zealand Flight Management System

## Overview

This project demonstrates **Hybrid Inheritance** in Python using an Air New Zealand Flight Management System.

The system includes:

* Flight (Parent Class)
* DomesticFlight (Child Class)
* InternationalFlight (Child Class)
* LoyaltyProgram (Parent Class)
* PremiumInternationalFlight (Hybrid Inheritance Class)

## Features

* Manage domestic and international flights.
* Display flight information.
* Calculate ticket discounts.
* Check passport and visa requirements.
* Manage loyalty points.
* Premium passenger services such as lounge access and meal preferences.

## Inheritance Structure

```text
Flight
├── DomesticFlight
└── InternationalFlight
        │
        └── PremiumInternationalFlight

LoyaltyProgram
        │
        └── PremiumInternationalFlight
```

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
