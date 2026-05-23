# Auckland Aquarium Management System

## Project Description

This project is a simple Aquarium Management System designed for managing fish stock in an aquarium in Auckland.

The system accepts input data from the user and displays the fish category along with the number of fish currently available in the aquarium.

The fish categories included in this project are:

- Goldfish
- Shark
- Angelfish
- Tuna
- Salmon

## Features

- Add Goldfish stock
- Add Shark stock
- Add Angelfish stock
- Add Tuna stock
- Add Salmon stock
- Display current fish stock
- Uses Factory Design Pattern
- Uses Singleton Design Pattern

## Design Patterns Used

### 1. Factory Design Pattern

The Factory Design Pattern is used to create fish objects.

Instead of creating each fish object directly in the main program, the `FishFactory` class is responsible for creating the correct fish object based on the user input.

Example:

```python
fish = FishFactory.create_fish("goldfish", quantity)

2. Singleton Design Pattern

The Singleton Design Pattern is used in the Aquarium class.

Only one aquarium object is created throughout the whole program. This is useful because the system manages one aquarium in Auckland.

Example:

aquarium = Aquarium()

Even if the Aquarium class is called multiple times, it will return the same object.

File Description
main.py

This file contains the main menu of the system. It accepts user input and displays options to add fish or view fish stock.

fish.py

This file contains the fish classes and the FishFactory class.

aquarium.py

This file contains the Aquarium class, which uses the Singleton Pattern.

README.md

This file contains the project description, features, design pattern explanation, and running instructions.

How to Run the Project
Download or clone the GitHub repository.
Open the project folder.
Run the following command:
python main.py
Sample Output
Welcome to Auckland Aquarium Management System

Fish Categories:
1. Goldfish
2. Shark
3. Angelfish
4. Tuna
5. Salmon
6. Display Fish Stock
7. Exit

Enter your choice: 1
Enter number of Goldfish: 25
Goldfish added successfully.

Enter your choice: 6

Auckland Aquarium Fish Stock
---------------------------
Fish Category: Goldfish | Available: 25