import commands
import glob
import datetime

#Need to clean this up... a lot. But it's running.

# What this script needs to do:
#   Open box score, determine week from date (filename)
#   Find team in box score file, grab stats for team, put in a list
#   stat_line=''.join(team, stats)
#   command = ''.join("sed -i s|" + team + ",|" + stat_line + "|g ")
#   

stats=["Total Yards", "Passing", "Rushing", "First Downs", "Penalties", "Turnovers"]
years=["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"]

def get_away_team():
	line_no=int(commands.getoutput("grep -n '<table id=\"schools\" class=\"stats_table\">' " + filename + " | awk -F':' '{print $1}'"))
	away_team=commands.getoutput(''.join("awk 'NR==" + str(line_no+1) + "' " + filename)).split("</th>")[1]
	return away_team[4:]
	
def get_home_team():
	line_no=int(commands.getoutput("grep -n '<table id=\"schools\" class=\"stats_table\">' " + filename + " | awk -F':' '{print $1}'"))
	home_team=commands.getoutput(''.join("awk 'NR==" + str(line_no+1) + "' " + filename)).split("</th>")[2]
	return home_team[4:]

def get_line(stat):
	line_no=int(commands.getoutput(''.join("grep -n '<br />" + stat + "</td>' " + filename + " | awk -F':' '{print $1}'")))
	return line_no
	
def away_stat(stat):
	stat_line=get_line(stat) + 2
	stat_value=commands.getoutput(''.join("awk 'NR==" + str(stat_line) + "' " + filename)).split(">")[1].strip("</th></div>")
	return stat_value

def home_stat(stat):
	stat_line=get_line(stat) + 4
	stat_value=commands.getoutput(''.join("awk 'NR==" + str(stat_line) + "' " + filename)).split(">")[1].strip("</th></div>")
	return stat_value
	
def get_week(filename):
	month = int(filename.split("-")[1])
	day = int(filename.split("-")[2])
	return datetime.datetime(int(year), month, day).weekday()	

for year in years:
	week = 1
	counter = 0	
	for filename in glob.glob(year + "/*_soup.html"):
		weekly_stats=[]
	
		try:
			with open(filename, 'r') as f:
				print filename
				if int(get_week(filename)) < int(counter):
					week += 1
				counter = int(get_week(filename))
				weekly_stats.append(get_away_team())
				for stat in stats:
					weekly_stats.append(away_stat(stat))
		except ValueError:
			continue
			
		
		database_file=''.join(year + "/week_" + str(week) + "_" + year + ".csv")
		team_and_conf=commands.getoutput("grep '^" + weekly_stats[0] + ",' " + database_file) 
		stat_line=''.join(team_and_conf + ','.join([str(stat) for stat in weekly_stats[1:]]))
		print stat_line
		insert_command=''.join("sed -i 's|" + team_and_conf + "|" + stat_line + ",|g' " + database_file)
		commands.getoutput(insert_command)
		weekly_stats=[]
		try:
			with open(filename, 'r') as f:
				print filename
				if int(get_week(filename)) < int(counter):
					week += 1
				counter = int(get_week(filename))
				weekly_stats.append(get_home_team())
				for stat in stats:
					weekly_stats.append(home_stat(stat))
		except ValueError:
			continue
					
		database_file=''.join(year + "/week_" + str(week) + "_" + year + ".csv")
		team_and_conf=commands.getoutput("grep '^" + weekly_stats[0] + ",' " + database_file) 
		stat_line=''.join(team_and_conf + ','.join([str(stat) for stat in weekly_stats[1:]]))
		print stat_line
		insert_command=''.join("sed -i 's|" + team_and_conf + "|" + stat_line + ",|g' " + database_file)
		commands.getoutput(insert_command)

