# Module Six Milestone Software Development Worksheet

* **Course**: IT 140 - Introduction to Scripting
* **Activity**: Module Six Milestone
* **Program**: Simplified Movement Prototype
* **Purpose**: Optional working notes for the M6 Construct + Test checkpoint

> [!NOTE]
> This worksheet is not a graded deliverable unless your instructor specifically
> asks for it. The graded milestone work belongs in `move_between_rooms.py`.

## How to Use This Worksheet

Keep answers brief. Use it to translate the current milestone requirements and
your Project One movement design into a small implementation plan.

## 1. Scope Check

### Where to Look

* Module Six Milestone Guidelines and Rubric
* Milestone Simplified Text Game Flowchart/supporting materials
* `../design/move.pseudo`
* `../analysis/text_based_game_srs.md`, Section 2

### Prompt

In your own words, what does the simplified milestone need to accomplish?

**Your notes:**

The simplified milestone needs to let the player move between three rooms using valid direction commands or exit the game. The program uses a dictionary to check room connections, a loop to continue gameplay, and conditional statements to handle player input. Items, inventory, the villain, and the final win or loss conditions will be added in Project Two.

### Reduced-Scope Checkpoint

* [x] I understand that the milestone uses the provided three-room dictionary.
* [x] I understand that the milestone includes movement and `exit`.
* [x] I understand that items, inventory, villain, and final win/loss behavior
  are deferred to Project Two.

## 2. Understand the Provided Dictionary

### Prompt

Trace the room connections before coding.

| Current room | Valid direction | Destination |
| --- | --- | --- |
| Great Hall | south | Bedroom |
| Bedroom | north | Great Hall |
| Bedroom | east | Cellar |
| Cellar | west | Bedroom |

What should happen if a requested direction is not listed for the current room?

**Your notes:**

The program should display an invalid move message and keep the player in the current room. The player should be able to enter another command.
## 3. Input, Process, Output

### Input

The player enters a direction, such as north, south, east, or west, or enters exit to end the game. The program must recognize valid directions for the current room, the exit command, and invalid commands.

### Process

The program checks the player's command using conditional statements. If the command is a valid direction, the dictionary determines the destination room. If the player enters exit, the program sets the current room to exit. Otherwise, the program displays an error message without changing rooms.

### Output

The program displays the player's current room and prompts for a command. It displays a message after a successful move, an error message after invalid input, and a goodbye message when the player exits.

## 4. Gameplay Loop Plan

### Prompt

Describe one iteration of the loop.

1. Display the player's current room.
2. Ask the player to enter a direction or exit.
3. Check the command and either move to a connected room, exit the game, or display an error message.
4. Repeat the loop until the player enters exit.

What condition causes the loop to stop?

**Your notes:**

The loop stops when the player's current room is set to exit.

## 5. Branch Plan

Complete the behavior table without writing the full Python solution here.

| Command category | Expected behavior |
| --- | --- |
| Valid movement | Use the dictionary to move the player to the connected room. |
| `exit` | Set the current room to exit and end the game. |
| Invalid input | Display an error message and keep the player in the same room. |

## 6. Incremental Construction Check

* [x] I can display the current room.
* [x] I can obtain one command.
* [x] I can recognize a valid movement command.
* [x] I can update the current room after a valid move.
* [x] I can recognize `exit`.
* [x] I can reject invalid input.
* [x] I can repeat until the exit condition is reached.

## 7. Test and Debug Notes

| Case | Expected result | Actual result | Pass? |
| --- | --- | --- | :---: |
| Valid move | South from Great Hall moves to Bedroom. | Moves to Bedroom. | Yes |
| Different valid move | East from Bedroom moves to Cellar. | Moves to Cellar. | Yes |
| Invalid direction | North from Great Hall displays an error and stays in Great Hall. | Displays an error and stays in Great Hall. | Yes |
| Invalid command | Typing jump displays an error and keeps the current room. | Displays an error and stays in the current room. | Yes |
| Exit | Typing exit ends the game. | Displays a goodbye message and ends the game. | Yes |

**Debugging note:**

One issue to watch for is allowing the player to move in a direction that is not connected to the current room. I corrected this by checking whether the command exists in the current room's dictionary before updating the player's location.

## 8. Project Two Handoff

What did you learn from this prototype that should carry into Project Two?

**Your notes:**

I learned how to use a dictionary to connect rooms and how to use a loop and conditional statements to process player commands. I also learned the importance of testing valid and invalid inputs to make sure the game works correctly.

What milestone-only behavior must **not** become the final design?

**Your notes:**

The three-room sample map is only for the milestone and must be replaced with the room connections from my Project Two design. The simplified exit command must also be expanded to support the final game's item collection, inventory, villain encounter, and win or loss conditions.
