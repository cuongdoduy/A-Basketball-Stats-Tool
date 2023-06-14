from constants import TEAMS,PLAYERS
import copy
PlayersData=[]
TeamsData=[]
Teams=[]     
def fetch_data():
    PlayersData=copy.deepcopy(PLAYERS)
    TeamsData=copy.deepcopy(TEAMS)
    return PlayersData,TeamsData

def clean_data(data):
    for player in data:
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
        player['height'] = int(player['height'].split()[0])
        player['guardians'] = player['guardians'].split(' and ')
    return data

def add_player(index,player,Teams,Number_of_team):
    Teams[index]['players'].append(player)
    Teams[index]['Guardians']+=player['guardians']
    if player['experience'] == True:
        Teams[index]['Num of experienced players']+=1 
    else:
        Teams[index]['Num of inexperienced players']+=1
    Teams[index]['Average height']+=player['height']
    if index==Number_of_team-1:
        index=0
    else:
        index+=1
    return Teams,index

def balance_teams(Teams,PlayersData,TeamsData):
    num_players_per_team = len(PlayersData) / len(TeamsData)
    Player_non_experience = []
    for index in range(len(TeamsData)):
        newTeam={'name':'','players':[],'Total players':0,'Num of experienced players':0,'Num of inexperienced players':0,'Average height':0,'Guardians':[]}
        Teams.append(newTeam)
        Teams[index]['name']=TeamsData[index]
        Teams[index]['Total players']=int(num_players_per_team)
    index=0
    for player in PlayersData:
        if player['experience'] == False:
            Player_non_experience.append(player)
        else:
            Teams,index=add_player(index,player,Teams,len(TeamsData))   
    index=0
    for player in Player_non_experience:
        Teams,index=add_player(index,player,Teams,len(TeamsData))
    for team in Teams:
        team['Average height']=round(team['Average height']/len(team['players']),2)
        team['players'].sort(key=lambda x: x['height'])            
    return Teams

def Print_Player(players):
    name=[]
    for player in players:
        name.append(player['name'])
    return (','.join(name))

def Print_Name(data):
    return (','.join(data))

def Print_Stats(Team):
    print(f"Team: {Team['name']} Stats")
    print("--------------------")
    print(f"Total players: {Team['Total players']}")
    print(f"Total experienced: {Team['Num of experienced players']}")
    print(f"Total inexperienced: {Team['Num of inexperienced players']}")
    print(f"Average height: {Team['Average height']}")
    print(f"Players on Team: {Print_Player(Team['players'])}")
    print(f"Guardians: {Print_Name(Team['Guardians'])}")
    print("\n")
    
def start(Teams):
    while True:
        print("BASKETBALL TEAM STATS TOOL")
        print("\n----MENU----\n")
        print("Here are your choices:")
        print("1) Display Team Stats")
        print("2) Quit")
        choice=input("Enter an option: ")
        if choice=='1':
            for index in range(len(Teams)):
                print(index+1,')',Teams[index]['name'])
            choice=input("Enter an option: ")
            Print_Stats(Teams[int(choice)-1])
            print("Press Enter to continue...")
            input()
        else:
            break   

if __name__ == "__main__":
    PlayersData,TeamsData=fetch_data()
    PlayersData=clean_data(PlayersData)
    Teams=balance_teams(Teams,PlayersData,TeamsData)
    start(Teams)
