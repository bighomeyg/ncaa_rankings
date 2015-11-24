import commands
import glob



stats=["Total Yards", "Passing", "Rushing", "First Downs", "Penalties", "Turnovers"]
years=["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"]


def get_away_team():
	line_no=int(commands.getoutput("grep -n '<table id=\"schools\" class=\"stats_table\">' " + filename + " | awk -F':' '{print $1}'"))
	away_team=commands.getoutput(''.join("awk 'NR==" + str(line_no+1) + "' " + filename)).split("</th>")[1]#.strip('<th>')
	return away_team[4:]
	
def get_home_team():
	line_no=int(commands.getoutput("grep -n '<table id=\"schools\" class=\"stats_table\">' " + filename + " | awk -F':' '{print $1}'"))
	home_team=commands.getoutput(''.join("awk 'NR==" + str(line_no+1) + "' " + filename)).split("</th>")[2]#.strip('<th>')
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


for year in years:
	for filename in glob.glob(year + "/*_soup.html"):
		try:
			print ''.join(get_away_team() + ","),
			for stat in stats:
				print ''.join(away_stat(stat) + ","),
			print "\n",
			print ''.join(get_home_team() + ","),
			for stat in stats:
				print ''.join(home_stat(stat) + ","),
			print "\n",
		except ValueError:
			continue
