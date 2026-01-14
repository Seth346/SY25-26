lineup = [
    ("Code Play", "Indie", 30),
    ("The Pythonistas", "Rock", 45),
    ("Syntax Error", "Metal", 60)
]

while True:
    print("\n---Py-Fest 2026 stage manager")
    print("1. View Lineup & Total Time")
    print("2. Add a New Band")
    print("3. Move First Band to End (Late Arrival)")
    print("4. Remove a Band by Name")
    print("5. Move Band to Specific Position")
    print("6. Exit")
    choice = input("select an option (1-6): ")
    if choice == '1':
        print("\nCurrent Lineup:")
        total_time = 0
        for i, (name, genre, duration) in enumerate(lineup):
            print(f"{i + 1}. {name} - {genre} ({duration} mins)")
            total_time += duration
        print(f"Total Duration: {total_time} minutes")
    elif choice == '2':
        name = input("Enter band name: ")
        genre = input("Enter genre: ")
        try:
            duration = int(input("Enter set duration (minutes): "))
            lineup.append((name, genre, duration))
            print(f"{name} added to the lineup.")
        except ValueError:
            print("Invalid duration. Please enter a number.")
    elif choice == '3':
        if lineup:
            band = lineup.pop(0)
            lineup.append(band)
            print(f"{band[0]} moved to the end of the lineup.")
        else:
            print("Lineup is empty.")
    elif choice == '4':
        name_to_remove = input("Enter the name of the band to remove: ")
        found = False
        for i, (name, genre, duration) in enumerate(lineup):
            if name.lower() == name_to_remove.lower():
                removed = lineup.pop(i)
                print(f"{removed[0]} removed.")
                found = True
                break
        if not found:
            print("Band not found.")
    elif choice == '5':
        name_to_move = input("Enter the name of the band to move: ")
        try:
            new_position = int(input("Enter the new position (1-based): ")) - 1
            if new_position < 0 or new_position >= len(lineup):
                print("Invalid position.")
                continue
            for i, (name, genre, duration) in enumerate(lineup):
                if name.lower() == name_to_move.lower():
                    band = lineup.pop(i)
                    lineup.insert(new_position, band)
                    print(f"{band[0]} moved to position {new_position + 1}.")
                    break
            else:
                print("Band not found.")
        except ValueError:
            print("Please enter a valid number for the position.")
    elif choice == '6':
        print("Exiting the stage manager. Have a great show!")
        break
    else:
        print("Invalid choice.")











