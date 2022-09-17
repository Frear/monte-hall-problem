# The monte-hall problem
This program plays the [monte-hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem).

It has a variation on how the game is played.

Normally, a player (p1) selects a door in hops of finding a prize.
After they make their selection, all doors are opened except the door they selected and door with the prize.
The player is offered the ability to change their answer.

At this point, our variation is we also introduce a new player (p2) who can select from either of the unopened doors.

Then, the door with the prize is revealed and the players who selected the door with the prize win
and the players who selected a door without the prize receive a goat.

## CLI usage
```
usage: monte-hall.py [-h] [-d NUMDOORS] [-g NUMGAMES] [-q] [-v]
                     [--p1-name P1NAME] [--p1-always] [--p1-never]
                     [--p2-name P2NAME] [--p2-always] [--p2-never]

Two players begin the monte hall problem...

optional arguments:
  -h, --help            show this help message and exit
  -d NUMDOORS, --doors NUMDOORS
                        Number of doors in the game
  -g NUMGAMES, --games NUMGAMES
                        Number of times we play the game
  -q, --quiet           Don't announce details of each game. (default=false)
  -v, --announceEachGame
                        Announce details of each game? (default=true)
  --p1-name P1NAME      Player 1's name
  --p1-always           Player 1 always changes their selection (default=true)
  --p1-never            Player 1 never changes their selection (default=false)
  --p2-name P2NAME      Player 2's name
  --p2-always           Player 2 always changes their selection (default=true)
  --p2-never            Player 2 never changes their selection (default=false)
```


## Player 1 never changes their answer
Three sample runs of 1000 games each with 100 doors:
```
$ python ./monte-hall.py -g 1000 -d 100 --p1-never -q
Whew. We have played 1000 games.
p1 {'wins': 5, 'goats': 995} won 5 prizes and 995 goats for a 0.5% win rate
p2 {'wins': 481, 'goats': 519} won 481 prizes and 519 goats for a 48.1% win rate
```

```
$ python ./monte-hall.py -g 1000 -d 100 --p1-never -q
Whew. We have played 1000 games.
p1 {'wins': 9, 'goats': 991} won 9 prizes and 991 goats for a 0.9% win rate
p2 {'wins': 511, 'goats': 489} won 511 prizes and 489 goats for a 51.1% win rate
```

```
$ python ./monte-hall.py -g 1000 -d 100 --p1-never -q
Whew. We have played 1000 games.
p1 {'wins': 10, 'goats': 990} won 10 prizes and 990 goats for a 1.0% win rate
p2 {'wins': 477, 'goats': 523} won 477 prizes and 523 goats for a 47.7% win rate
```

## Player 1 always changes their answer
Three sample runs of 1000 games each with 100 doors:
```
$ python ./monte-hall.py -g 1000 -d 100 --p1-always -q
Whew. We have played 1000 games.
p1 {'wins': 989, 'goats': 11} won 989 prizes and 11 goats for a 98.9% win rate
p2 {'wins': 519, 'goats': 481} won 519 prizes and 481 goats for a 51.9% win rate
```

```
$ python ./monte-hall.py -g 1000 -d 100 --p1-always -q
Whew. We have played 1000 games.
p1 {'wins': 987, 'goats': 13} won 987 prizes and 13 goats for a 98.7% win rate
p2 {'wins': 498, 'goats': 502} won 498 prizes and 502 goats for a 49.8% win rate
```

```
$ python ./monte-hall.py -g 1000 -d 100 --p1-always -q
Whew. We have played 1000 games.
p1 {'wins': 990, 'goats': 10} won 990 prizes and 10 goats for a 99.0% win rate
p2 {'wins': 492, 'goats': 508} won 492 prizes and 508 goats for a 49.2% win rate
```
