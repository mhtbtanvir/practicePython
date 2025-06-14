# Ball Splitting Game 🎯

An interactive pygame-based ball splitting game where you click to split balls and manage the chaos within a circular boundary!

## 🎮 Game Overview

In this engaging arcade-style game, you start with a single ball bouncing inside a circle. Your goal is to click on balls to split them while preventing the circle from becoming too crowded.

## ✨ Features

### Core Gameplay
- **Ball Splitting**: Click on red balls to split them into two
- **Circular Boundary**: All action happens within a defined circle
- **Physics**: Realistic ball collisions and bouncing
- **Particle Effects**: Visual feedback with smoke and particle systems

### Special Balls
- **🔵 Blue Balls**: Power-up balls that reduce the total number of balls by half
- **🟢 Green Balls**: Penalty balls that clear all balls (only in Death Mode)

### Game Modes
- **Normal Mode**: Standard gameplay with forgiving mechanics
- **Death Mode**: Hardcore mode where missed clicks add penalty balls

### Power-ups & Effects
- **Black Hole**: Activate after 3 consecutive splits to consume nearby balls
- **Combo System**: Score multiplier for consecutive successful clicks
- **Visual Effects**: Particle systems and miss indicators

### Audio
- Sound effects for splitting, power-ups, and game over
- Audio feedback enhances the gaming experience

## 🎯 How to Play

### Basic Controls
- **Left Click**: Split balls or activate power-ups
- **D Key**: Toggle Death Mode on/off
- **R Key**: Restart game (when game over)
- **ESC**: Exit game

### Gameplay Tips
1. Click on red balls to split them into two smaller balls
2. Blue balls are your friends - they reduce the total ball count by half
3. In Death Mode, green balls clear all balls but missed clicks add penalty balls
4. Keep an eye on the ball density - don't let the circle get too crowded!
5. Build combos for higher scores
6. Use the black hole power-up strategically

### Scoring
- **10 points** per ball split (multiplied by combo)
- **5 points** per ball consumed by black hole
- Combo multiplier increases with consecutive successful clicks

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7+
- pygame library

### Installation
```bash
# Clone or download the repository
# Navigate to the game directory
cd wrap

# Install pygame if not already installed
pip install pygame

# Run the game
python ball_game.py
```

### Running the Executable
If you have the compiled `.exe` file:
```bash
# Simply double-click ball_game.exe or run from command line
ball_game.exe
```

## 📁 Project Structure

```
wrap/
├── ball_game.py          # Main game file
├── ball_game.exe         # Compiled executable (after build)
├── sounds/               # Sound effects directory
│   ├── split.wav        # Ball splitting sound
│   ├── powerup.wav      # Power-up activation sound
│   └── gameover.wav     # Game over sound
├── highscore.txt        # High score storage
└── README.md            # This file
```

## 🎵 Audio Requirements

The game expects the following sound files in the `sounds/` directory:
- `split.wav` - Played when balls are split
- `powerup.wav` - Played when power-ups are activated
- `gameover.wav` - Played when the game ends

## 🏆 Game Over Conditions

The game ends when:
- More than 80 balls are present in the circle
- Ball density exceeds 60% of the circle area
- In Death Mode: Excessive missed clicks can make the game unmanageable

## 🔧 Technical Details

### Built With
- **Python 3.x**
- **Pygame** - Game development library
- **Math** - Physics calculations
- **Random** - Procedural elements

### Key Classes
- `Ball`: Handles individual ball physics and rendering
- `Particle`: Manages visual effects and particle systems  
- `Game`: Main game loop and state management

### Performance Features
- Consistent ball speeds with normalization
- Efficient collision detection
- Particle system with automatic cleanup
- Smooth 60 FPS gameplay

## 🎨 Customization

You can easily modify:
- Colors and visual themes
- Ball physics (speed, bounce factors)
- Special ball frequencies
- Sound effects
- Particle effects
- Game difficulty parameters

## 🐛 Troubleshooting

### Common Issues
1. **No sound**: Ensure sound files exist in the `sounds/` directory
2. **Pygame not found**: Install pygame with `pip install pygame`
3. **Game runs slowly**: Check system resources and close other applications

### System Requirements
- **OS**: Windows, macOS, or Linux
- **RAM**: 256MB minimum
- **Storage**: 50MB free space
- **Audio**: Sound card for audio effects

## 📊 High Scores

High scores are automatically saved to `highscore.txt` and persist between game sessions.

## 🤝 Contributing

Feel free to fork this project and submit improvements! Some ideas:
- New ball types and power-ups
- Different game modes
- Enhanced visual effects
- Mobile touch controls
- Multiplayer support

## 📜 License

This project is open source. Feel free to use, modify, and distribute as needed.

---

**Enjoy the game and happy ball splitting!** 🎯✨

