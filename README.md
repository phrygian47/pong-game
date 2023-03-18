# Pong Game in Python
## Overview

This is a simple pong style game where two players can play on the same keyboard to bounce a ball back and forth. Player 1 one will control their paddle with "w" and "s", player two will control theirs with the up and down arrow keys. If a player fails to bounce the ball back, it will award the opposing player a point, and reset the ball position. The game is over once a player has reached 10 points.

The purpose of writing this software was to gain experience in programming with actors to use in a game framework. It is also to utilize and create a framework that can be repurposed and used for other game ideas and types. Many actors, scripts, and classes used here can be used for a variety of different games.

[Software Demo Video](https://youtu.be/wAwClLd3aw0)

## Development Environment

For this projext I used Visual Studio Code as it is a very useful tool for programming in Python. I wanted to develop a game framework that can be utilized in many different cases, and edited to the user's content. I chose Python mostly because of my previous experience in programming with Python and Python classes. I used the Raylib library to help devlope this GUI for this game and to help handle inputs from the keyboard. The arcade library is also very useful however I've had previous experience using Raylib so that is what I opted for.

## Useful Websites

This website is a useful intro to raylib if you have no experience in using it.
* [dev-journey.com](https://www.dev-journey.com/posts/your-first-step-in-video-game-development-using-raylib-and-python/)

If you need help or a refresher with python classes this is a good review.
* [W3schools](https://www.w3schools.com/python/python_classes.asp)

## Future Work

* Fix top and bottom paddle colision.
* Create more difficulty by increasing ball speed when hit by paddle
* introduce more game elements like a specific goal.
