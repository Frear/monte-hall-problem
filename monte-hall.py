from secrets import randbelow
import argparse

class hall:
    """
    Imagine a hall with doors numbered from 1 to numDoors.

    Behind all of them is an empty closet, except there is a prize behind the
    door numbered prizeDoor.

    In roundOne, a door is chosen.
    """

    numDoors:int
    prizeDoor:int
    closedDoors:list
    #r:Random

    def __init__(self, numDoors:int = 3):
        self.numDoors = numDoors
        self.prizeDoor = 1+randbelow(numDoors)
        self.closedDoors = [None, None]
    #end __init__

    def revealDoors(self, playerSelectedDoor:int):
        """
        After the player selects a door, we open all doors except the
        player's selected door and the door with the prize.
        If the player happened to select the door with the prize, we leave
        their door closed and select a random other door to leave closed.
        """

        # We flip a coin to decide if the prize door will be self.closedDoors[0] or [1]
        if randbelow(2) == 1:
            prizeDoorSlot = 0
            emptyDoorSlot = 1
        else:
            prizeDoorSlot = 1
            emptyDoorSlot = 0

        self.closedDoors[prizeDoorSlot] = self.prizeDoor
        if playerSelectedDoor == self.prizeDoor:
            while self.closedDoors[emptyDoorSlot] == None or self.closedDoors[emptyDoorSlot] == self.prizeDoor:
                self.closedDoors[emptyDoorSlot] = 1+randbelow(self.numDoors)
        else:
            self.closedDoors[emptyDoorSlot] = playerSelectedDoor
    #end revealDoors
#end class hall

class player:
    """
    The player in the monte-hall problem is attempting to choose the door with
    the prize
    """

    numDoors:int
    selectedDoor:int
    name:str
    alwaysSwitchDoors:bool
    switchedDoors:bool

    def __init__(self, numDoors:int, alwaysSwitchDoors:bool, name:str):
        self.numDoors = numDoors
        self.selectedDoor = None
        self.alwaysSwitchDoors = alwaysSwitchDoors
        self.name = name
        self.switchedDoors = None
    #end __init__

    def __repr__(self) -> str:
        if self.selectedDoor == None:
            doorStr = "no door yet"
        else:
            doorStr = "door {}".format(self.selectedDoor)
        if self.alwaysSwitchDoors:
            changeStr = "always"
        else:
            changeStr = "never"
        if self.switchedDoors == None:
            switchedStr = "couldn\'t change"
        elif self.switchedDoors:
            switchedStr = "did"
        else:
            switchedStr = "didn\'t"
        return "I am {}, I {} change my door selection, I have selected {}, and I {} change my selection".format(self.name, changeStr, doorStr, switchedStr)
    #end __repr__


    def selectDoor(self, closedDoors:list = [None, None]) -> bool:
        if closedDoors[0] == None and closedDoors[1] == None:
            # If all doors are closed, we select a random door
            if self.alwaysSwitchDoors or self.selectedDoor == None:
                if self.selectedDoor == None:
                    self.switchedDoors = False
                else:
                    self.switchedDoors = True
                self.selectedDoor = 1+randbelow(self.numDoors)
            else:
                self.switchedDoors = False
        else:
            # If only 2 doors are closed...
            if self.selectedDoor == None:
                # If we haven't previously selected a door, we pick randomly between 2 closed doors
                if randbelow(2) == 1:
                    self.selectedDoor = closedDoors[0]
                else:
                    self.selectedDoor = closedDoors[1]
                self.switchedDoors = False
            else:
                if self.alwaysSwitchDoors:
                    # If we've previously selected a door and now only 2 are open, pick the other door
                    if self.selectedDoor == closedDoors[0]:
                        self.selectedDoor = closedDoors[1]
                    elif self.selectedDoor == closedDoors[1]:
                        self.selectedDoor = closedDoors[0]
                    else:
                        raise("Unpossible! I selected door {} but only doors {} and {} are closed!".format(self.selectedDoor, closedDoors[0], closedDoors[1]))
                    self.switchedDoors = True
                else:
                    self.switchedDoors = False
        return self.switchedDoors
    #end selectDoor

