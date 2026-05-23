class Aquarium:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Aquarium, cls).__new__(cls)
            cls._instance.fish_list = []
        return cls._instance

    def add_fish(self, fish):
        self.fish_list.append(fish)

    def display_fish(self):
        print("\nAuckland Aquarium Fish Stock")
        print("---------------------------")

        if not self.fish_list:
            print("No fish available in the aquarium.")
        else:
            for fish in self.fish_list:
                print(f"Fish Category: {fish.category()} | Available: {fish.quantity}")