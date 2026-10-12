"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# Set the player's starting room.
current_room = "Great Hall"

# Create the gameplay loop.
while current_room != "exit":

    # Display the current room.
    print(f"\nYou are in the {current_room}.")

    # Prompt the player for a movement command or exit.
    command = input("Enter a direction (north, south, east, west) or exit: ")
    command = command.lower().strip()

    # Exit the game.
    if command == "exit":
        current_room = "exit"
        print("Thanks for playing!")

    # Check whether the direction is valid for the current room.
    elif command in rooms[current_room]:
        current_room = rooms[current_room][command]
        print(f"You moved to the {current_room}.")

    # Handle invalid commands or unavailable directions.
    else:
        print("Invalid move. Please try again.")
