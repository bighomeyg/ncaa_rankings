import commands

stats=["Total Yards", "Passing", "Rushing", "First Downs", "Penalties", "Turnovers"]

def get_away_team():
	line_no=int(commands.getoutput("grep -n '<table id=\"schools\" class=\"stats_table\">' tmp/2000-08-27-penn-state_soup.html | awk -F':' '{print $1}'"))
	away_team=commands.getoutput(''.join("awk 'NR==" + str(line_no+1) + "' tmp/2000-08-27-penn-state_soup.html")).split("</th>")[1].strip("<th>")
	return away_team
	
def get_home_team():
	line_no=int(commands.getoutput("grep -n '<table id=\"schools\" class=\"stats_table\">' tmp/2000-08-27-penn-state_soup.html | awk -F':' '{print $1}'"))
	home_team=commands.getoutput(''.join("awk 'NR==" + str(line_no+1) + "' tmp/2000-08-27-penn-state_soup.html")).split("</th>")[2].strip("<th>")
	return home_team

def get_line(stat):
	line_no=int(commands.getoutput(''.join("grep -n '<br />" + stat + "</td>' tmp/2000-08-27-penn-state_soup.html | awk -F':' '{print $1}'")))
	return line_no
	
def away_stat(stat):
	stat_line=get_line(stat) + 2
	stat_value=commands.getoutput(''.join("awk 'NR==" + str(stat_line) + "' tmp/2000-08-27-penn-state_soup.html")).split(">")[1].strip("</th></div>")
	return stat_value

def home_stat(stat):
	stat_line=get_line(stat) + 4
	stat_value=commands.getoutput(''.join("awk 'NR==" + str(stat_line) + "' tmp/2000-08-27-penn-state_soup.html")).split(">")[1].strip("</th></div>")
	return stat_value


print get_home_team()
for stat in stats:
	print stat, home_stat(stat)
	

print get_away_team()
for stat in stats:
	print stat, away_stat(stat)


