from secrets import randbelow
from uuid import uuid4

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
        if randbelow(1) == 1:
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

    def __init__(self, numDoors:int, alwaysSwitchDoors:bool, name:str = None):
        self.numDoors = numDoors
        self.selectedDoor = None
        self.alwaysSwitchDoors = alwaysSwitchDoors
        if name == None:
            self.name = uuid4()
        else:
            self.name = name
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
        return "I am {}, I {} change my door selection, and I have selected {}".format(self.name, changeStr, doorStr)
    #end __repr__


    def selectDoor(self, closedDoors:list = [None, None]) -> bool:
        changedDoor = False
        if closedDoors[0] == None and closedDoors[1] == None:
            # If all doors are closed, we select a random door
            if self.alwaysSwitchDoors or self.selectedDoor == None :
                self.selectedDoor = 1+randbelow(self.numDoors)
                changedDoor = True
        else:
            # If only 2 doors are closed...
            if self.selectedDoor == None:
                # If we haven't previously selected a door, we pick randomly between 2 closed doors
                if randbelow(1) == 1:
                    self.selectedDoor = closedDoors[0]
                else:
                    self.selectedDoor = closedDoors[1]
                changedDoor = True
            elif self.alwaysSwitchDoors:
                # If we've previously selected a door and now only 2 are open, pick the other door
                if self.selectedDoor == closedDoors[0]:
                    self.selectedDoor = closedDoors[1]
                elif self.selectedDoor == closedDoors[1]:
                    self.selectedDoor = closedDoors[0]
                else:
                    raise("Unpossible! I selected door {} but only doors {} and {} are closed!".format(self.selectedDoor, closedDoors[0], closedDoors[1]))
                changedDoor = True
        return changedDoor
    #end selectDoor

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

    numDoors = 100
    numGames = 2

    scorecard = {}
    gameNum=0
    while gameNum < numGames:
        gameNum = gameNum+1

        if gameNum > 1:
            print("")
        print("We are starting game {}! There are {} closed doors".format(gameNum, numDoors))

        h = hall(numDoors)
        print("Don't tell anyone, but the prize is behind door {}".format(h.prizeDoor))

        p1 = player(numDoors, name="Player 1", alwaysSwitchDoors=True)
        #p1 = player(numDoors, alwaysSwitchDoors=True)
        if scorecard.get(p1.name) == None:
            scorecard[p1.name] = { "wins":0, "goats":0}
        p1.selectDoor(closedDoors=h.closedDoors)
        print("p1 = {}".format(p1))
        h.revealDoors(p1.selectedDoor)
        print("All doors have been opened except {} and {}".format(h.closedDoors[0],h.closedDoors[1]))

        p2 = player(numDoors, name="Player 2", alwaysSwitchDoors=True)
        #p2 = player(numDoors, alwaysSwitchDoors=True)
        if scorecard.get(p2.name) == None:
            scorecard[p2.name] = { "wins":0, "goats":0}
        p2.selectDoor(closedDoors=h.closedDoors)
        print("p2 = {}".format(p2))

        p1.selectDoor(closedDoors=h.closedDoors)
        print("p1 = {}".format(p1))

        if p1.selectedDoor == h.prizeDoor:
            scorecard[p1.name]['wins'] = scorecard[p1.name]['wins']+1
            print("p1 {} wins a prize!".format(p1.name))
        else:
            scorecard[p1.name]['goats'] = scorecard[p1.name]['goats']+1
            print("p1 {} receives a goat".format(p1.name))

        if p2.selectedDoor == h.prizeDoor:
            scorecard[p2.name]['wins'] = scorecard[p2.name]['wins']+1
            print("p2 {} wins a prize!".format(p2.name))
        else:
            scorecard[p2.name]['goats'] = scorecard[p2.name]['goats']+1
            print("p2 {} receives a goat".format(p2.name))
    #end while

    print("")
    print("Whew. We have played {} games.".format(numGames))
    print("{} won {} prizes and {} goats".format(scorecard[p1.name],scorecard[p1.name]['wins'],scorecard[p1.name]['goats']))
    print("{} won {} prizes and {} goats".format(scorecard[p2.name],scorecard[p2.name]['wins'],scorecard[p2.name]['goats']))

    return

if __name__ == "__main__":
    main()
