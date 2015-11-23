import datetime
import glob

teamlist=[]
years=["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"]

def get_week(filename):
	month = int(filename.split("-")[1])
	day = int(filename.split("-")[2])
	return datetime.datetime(int(year), month, day).weekday()

for year in years:
	week = 1
	counter = 0	
	for filename in glob.glob(year + "/*_soup.html"):
		print filename
		if int(get_week(filename)) < int(counter):
			week += 1
		counter = int(get_week(filename))
		print week
	
	
	#Template file for database: preseason/week 0 (lists all 1A teams)
	with open(''.join(year + "/conferences_" + year + ".csv"), "r") as filename:
		for line in filename.readlines():
			team=line.split(",")[0]
			conference=line.split(",")[1]
			for n in range(0, week+1):
				template_file=open(''.join(year + "/week_" + str(n) + "_" + year + ".csv"), "a")
				template_file.write(''.join(line.strip() + ",\n"))




