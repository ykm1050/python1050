'''
Problem 156: Sports Tournament Scheduler POC:
• CRUD: Tournament data - class Tournament & class Team CRUD operations.
• Team Details , Player details , Match Schedulling & Venue of the match.
• stored in FILE - [.csv , .txt , .json]

'''

class Team:
    def __init__(self, team_id, name, players):
        self.team_id = team_id
        self.name = name
        self.players = players

class Match:
    def __init__(self, match_id, team1_id, team2_id, date, venue):
        self.match_id = match_id
        self.team1_id = team1_id
        self.team2_id = team2_id
        self.date = date
        self.venue = venue

class Tournament:
    def __init__(self, tournament_id, name):
        self.tournament_id = tournament_id
        self.name = name
        self.teams = []
        self.matches = []

    def add_team(self, team):
        self.teams.append(team)

    def add_match(self, match):
        self.matches.append(match)

    def get_team(self, team_id):
        for team in self.teams:
            if team.team_id == team_id:
                return team
        return None

    def update_team(self, team_id, new_name, new_players):
        team = self.get_team(team_id)
        if team:
            team.name = new_name
            team.players = new_players
            return True
        return False

    def delete_team(self, team_id):
        team = self.get_team(team_id)
        if team:
            self.teams.remove(team)
            return True
        return False

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(f'Tournament - Indian Premier League 2024\n\n\n')
            for team in self.teams:
                file.write(f"Team ID- {team.team_id} , {'Team Name -'} {team.name} , {'Players -'} {' , '.join(team.players)}\n\n")
            file.write(f'\nIPL 2024 Match Fixtures - 12 + 2 matches\n\n')
            for match in self.matches:
                file.write(f"Match ID - {match.match_id} , {'Team ID -'} {match.team1_id}  {'vs'}  {match.team2_id}  {'scheduled on',match.date} {'Venue -'} {match.venue}\n\n")
            file.write(f'{'IPL 2024 Winner - Royal challengers Bengaluru\n'}')

def main():
    tournament = Tournament(tournament_id=1, name="Indian Premier League 2024")

    team1 = Team(team_id='RCB', name="Royal Challengers Bengaluru\n",players=["Virat Kohli (c)", "Will Jacks" , 'Faf Du Plessis' , 'Maxwell' , 'C Green' , 'D Karthik' , 'Md Siraj' ])
    team2 = Team(team_id='GT', name="Gujarat Titans\n",players=["Shubman Gill (c)", "Sai Sudarshan" , 'W Saha' , 'Rashid khan' , 'Khen Williamson' , 'Mohit Sharma' , 'Noor' ])
    team3 = Team(team_id='CSK', name="Chennai Super Kings\n",players=["MS Dhoni (c)", "R Ravindra" , 'Ruturaj Gaikwad' , 'M Ali' , 'R Jadeja' , 'M Patheerana' , 'Daryl Mitchell' ])
    team4 = Team(team_id='MI', name="Mumbai Indians\n",players=["Rohit Sharma (c)", "Ishan Kishan" , 'Hardhik Pandya' , 'S K Yadav' , 'J Bumrah' , 'Coetzee' , 'Tilak Varma' ])

    match1 = Match(match_id='1 of 14', team1_id='RCB', team2_id='GT', date="01-05-2024" , venue='Chinnaswamy stadium')
    match2 = Match(match_id='2 of 14', team1_id='GT', team2_id='CSK', date="02-05-2024" , venue='M A Chidambaram stadium')
    match3 = Match(match_id='3 of 14', team1_id='CSK', team2_id='MI', date="03-05-2024" , venue='Wankhede stadium')
    match4 = Match(match_id='4 of 14', team1_id='MI', team2_id='RCB', date="04-05-2024" , venue='Chinnaswamy stadium')
    match5 = Match(match_id='5 of 14', team1_id='RCB', team2_id='CSK', date="05-05-2024" , venue='M A Chidambaram stadium')
    match6 = Match(match_id='6 of 14', team1_id='GT', team2_id='MI', date="06-05-2024" , venue='Wankhede stadium')
    match7 = Match(match_id='7 of 14', team1_id='CSK', team2_id='RCB', date="07-05-2024" , venue='chinnaswamy stadium')
    match8 = Match(match_id='8 of 14', team1_id='MI', team2_id='GT', date="08-05-2024" , venue='Eden Gardens stadium')
    match9 = Match(match_id='9 of 14', team1_id='RCB', team2_id='MI', date="09-05-2024" , venue='Arun Jaitley stadium')
    match10 = Match(match_id='10 of 14', team1_id='GT', team2_id='RCB', date="10-05-2024" , venue='Dharmashala stadium')
    match11 = Match(match_id='11 of 14', team1_id='CSK', team2_id='GT', date="11-05-2024" , venue='Rajiv Gandhi stadium')
    match12 = Match(match_id='12 of 14', team1_id='MI', team2_id='RCB', date="12-05-2024" , venue='chinnaswamy stadium')
    match13 = Match(match_id='PlayOffs', team1_id='RCB', team2_id='GT', date="14-05-2024" , venue='M A Chidambaram stadium')
    match14 = Match(match_id='FINALS', team1_id='RCB', team2_id='GT', date="17-05-2024" , venue='Narendra Modi stadium')

    tournament.add_team(team1)
    tournament.add_team(team2)
    tournament.add_team(team3)
    tournament.add_team(team4)

    tournament.add_match(match1)
    tournament.add_match(match2)
    tournament.add_match(match3)
    tournament.add_match(match4)
    tournament.add_match(match5)
    tournament.add_match(match6)
    tournament.add_match(match7)
    tournament.add_match(match8)
    tournament.add_match(match9)
    tournament.add_match(match10)
    tournament.add_match(match11)
    tournament.add_match(match12)
    tournament.add_match(match13)
    tournament.add_match(match14)

    
    tournament.save_to_file("tournament_data.csv")
    tournament.save_to_file('tournament_data.txt')
    tournament.save_to_file('tournament_data.json')
    

