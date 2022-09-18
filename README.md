# The monte-hall problem
This program plays the [monte-hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem).

It has a variation on how the game is played.

Normally, a player (p1) selects a door in hopes of finding a prize.
After they make their selection, all doors are opened except the door they selected and door with the prize.
The player is offered the ability to change their answer.

At this point, our variation is we also introduce a new player (p2) who can select from either of the unopened doors.

Then, the door with the prize is revealed and the players who selected the door with the prize win
and the players who selected a door without the prize receive a goat.

## CLI usage
```
usage: monte-hall.py [-h] [-d NUMDOORS] [-g NUMGAMES] [-q] [-v]
                     [--p1-name P1NAME] [--p1-always] [--p1-never]
                     [--p2-name P2NAME]

Two players begin the monte hall problem...

optional arguments:
  -h, --help            show this help message and exit
  -d NUMDOORS, --doors NUMDOORS
                        Number of doors in the game (default=3)
  -g NUMGAMES, --games NUMGAMES
                        Number of times we play the game (default=1)
  -q, --quiet           Don't announce details of each game. (default=false)
  -v, --announceEachGame
                        Announce details of each game? (default=true)
  --p1-name P1NAME      Player 1's name
  --p1-always           Player 1 always changes their selection (default=true)
  --p1-never            Player 1 never changes their selection (default=false)
  --p2-name P2NAME      Player 2's name
```


# Sample runs:

## There are 3 doors and player 1 always changes their answer and we show all game details:
```
$ python ./monte-hall.py --games 2
Host: We are starting game 1! There are 3 closed doors
Host: Don't tell anyone, but the prize is behind door 2
Alice: I always change my door selection, I have selected door 3, and I couldn't change my selection
Host: All doors have been opened except 3 and 2
Bob: I can't change my door selection, I have selected door 3, and I couldn't change my selection
Alice: I always change my door selection, I have selected door 2, and I did change my selection
Alice wins a prize!
Bob receives a goat

Host: We are starting game 2! There are 3 closed doors
Host: Don't tell anyone, but the prize is behind door 1
Alice: I always change my door selection, I have selected door 1, and I couldn't change my selection
Host: All doors have been opened except 1 and 2
Bob: I can't change my door selection, I have selected door 1, and I couldn't change my selection
Alice: I always change my door selection, I have selected door 2, and I did change my selection
Alice receives a goat
Bob wins a prize!

Whew. We have played 2 games.
Alice won 1 prizes and 1 goats for a 50.0% win rate
Bob won 1 prizes and 1 goats for a 50.0% win rate
```

## There are 3 doors, player 1 never changes their answer, played 1000 times
```
$ python ./monte-hall.py --games 1000 --doors 3 --p1-never --quiet
Whew. We have played 1000 games.
Alice won 348 prizes and 652 goats for a 34.8% win rate
Bob won 518 prizes and 482 goats for a 51.8% win rate
```

```
$ python ./monte-hall.py --games 1000 --doors 3 --p1-never --quiet
Whew. We have played 1000 games.
Alice won 327 prizes and 673 goats for a 32.7% win rate
Bob won 494 prizes and 506 goats for a 49.4% win rate
```

```
$ python ./monte-hall.py --games 1000 --doors 3 --p1-never --quiet
Whew. We have played 1000 games.
Alice won 332 prizes and 668 goats for a 33.2% win rate
Bob won 475 prizes and 525 goats for a 47.5% win rate
```

## There are 3 doors, player 1 always changes their answer, played 1000 times
```
$ python ./monte-hall.py --games 1000 --doors 3 --p1-always --quiet
Whew. We have played 1000 games.
Alice won 671 prizes and 329 goats for a 67.1% win rate
Bob won 518 prizes and 482 goats for a 51.8% win rate
```

```
$ python ./monte-hall.py --games 1000 --doors 3 --p1-always --quiet
Whew. We have played 1000 games.
Alice won 687 prizes and 313 goats for a 68.7% win rate
Bob won 465 prizes and 535 goats for a 46.5% win rate
```

```
$ python ./monte-hall.py --games 1000 --doors 3 --p1-always --quiet
Whew. We have played 1000 games.
Alice won 675 prizes and 325 goats for a 67.5% win rate
Bob won 505 prizes and 495 goats for a 50.5% win rate
```

## There are 100 doors, player 1 never changes their answer, played 1000 times
```
$ python ./monte-hall.py --games 1000 --doors 100 --p1-never --quiet
Whew. We have played 1000 games.
Alice won 12 prizes and 988 goats for a 1.2% win rate
Bob won 498 prizes and 502 goats for a 49.8% win rate
```

```
$ python ./monte-hall.py --games 1000 --doors 100 --p1-never --quiet
Whew. We have played 1000 games.
Alice won 14 prizes and 986 goats for a 1.4% win rate
Bob won 505 prizes and 495 goats for a 50.5% win rate
```

```
$ python ./monte-hall.py --games 1000 --doors 100 --p1-never --quiet
Whew. We have played 1000 games.
Alice won 6 prizes and 994 goats for a 0.6% win rate
Bob won 486 prizes and 514 goats for a 48.6% win rate
```

## There are 100 doors, player 1 always changes their answer, played 1000 times
```
$ python ./monte-hall.py --games 1000 --doors 100 --p1-always --quiet
Whew. We have played 1000 games.
Alice won 990 prizes and 10 goats for a 99.0% win rate
Bob won 484 prizes and 516 goats for a 48.4% win rate
```

```
$ python ./monte-hall.py --games 1000 --doors 100 --p1-always --quiet
Whew. We have played 1000 games.
Alice won 991 prizes and 9 goats for a 99.1% win rate
Bob won 507 prizes and 493 goats for a 50.7% win rate
```

```
$ python ./monte-hall.py --games 1000 --doors 100 --p1-always --quiet
Whew. We have played 1000 games.
Alice won 983 prizes and 17 goats for a 98.3% win rate
Bob won 490 prizes and 510 goats for a 49.0% win rate
```
