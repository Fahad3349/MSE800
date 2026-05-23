from fish import FishFactory
from aquarium import Aquarium


def main():
    aquarium = Aquarium()

    print("Welcome to Auckland Aquarium Management System")

    while True:
        print("\nFish Categories:")
        print("1. Goldfish")
        print("2. Shark")
        print("3. Angelfish")
        print("4. Tuna")
        print("5. Salmon")
        print("6. Display Fish Stock")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                quantity = int(input("Enter number of Goldfish: "))
                fish = FishFactory.create_fish("goldfish", quantity)
                aquarium.add_fish(fish)
                print("Goldfish added successfully.")

            elif choice == "2":
                quantity = int(input("Enter number of Shark: "))
                fish = FishFactory.create_fish("shark", quantity)
                aquarium.add_fish(fish)
                print("Shark added successfully.")

            elif choice == "3":
                quantity = int(input("Enter number of Angelfish: "))
                fish = FishFactory.create_fish("angelfish", quantity)
                aquarium.add_fish(fish)
                print("Angelfish added successfully.")

            elif choice == "4":
                quantity = int(input("Enter number of Tuna: "))
                fish = FishFactory.create_fish("tuna", quantity)
                aquarium.add_fish(fish)
                print("Tuna added successfully.")

            elif choice == "5":
                quantity = int(input("Enter number of Salmon: "))
                fish = FishFactory.create_fish("salmon", quantity)
                aquarium.add_fish(fish)
                print("Salmon added successfully.")

            elif choice == "6":
                aquarium.display_fish()

            elif choice == "7":
                print("Thank you for using the Aquarium Management System.")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()