def parseargs():
    parser = argparse.ArgumentParser(description='Two players begin the monte hall problem...')
    parser.add_argument('-d', '--doors', dest='numDoors', type=int, default=3,
                        help='Number of doors in the game')
    parser.add_argument('-g', '--games', dest='numGames', type=int, default=1,
                        help='Number of times we play the game')
    parser.add_argument('-q', '--quiet', dest='announceEachGame', action='store_false',
                        help='Don\'t announce details of each game. (default=false)')
    parser.add_argument('-v', '--announceEachGame', dest='announceEachGame', default=True, action='store_true',
                        help='Announce details of each game? (default=true)')

    parser.add_argument('--p1-name', dest='p1name', type=str, default='Alice',
                        help='Player 1\'s name')
    parser.add_argument('--p1-always', dest='p1changes', action='store_true', default=True,
                        help='Player 1 always changes their selection (default=true)')
    parser.add_argument('--p1-never', dest='p1changes', action='store_false',
                        help='Player 1 never changes their selection (default=false)')

    parser.add_argument('--p2-name', dest='p2name', type=str, default='Bob',
                        help='Player 2\'s name')
    parser.add_argument('--p2-always', dest='p2changes', action='store_true', default=True,
                        help='Player 2 always changes their selection (default=true)')
    parser.add_argument('--p2-never', dest='p2changes', action='store_false',
                        help='Player 2 never changes their selection (default=false)')

    return parser.parse_args()

def main():
    """
    Game flow:
        hall is created
        player1 is created
        player1 selects a door
        n-2 doors are opened
        player1 may re-select a door
        player2 is created and selects a door
        the prize door is opened
        wins and losses are tracked
    """

    args = parseargs()

    numDoors = args.numDoors
    numGames = args.numGames
    announceEachGame = args.announceEachGame

    scorecard = {}
    gameNum=0
    while gameNum < numGames:
        gameNum = gameNum+1

        if announceEachGame:
            if gameNum > 1:
                print("")
            print("We are starting game {}! There are {} closed doors".format(gameNum, numDoors))

        h = hall(numDoors)
        if announceEachGame:
            print("Don't tell anyone, but the prize is behind door {}".format(h.prizeDoor))

        p1 = player(numDoors, name=args.p1name, alwaysSwitchDoors=args.p1changes)
        if scorecard.get('p1') == None:
            scorecard['p1'] = {"wins":0, "goats":0}
        p1.selectDoor(closedDoors=h.closedDoors)
        if announceEachGame:
            print("p1 = {}".format(p1))
        h.revealDoors(p1.selectedDoor)
        if announceEachGame:
            print("All doors have been opened except {} and {}".format(h.closedDoors[0],h.closedDoors[1]))

        p2 = player(numDoors, name=args.p2name, alwaysSwitchDoors=args.p2changes)
        if scorecard.get('p2') == None:
            scorecard['p2'] = {"wins":0, "goats":0}
        p2.selectDoor(closedDoors=h.closedDoors)
        if announceEachGame:
            print("p2 = {}".format(p2))

        p1.selectDoor(closedDoors=h.closedDoors)
        if announceEachGame:
            print("p1 = {}".format(p1))

        if p1.selectedDoor == h.prizeDoor:
            scorecard['p1']['wins'] = scorecard['p1']['wins']+1
            if announceEachGame:
                print("p1 {} wins a prize!".format(p1.name))
        else:
            scorecard['p1']['goats'] = scorecard['p1']['goats']+1
            if announceEachGame:
                print("p1 {} receives a goat".format(p1.name))

        if p2.selectedDoor == h.prizeDoor:
            scorecard['p2']['wins'] = scorecard['p2']['wins']+1
            if announceEachGame:
                print("p2 {} wins a prize!".format(p2.name))
        else:
            scorecard['p2']['goats'] = scorecard['p2']['goats']+1
            if announceEachGame:
                print("p2 {} receives a goat".format(p2.name))
    #end while

    print("")
    print("Whew. We have played {} games.".format(numGames))
    print("p1 {} won {} prizes and {} goats".format(scorecard['p1'],scorecard['p1']['wins'],scorecard['p1']['goats']))
    print("p2 {} won {} prizes and {} goats".format(scorecard['p2'],scorecard['p2']['wins'],scorecard['p2']['goats']))

    return

if __name__ == "__main__":
    main()
