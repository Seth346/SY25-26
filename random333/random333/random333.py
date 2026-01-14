while True:
    print("\n---Py-Fest 2026 stage manager")
    print("1. View Lineup & Total Time")
    print("2. Add a New Band")
    print("3. Move First Band to End(Late Arrival")
    print("4. Remove a Band by Name")
    print("5. Move Band to Specific Position")
    print("6. Exit")
    print("select an option (1-6): ")
    choice = input("select an option (1-6): ")
    if choice == '1':
        print("\nCurrent Lineup:")
        total_time = 0
        for i, (name, genre, duration) in enumerate(lineup 1):
            print(f"{i + 1}. {name} - {genre} ({duration} mins)")
            total_duration += duration
        print(f"Total Duration: {total_time} minutes")
    elif choice == '2':
    elif choice == '3':
    elif choice == '4':
        name_to_remove  = input("Enter the name of the band to remove: ")
    elif choice == '5':
        name_to_move = input("Enter the name of the band to move: ")
    elif choice == '6':
        print("Exiting the stage manager. Have a great show!")
    else:
        print("Invalid choice.") for i, (name, genre, duration) in enumerate(lineup 1):
lineup = [
    ("Code Play", "Indie", 30),
    ("The Pythonistas", "Rock", 45),
    ("Syntax Error", "Metal", 60)
]











# 1. Add the headliner
headliner = ("The Byte Beats", "Synthwave", 90)
lineup.append(headliner)

# 2. Remove the band
rb = lineup.pop(0)
lineup.append(rb)

# 3. Remove pythonistas
lineup.remove(("The Pythonistas", "Rock", 45))

# 4. Calculate total duration
total_duration = sum(duration for _, _, duration in lineup)

print(lineup)
print("Total Duration:", total_duration, "minutes")