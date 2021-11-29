#Adventure Quest

#the play variable is to keep track if game is over
play = True
#this keeps track if player went back, or if first time through
firstTime = True
stillAlive = True
#make empty list of player possesions
stuff = []
hasTorch = False
#turn all the room selections off to start with except room0
room0 = True
room1 = False
room2 = False

#while play is true you can keep moving to different rooms
while(play):
  #room zero is the outside of the dungeon
  while(room0 and stillAlive):
    print ("You are standing in front of a door.")
    print ("Do you open the door? y n")
    ans = raw_input()
    if ans == 'y':
      if firstTime:
        print ("A hand reaches out and drags you into the dungeon.")
      else:
        print ('You open the door and enter the dungeon')
      #enter room 1
      room1 = True
    else:
      #any other answer is assumed no
      print ("you walk away and live a long and boring life.")
      #leave the game
      play = False
    #leave the room
    room0 = False
      
  #setup and start room1 (head of tunnel)
  #keeps track of if the player looked in this room
  looked1 = False
  #set up a list of actions to choose from
  choice1 = ['look', 'leave']
  while(room1 and stillAlive):
    print ("What do you do?")
    ans = raw_input()
    #run through a series of if statements to test user responce
    if ans == 'leave':
      #this takes the player back outside
      room1 = False
      room0 = True
    elif ans == 'look':
      print ('')
      print ('You are standing in a tunnel carved into the rock.')
      print ('It looks like an old mine with thick rotten logs supporting the roof.')
      if(not hasTorch):
        print ('There is a torch on the wall lighting the area you are in.')
      print ('The tunnel in front of you stretches into darkness...')
      if(firstTime):
        print ('You look down and see the bones of a skeleton arm that was holding your shirt fall to the floor and turn to dust.')
        #so this only happens first time through
        firstTime = False
      #now that player has looked, they get extra choices added
      if not looked1:
        choice1.append('take torch')
        choice1.append('walk down tunnel')
        looked1 = True
    elif ans == 'take torch' and looked1 and not hasTorch:
      print ('')
      print ('You are carrying a torch')
      #put a torch into players stuff list
      stuff.append('torch')
      #remove that choice from room1 action list
      choice1.remove('take torch')
      #add this choice
      choice1.append('drop torch')
      hasTorch = True
    elif ans == 'drop torch' and looked1 and hasTorch:
      print ('')
      print ('You put the torch back on the wall where it continues to burn.')
      stuff.remove('torch')
      choice1.remove('drop torch')
      choice1.append('take torch')
      hasTorch = False
    elif ans == 'walk down tunnel':
      print ('')
      print ('You walk down the tunnel')
      #based on this, walking down the tunnel is safe or not
      if hasTorch:
        print ('')
        print ('You see a bottomless pit that you carefully move past.')
        print ('You continue walking until you reach the end of the tunnel.')
        #end of the tunnel is considered room2, so leave room1
        room1 = False
        room2 = True
      else:
        print ('')
        print ('In the dark you stumble into a bottomless pit.')
        print ('After falling for about 3 hours you discover that the pit does have a bottom.')
        print ('The End')
        #and to exit the game
        room1 = False
        stillAlive = False
        play = False
    else:
      #no valid choice was detected for room1 so loop back to the start of room1
      print ('Your choices are:', choice1)
  
  #setup and start room2 (end of tunnel)
  choice2 = ['look', 'go back']
  looked2 = False
  while(room2 and stillAlive):
    print ('What do you do?')
    ans = raw_input()
    if ans == 'look':
      print ('')
      print ('*** description of end of tunnel goes here ***')
      #choice2.append('open gate')
      looked2 = True
    elif ans == 'go back':
      print ('')
      print ('You head back to the tunnel entrance.')
      #so program can exit room2 while loop and enter room1 loop
      room2 = False
      room1 = True
    else:
      #no valid choice was detected for room2 so loop back to the start of room2
      print ('Your choices are:', choice2)
      
#this happens if player is not alive when game ends
print ('')
if not stillAlive:   
  print ('Even though you perished you vow to return some day')
raw_input("good by")