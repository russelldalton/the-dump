"""
Introduction to Data Structures, Spring 2023, UMA

Program: ESPN.py
Author: jobe odulio
Date Created: 3/3/2023
Description:this program tracks all players from the patriots 

"""

class Player():
    """ implement a Player class which allows us to track the details
        about each individual player (an instance of the class) """

    def __init__(self, first, last, position ):
        self.first = first
        self.last = last
        self.position = position

    def __str__(self):
        return self.first, self.last, self.position
        

    ''' think about what other methods you might need.  add them here '''

class Team():
    """ """
    def __init__(self, teamName):
        self.teamName = teamName
        self.player = []
        

        
        
        """ Create an instance of Team.   Note that the team name is
            passed as a parameter and should be stored as an instance
            variable.   You will also need an instance variable which
            serves as the container for the istances of Player """
    
        

    def addPlayer(self, first, last, position):
        """ Create an instance of your Player class and add it to the team container """
        if isinstance(first, Player):
            self.player.append(first)
        if isinstance(last, Player):
            self.player.append(last)
        if isinstance(position, Player):
            self.player.append(position)
        
        

        
        
        
        
   
           
        
   # def removePlayer(self, first, last, position):
        """ You are given just a player's first & last name.  Find the specified
        player in the team container and remove that instance """
       # if Team.removePlayer == True:
          #  self.player = False
           # return False
        
            
    def listPlayers(self):
        """ List all the players on the team.  Your output should be nicely formatted
            and the team name should be printed as a header"""
        print(self.teamName)
        for player in self.player:
            player.__str__()
        
        
        
        

def main():
    """ A simple test of the class

        A correct program will create output like this:

        Current Patriots players:
             Mac Jones, Quarterback
             Matthew Slater, Special Teams
             Jonnu Smith, Tight End
             JJ Taylor, Running Back
             Matthew Judon, Linebacker

        Current Patriots players:
             Mac Jones, Quarterback
             Matthew Slater, Special Teams
             Jonnu Smith, Tight End
             Matthew Judon, Linebacker
    """

    # Note: we pass the team name when we create an instance of Team
    patriots = Team('Patriots')
    
    patriots.addPlayer("Mac", "Jones", "Quarterback")
    patriots.addPlayer("Matthew", "Slater", "Special Teams")
    patriots.addPlayer("Jonnu", "Smith", "Tight End")
    patriots.addPlayer("JJ", "Taylor", "Running Back")
    patriots.addPlayer("Matthew", "Judon", "Linebacker")    
    patriots.listPlayers()

    # now we remove one of the players
    #patriots.removePlayer("JJ", "Taylor", "bruh")

    print()
    patriots.listPlayers()
    

main()
