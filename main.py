'''
This part of the project is complete, dom reccomends writing this script in 
javascript and using express js

TODO
look into expressJS
write hello world with extressJS and node
make repo and call it 'TeamDiff'and push hello world
make html css for UI
'''


import requests
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access API key
api_key = os.getenv('API_KEY')
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": f"{api_key}"}

name = 'ChrisK1987'
api_SUMMONER_v4 = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
api_MATCHES_v5 = 'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/'
api_MATCH_v5 = 'https://europe.api.riotgames.com/lol/match/v5/matches/'
api_LEAGUE_v4= 'https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/'


def get_summoner_info():
    summoner_info_url = f'{api_SUMMONER_v4}{name}'
    summoner_info = requests.get(summoner_info_url, headers=headers).json()
    return summoner_info

def get_matches(summoner_info):
    summoner_matches_url = f"{api_MATCHES_v5}{summoner_info['puuid']}/ids?type=ranked&start=0&count=20"
    summoner_matches = requests.get(summoner_matches_url, headers = headers).json()
    return summoner_matches

def get_participants(summoner_matches):
    summoner_names = []
    for match in range(len(summoner_matches)):
        req_url = f'{api_MATCH_v5}{summoner_matches[match]}'
        response = requests.get(req_url, headers = headers).json()
        teamId = get_team_id(response['info']['participants'])
        summoner_names.append(get_teammates_with_matching_id(response['info']['participants'],teamId))
    return summoner_names
    
def get_team_id(participants):
     for participant in participants:
        if participant['summonerName'] == name:
            return participant['teamId']
 
def get_teammates_with_matching_id(participants, teamId):
    team_array = []
    for participant in participants:
        if (participant['teamId'] == teamId) and (participant['summonerName'] != name):
            team_array.append(participant['summonerId'])
    return team_array

def get_winrate(participants, queue_type): # 'RANKED_SOLO_5x5' or 'RANKED_FLEX_SR'
    winrates ={}
    for match in participants:
        for player in match:
            req_url=f'{api_LEAGUE_v4}{player}'
            response = requests.get(req_url,headers=headers).json()
            for item in response:
                if item.get('queueType') == queue_type: 
                    summonerName = item.get('summonerName')                 
                    wins = item.get('wins',0)
                    losses = item.get('losses', 0)
                    total_games = wins + losses
                    if total_games > 0:
                        winrate = f'{round(((wins / total_games)*100),1)} %'
                        winrates[summonerName] = winrate
                    else:
                        winrates.append(0)  # Append 0 if no games played
                else:
                    continue        
                        
    return winrates
    
def main():
    print('running...')
    summoner_info = get_summoner_info()
    summoner_matches = get_matches(summoner_info)   
    participants = get_participants(summoner_matches)
    winrates = get_winrate(participants,'RANKED_SOLO_5x5' )# 'RANKED_SOLO_5x5' or 'RANKED_FLEX_SR'
    print(winrates)
    
if __name__ == '__main__':
    main()