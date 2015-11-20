import commands


#Use flags to find relevant stat info in file
def total_yards_line():
	line_no=int(commands.getoutput("grep -n '<br />Total Yards</td>' tmp/2000-08-27-penn-state_soup.html | awk -F':' '{print $1}'"))
	return line_no
	
def passing_line():
	line_no=int(commands.getoutput("grep -n '<br />Passing</td>' tmp/2000-08-27-penn-state_soup.html | awk -F':' '{print $1}'"))
	return line_no
	
def rushing_line():
	line_no=int(commands.getoutput("grep -n '<br />Rushing</td>' tmp/2000-08-27-penn-state_soup.html | awk -F':' '{print $1}'"))
	return line_no
	
def first_downs_line():
	line_no=int(commands.getoutput("grep -n '<br />First Downs</td>' tmp/2000-08-27-penn-state_soup.html | awk -F':' '{print $1}'"))
	return line_no
	
def penalties_line():
	line_no=int(commands.getoutput("grep -n '<br />Penalties</td>' tmp/2000-08-27-penn-state_soup.html | awk -F':' '{print $1}'"))
	return line_no
	
def turnovers_line():
	line_no=int(commands.getoutput("grep -n '<br />Turnovers</td>' tmp/2000-08-27-penn-state_soup.html | awk -F':' '{print $1}'"))
	return line_no
	
def teams_line():
	line_no=int(commands.getoutput("grep -n '<table id=\"schools\" class=\"stats_table\">' tmp/2000-08-27-penn-state_soup.html | awk -F':' '{print $1}'"))
	return line_no

"""
print total_yards_line()
print passing_line()
print rushing_line()
print first_downs_line()
print penalties_line()
print turnovers_line()
print teams_line()
"""




"""
class Team(stat):

	def __init__(self, TeamName, Year, Week):
	self.TeamName = TeamName
	self.Year = Year


	def total_yards_line():
		line_no=int(commands.getoutput("grep -n '<br />Total Yards</td>' tmp/2000-08-27-penn-state_soup.html | awk -F':' '{print $1}'"))
		return line_no
		
	def passing_line():
		line_no=int(commands.getoutput("grep -n '<br />Passing</td>' tmp/2000-08-27-penn-state_soup.html | awk -F':' '{print $1}'"))
		return line_no
		
	def rushing_line():
		line_no=int(commands.getoutput("grep -n '<br />Rushing</td>' tmp/2000-08-27-penn-state_soup.html | awk -F':' '{print $1}'"))
		return line_no
		
	def first_downs_line():
		line_no=int(commands.getoutput("grep -n '<br />First Downs</td>' tmp/2000-08-27-penn-state_soup.html | awk -F':' '{print $1}'"))
		return line_no
		
	def penalties_line():
		line_no=int(commands.getoutput("grep -n '<br />Penalties</td>' tmp/2000-08-27-penn-state_soup.html | awk -F':' '{print $1}'"))
		return line_no
		
	def turnovers_line():
		line_no=int(commands.getoutput("grep -n '<br />Turnovers</td>' tmp/2000-08-27-penn-state_soup.html | awk -F':' '{print $1}'"))
		return line_no
		
	def teams_line():
		line_no=int(commands.getoutput("grep -n '<table id=\"schools\" class=\"stats_table\">' tmp/2000-08-27-penn-state_soup.html | awk -F':' '{print $1}'"))
		return line_no

"""





#stats=["total_yards_line()", "passing_line()", "rushing_line", "first_downs_line()", "penalties_line()", "turnovers_line()", "teams_line"]

#Use line numbers to get values

away_yards=commands.getoutput(''.join("awk 'NR==" + str(total_yards_line()+2) + "' tmp/2000-08-27-penn-state_soup.html")).split(">")[1].strip("</th></div>")
print away_yards

home_yards=commands.getoutput(''.join("awk 'NR==" + str(total_yards_line()+4) + "' tmp/2000-08-27-penn-state_soup.html")).split(">")[1].strip("</th></div>")
print home_yards

away_passing=commands.getoutput(''.join("awk 'NR==" + str(passing_line()+2) + "' tmp/2000-08-27-penn-state_soup.html")).split(">")[1].strip("</td>")
print away_passing

home_passing=commands.getoutput(''.join("awk 'NR==" + str(passing_line()+4) + "' tmp/2000-08-27-penn-state_soup.html")).split(">")[1].strip("</td>")
print home_passing

away_rushing=commands.getoutput(''.join("awk 'NR==" + str(rushing_line()+2) + "' tmp/2000-08-27-penn-state_soup.html")).split(">")[1].strip("</td>")
print away_rushing

home_rushing=commands.getoutput(''.join("awk 'NR==" + str(rushing_line()+4) + "' tmp/2000-08-27-penn-state_soup.html")).split(">")[1].strip("</td>")
print home_rushing

away_first_downs=commands.getoutput(''.join("awk 'NR==" + str(first_downs_line()+2) + "' tmp/2000-08-27-penn-state_soup.html")).split(">")[1].strip("</td>")
print away_first_downs

home_first_downs=commands.getoutput(''.join("awk 'NR==" + str(first_downs_line()+4) + "' tmp/2000-08-27-penn-state_soup.html")).split(">")[1].strip("</td>")
print home_first_downs

away_penalties=commands.getoutput(''.join("awk 'NR==" + str(penalties_line()+2) + "' tmp/2000-08-27-penn-state_soup.html")).split(">")[1].strip("</td>")
print away_penalties

home_penalties=commands.getoutput(''.join("awk 'NR==" + str(penalties_line()+4) + "' tmp/2000-08-27-penn-state_soup.html")).split(">")[1].strip("</td>")
print home_penalties

away_turnovers=commands.getoutput(''.join("awk 'NR==" + str(turnovers_line()+2) + "' tmp/2000-08-27-penn-state_soup.html")).split(">")[1].strip("</td>")
print away_turnovers

home_turnovers=commands.getoutput(''.join("awk 'NR==" + str(turnovers_line()+4) + "' tmp/2000-08-27-penn-state_soup.html")).split(">")[1].strip("</td>")
print home_turnovers


away_team=commands.getoutput(''.join("awk 'NR==" + str(teams_line()+1) + "' tmp/2000-08-27-penn-state_soup.html")).split("</th>")[1].strip("<th>")
home_team=commands.getoutput(''.join("awk 'NR==" + str(teams_line()+1) + "' tmp/2000-08-27-penn-state_soup.html")).split("</th>")[2].strip("<th>")





print away_team
print home_team
print home_first_downs
