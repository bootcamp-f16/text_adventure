#Implementation Plan

## Game
Game class will be used to create an object that controls my game.

### Data
* current_room: The room the player is currently in
* player: The player object that is playing the game
* guesses_left: The number of guess left before the user wins/loses
* github_username: store the user name entered by the user

### Methods
* handle_input: input handling
* check_status: check win and lose conditions and cause the appropiate thing to happen if needed
* setup: setup the game

## Player
Object that will hold the clues in inventory, keep track of health

## ActionHandler
A base class that checks input from the user and triggers the need action if an action is found to match

## Action
A class that will be used to structure actions and what happens when an action is triggered

## Monster
A class that the player can interact with.

## GithubOverlord
A child class of monster that talks to the user and handles the guessing actions

## Item
A base class for items the user can pick up

## Clue
A child class of Item that will provide the hints the user needs to answer the Overlord's question
