# PYVESTOR

A random based trading/investment game with a completely fictional cryptocurrency market and rates.

### Introduction Video : <https://youtu.be/CXPopVQu0FU>

<br>

## Description

With this in-terminal game named PYVESTOR, written in Python, by Muhammed B. Anbarpinar; you will have a completely fictional cryptocurrency market, random based cryptocurrency value rates changing daily (in game days) and have the right to invest or divest your money on cryptocurrencies in the way you want! You can stuck all the eggs in the same basket or you can choose a more deffensive way. Are you brave enough? Let's see!

<br>

## Files Created:

### project.py
   - The main code, all the functionality of the game is implemented in this file.

### settings.py
   - Random cryptocurrency value rates changing daily is one of the most important and complicated features of the game so, it deserves to be in its own file. The algorithm which provides the randomness to the game is implemented in this file and its only purpose is providing this.

### setting.txt
   - The data provided by "settings.py" is stored in this file.

### default_coins.txt
   - This file includes the default values of each fictional coin in the game, which will be used when the user starts a new game.

### coins.txt
   - Since the game has a daily time mechanism and different cryptocurrency value rates for each day, this file includes current day's coin values.

### saved.txt
   - User's data is stored in this file.

### requirements.txt
   - This file includes every library which should be downloaded before running the program.

### test_project.py
   - This is the file where some of the game's functions are tested.

<br>

## How To Run
First of all, you should have python setted in your device. You should have downloaded every file listed above in the same folder and have downloaded all the libraries listed in "requirements.txt". Then you should double click on "project.py" or run the program in the terminal screen with "python {.../project.py}" code.

<br>

## Operating Logic
### Starting
When you start a new game, you are prompted for your name first. This is your first step into the PYVESTOR world. Once you give a name, you start the game with $100 cash that you can see in the game bar to the left of the "Days" box, at the top of the terminal screen.
### Playing
First thing you should do after starting the game is checking the cryptocurrency market, this is why you are here! You can see 20 different coins and you can invest your money on the ones you want and you can divest them and take your money with your profit, or your loss. After you purchase some, you can choose waiting option[^1] to wait some amount of days, hoping the currency you are holding earn more value! After waiting, you can go to your wallet and you can view your assets and how much the worth so, you can decide to stay, invest more or divest. And whenever you feel like you are done for this session, you can alway choose "Save & Quit" option to leave the game saving your data so, you can come back and move on from where you left!
### Finishing
When you reach 100 days in the game days, it means you came to the end of the game. Your assets (if you have any) are authomatically converted into cash. You will see an ending message depending on how much money do you have at the end of the game. But it is not an end, it means you got a chance to start over and make more money every time!

<br>

#### -Muhammed B. Anbarpinar

[^1]: To be able to choose waiting option, you don't have to have purchased something. If you didn't like the market, just wait and see the changes!
