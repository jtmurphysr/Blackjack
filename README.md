# Python Blackjack Game

A command-line implementation of the classic casino card game Blackjack (also known as 21), written in Python using object-oriented programming principles.

## Features

- Full implementation of basic Blackjack rules
- Object-oriented design with proper class structure
- Type hints for better code clarity
- Automatic ace value adjustment (1 or 11)
- Dealer AI that follows standard casino rules
- Card deck management with automatic reshuffling
- Play again functionality

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Clone this repository or download the `blackjack.py` file
2. Ensure you have Python 3.6+ installed
3. Run the game using Python:


## How to Play

1. The game starts automatically when you run the script
2. You and the dealer will each receive two cards
3. Your cards will be visible, but only one of the dealer's cards is shown
4. On your turn, you can:
   - Enter 'h' to Hit (receive another card)
   - Enter 's' to Stand (keep your current hand)
5. The dealer will then play according to standard casino rules:
   - Must hit on 16 or below
   - Must stand on 17 or above
6. The winner is determined by:
   - Whoever has the highest value hand without going over 21
   - If you go over 21, you "bust" and lose
   - If the dealer goes over 21, they bust and you win
   - If both players have the same value, it's a tie

## Game Rules

- Number cards (2-10) are worth their face value
- Face cards (Jack, Queen, King) are worth 10
- Aces are worth 11 unless that would cause a bust, then they're worth 1
- The dealer must hit on 16 or below and stand on 17 or above
- The maximum hand value is 21

## Code Structure

- `Suit`: Enum class for card suits
- `Rank`: Enum class for card ranks and their values
- `Card`: Class representing a playing card
- `Player`: Class managing player/dealer hands and actions
- `Blackjack`: Main game class handling game logic and flow

## Future Improvements

- Add betting system
- Implement split functionality
- Add multiplayer support
- Include insurance options
- Add statistical tracking
- Implement a graphical user interface

## Contributing

Feel free to fork this repository and submit pull requests for any improvements you'd like to add.

## License

This project is open source and available under the MIT License.
