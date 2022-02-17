
def world_series_coutner():
    text = open('WorldSeriesWinners.txt', 'r')
    team = {}
    
    for line in text:
        line = line.strip()
        words = line.split("\n")
        
        for i in words:
            if i in team:
                team[i] = team[i] + 1
            else:
                team[i] = 1
    print(team)


from ast import Continue
from distutils import text_file
from unittest import skip


def year_won():
    year_input = int(input('Enter a year to see what team won the World Series: '))
    text = open('WorldSeriesWinners.txt', 'r')

    teams = {}

    year = 1903

    for team in text:
        if year == 1904 or year == 1994:
            year += 1
        teams[year] = team
        year += 1
         


    for key, value in teams.items():
       teams[key] = value.rstrip() 


    print(teams[year_input])
    print(teams)
    
    


world_series_coutner()
year_won()


