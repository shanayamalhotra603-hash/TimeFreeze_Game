⏳ TIME FREEZE

TIME FREEZE is a simple 2D arcade-style game developed using Python and Tkinter. The player must collect all the crystals while avoiding enemies and reach the exit door to advance to the next level.

The game features a special Time Freeze ability that allows players to temporarily stop enemy movement and collect crystals safely.

🎮 Features
Player Movement: Move the player using the arrow keys.
Time Freeze Ability: Press the Spacebar to freeze or unfreeze enemies.
Freeze Energy: Time Freeze consumes energy, which can be restored by collecting crystals.
Crystal Collection: Collect crystals to increase your score and freeze energy.
Enemy System: Avoid randomly moving enemies.
Lives System: The player starts with 3 lives.
Level Progression: Collect all crystals and reach the exit to unlock the next level.
Game Over: The game ends when the player loses all lives.
Restart Option: Restart the game by pressing the R key.
🛠️ Technologies Used
Python 3
Tkinter – For GUI and game graphics.
Random Module – For generating random enemy movements and positions.
📋 Requirements
Python 3.x
Tkinter (usually included with standard Python installations)
🚀 Installation and Setup
1. Clone the Repository
bash
git clone https://github.com/your-username/time-freeze.git

2. Navigate to the Project Directory
bash
cd time-freeze

3. Run the Game
bash
python main.py


Note: Replace main.py with the actual name of your Python file if it is different.

🕹️ Game Controls
Key	Action
⬆️ Up Arrow	Move Up
⬇️ Down Arrow	Move Down
⬅️ Left Arrow	Move Left
➡️ Right Arrow	Move Right
Spacebar	Freeze / Unfreeze Time
R	Restart Game
🎯 How to Play
Start the game and control the cyan-colored player.
Collect all the cyan crystals scattered around the game area.
Avoid the red enemies because touching them costs one life.
Use the Spacebar to activate Time Freeze and stop enemies from moving.
Collect crystals to increase your score by 20 points each.
Each collected crystal also restores 20% freeze energy, up to a maximum of 100%.
Once all crystals are collected, reach the purple EXIT door.
Advance through increasingly challenging levels.
Avoid losing all three lives!
📊 Scoring System
Action	Result
Collect one crystal	+20 Score
Collect one crystal	+20% Freeze Energy
Touch an enemy	-1 Life
Complete a level	Advance to next level
⚡ Time Freeze Mechanism

The Time Freeze feature is the main ability of the game.

Press Spacebar to activate Time Freeze.
Enemies stop moving while Time Freeze is active.
Freeze energy decreases over time.
When energy reaches 0%, Time Freeze automatically deactivates.
Collect crystals to restore freeze energy.
📁 Project Structure
text
TIME-FREEZE/
│
├── main.py
└── README.md

🔮 Future Improvements

Possible future enhancements include:

Add background music and sound effects.
Add different types of enemies.
Introduce power-ups and bonus items.
Add new maps and obstacles.
Improve enemy AI and movement patterns.
Add a main menu and pause option.
Save high scores.
Add animations and improved visual effects.
👨‍💻 Author

Developed as a Python GUI-based game project using Tkinter.

📜 License

This project is open-source and available for learning and educational purposes.

Enjoy playing TIME FREEZE! ⏳🎮