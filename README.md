# My_Teammates

### An application that uses the RIOT API to pull game / player information and calculate the average win-rate of a given summoners teammates over x games.  Potentially has a leaderboard so users can enter their summoner name and compete for thre worst teammates against their friends.  Who is really hard stuck?   how has the carry pants?  lets find out!

## Breakdown

- Use RIOT API to determine a users teammates from the past x games
- Check each teammates win rate  over x games 
- Aggregate teammates win-rate and show user
- UI for entering summoner ID and viewing results
- Make a leaderboard of users who have entered their summoner IDs
 -Will require persistence of user input in a database

## Tech stack

- Starting with Jupyter notebooks to try and understand the RIOT API
- Python scripts to understand the api calls and manipulations
- will re write in javascript and use express js in a different repo
