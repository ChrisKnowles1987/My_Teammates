
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


def get_summoner_info():
    summoner_info_url = f'{api_SUMMONER_v4}{name}'
    summoner_info = requests.get(summoner_info_url, headers=headers).json()
    # print(f'summoner info: {summoner_info}')
    return summoner_info

def get_matches(summoner_info):
    summoner_matches_url = f"{api_MATCHES_v5}{summoner_info['puuid']}/ids?type=ranked&start=0&count=20"
    summoner_matches = requests.get(summoner_matches_url, headers = headers).json()
    #print(f'summoner_matches: {summoner_matches}')
    return summoner_matches

def get_summoner_names(summoner_matches): 
    for match in range(len(summoner_matches)):
        req_url = f'{api_MATCH_v5}{summoner_matches[match]}'
        response = requests.get(req_url, headers = headers).json()
        participants = response['info']['participants']
        return [participant['summonerName'] for participant in participants]
        
    

def get_teammates(participants_array):
    
    for participant in participants_array:
        return
        
    
def main():
    summoner_info = get_summoner_info()
    summoner_matches = get_matches(summoner_info)   
    extracted_info = get_summoner_names(summoner_matches)
    print(extracted_info)
    
    
    
if __name__ == '__main__':
    main()