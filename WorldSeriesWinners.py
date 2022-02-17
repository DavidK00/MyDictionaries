
# # def world_series_coutner():
# #     text = open('WorldSeriesWinners.txt', 'r')
# #     team = {}
    
# #     for line in text:
# #         line = line.strip()
# #         line = line.lower()
# #         words = line.split("\n")
        
# #         for i in words:
# #             if i in team:
# #                 team[i] = team[i] + 1
# #             else:
# #                 team[i] = 1
# #     print(team)

from unittest import skip


def year_won():
    year_input = int(input('Enter a year to see what team won the World Series: '))
    text = open('WorldSeriesWinners.txt', 'r')
    year = {}

    starter_year = 1903
    

    for i in range(starter_year,2009):
        if i != 1904  or i != 1994:
            for row in text:
                year[starter_year] = row
                starter_year += 1
        else:
            skip

            
            
        
        
    for key, value in year.items():
        year[key] = value.rstrip() 

    year[1904] = 'Not Played'     
    year[1994] = 'Not Played'

    print(year[year_input])
    print(year)
    
    


#world_series_coutner()
year_won()