
def getNames(FILENAME):
    #open the file
    file1 = open(FILENAME,"r")
    
    #loop through each line of the file
    names=[]
    for line in file1:
        index=0
        leaderName=""
        while (line[index]!=","):
            leaderName+=line[index]
            index+=1  
        names.append(leaderName)
    #return that information
    return names

# print(getNames("Database.txt"))


def getScores(FILENAME):
        #open the file
    file1 = open(FILENAME,"r")
    
    #loop through each line of the file
    scores=[]
    for line in file1:
        index=0
        leaderScore=""
        
        while(line[index]!=","):
            index+=1
        index+=1
        
        while (line[index]!="\n"):
            leaderScore+=line[index]
            index+=1  
        scores.append(leaderScore)
    #return that information
    return scores

# print(getScores("Database.txt"))

#not the best habit
def updateLeaderBoard(FILENAME,leaderNames,leaderScores,playerName,playerScore):
    index=0
    while (index<len(leaderScores)):
        #check if score can be inseted in this position
        if(playerScore>=int(leaderScores[index])):
            break
        else:
            index+=1
    #insert player info
    leaderNames.insert(index,playerName)
    leaderScores.insert(index,playerScore)

    if (len(leaderNames)>5):#ensure only 5 players on leaderboard
        leaderNames.pop()
        leaderScores.pop()
        
    #resave to the leaderboard
    file1=open(FILENAME,"w")

    #loop through the lists and save ache list to the file
    for i in range(len(leaderNames)):
        file1.write(f"{leaderNames[i]},{leaderScores[i]}\n")
    file1.close()
        

# draw leaderboard and display a message to player
def draw_leaderboard(high_scorer, leader_names, leader_scores, turtle_object, player_score):
  #high_scorer is a boolean to tell if the current user is a high_scorer
  
  # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
  font_setup = ("Arial", 20, "normal")
  turtle_object.clear()
  turtle_object.penup()
  turtle_object.goto(-160,100)
  turtle_object.hideturtle()
  turtle_object.down()
  
  index = 0
  # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
  while (index < len(leader_scores)):
    turtle_object.write(str(index + 1) + "\t" + leader_names[index] + "\t" + str(leader_scores[index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-160,int(turtle_object.ycor())-50)
    turtle_object.down()
    index = index + 1
  #TODO: Display message about player making the leaderBoard or not
  
  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()
  
  # move turtle to a new line
  turtle_object.penup()
  turtle_object.goto(-160,int(turtle_object.ycor())-50)
  turtle_object.pendown()

  #display gold silver bronze
  gold=leader_scores[0]
  silver=leader_scores[1]
  bronze=leader_scores[2]
  if int(player_score)>=int(gold):
      turtle_object.write("you earned  gold medal!",font=("Comic Sans",10,"bold"))
  elif int(player_score)>=int(silver):
    turtle_object("you earned a silver medal!",font=("Comic Sans",10,"bold"))
  elif int(player_score)>=int(bronze):
    turtle_object("you earned a bronze medal!",font=("Comic Sans",10,"bold"))