from Team import Team


#data here is on slack
oldScores=[]
teams=[]
for n in ['Netherlands','England','Poland','France','Spain','Croatia','Brazil','Portugal']:
    teams.append(Team(n,0,0,0))
    
day1Wins=[1,0,1,1,0,1,0,0]

for t in teams:
    print(t)

for i in range(len(day1Wins)):
    if day1Wins[i]==1:
        teams[i].addwins()
print()
for t in teams:
    print(t.wins)
    
    
# for i in range(len(teams)):
#     print(f"{teams[i]} has {scores[i]} many points")
# print()
# for i in range(len(teams)):
#     print(f"{teams[i]} has {injuries[i]} injuries")
# print()
# for i in range(len(teams)):
#     print(f"{teams[i]} has {wins[i]} wins")