if __name__ == "__main__":
    main()



'''
OUTPUT ----------------------------------------------------------------------------------------------------------------
stored in .csv , .txt , .json files.

Tournament - Indian Premier League 2024


Team ID- RCB , Team Name - Royal Challengers Bengaluru
 , Players - Virat Kohli (c) , Will Jacks , Faf Du Plessis , Maxwell , C Green , D Karthik , Md Siraj

Team ID- GT , Team Name - Gujarat Titans
 , Players - Shubman Gill (c) , Sai Sudarshan , W Saha , Rashid khan , Khen Williamson , Mohit Sharma , Noor

Team ID- CSK , Team Name - Chennai Super Kings
 , Players - MS Dhoni (c) , R Ravindra , Ruturaj Gaikwad , M Ali , R Jadeja , M Patheerana , Daryl Mitchell

Team ID- MI , Team Name - Mumbai Indians
 , Players - Rohit Sharma (c) , Ishan Kishan , Hardhik Pandya , S K Yadav , J Bumrah , Coetzee , Tilak Varma



IPL 2024 Match Fixtures - 12 + 2 matches

Match ID - 1 of 14 , Team ID - RCB  vs  GT  ('scheduled on', '01-05-2024') Venue - Chinnaswamy stadium

Match ID - 2 of 14 , Team ID - GT  vs  CSK  ('scheduled on', '02-05-2024') Venue - M A Chidambaram stadium

Match ID - 3 of 14 , Team ID - CSK  vs  MI  ('scheduled on', '03-05-2024') Venue - Wankhede stadium

Match ID - 4 of 14 , Team ID - MI  vs  RCB  ('scheduled on', '04-05-2024') Venue - Chinnaswamy stadium

Match ID - 5 of 14 , Team ID - RCB  vs  CSK  ('scheduled on', '05-05-2024') Venue - M A Chidambaram stadium

Match ID - 6 of 14 , Team ID - GT  vs  MI  ('scheduled on', '06-05-2024') Venue - Wankhede stadium

Match ID - 7 of 14 , Team ID - CSK  vs  RCB  ('scheduled on', '07-05-2024') Venue - chinnaswamy stadium

Match ID - 8 of 14 , Team ID - MI  vs  GT  ('scheduled on', '08-05-2024') Venue - Eden Gardens stadium

Match ID - 9 of 14 , Team ID - RCB  vs  MI  ('scheduled on', '09-05-2024') Venue - Arun Jaitley stadium

Match ID - 10 of 14 , Team ID - GT  vs  RCB  ('scheduled on', '10-05-2024') Venue - Dharmashala stadium

Match ID - 11 of 14 , Team ID - CSK  vs  GT  ('scheduled on', '11-05-2024') Venue - Rajiv Gandhi stadium

Match ID - 12 of 14 , Team ID - MI  vs  RCB  ('scheduled on', '12-05-2024') Venue - chinnaswamy stadium

Match ID - PlayOffs , Team ID - RCB  vs  GT  ('scheduled on', '14-05-2024') Venue - M A Chidambaram stadium

Match ID - FINALS , Team ID - RCB  vs  GT  ('scheduled on', '17-05-2024') Venue - Narendra Modi stadium


IPL 2024 Winner - Royal challengers Bengaluru

'''