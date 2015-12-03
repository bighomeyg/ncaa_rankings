NCAA Rankings
-----

Example webpage (raw data, formatted):
http://www.sports-reference.com/cfb/boxscores/2000-08-27-penn-state.html

html found in tmp/2000-08-27-penn-state_soup.html

*All instances of "Texas A&M" changed to "Texas AM" because of a processing bug (rendering as 'Texas A&amp;M', which throws fits in csv files) with: sed -i 's|Texas A&amp;M|Texas AM|g' 
*Only done for 2000.... will convert 2001-2014 once stat compilation is complete
	
1. compile_database.py generates a weekly database of cummulative stats
2. stat_parser.py iterates through game files to parse out stats, add team stats to weekly databases
3. weekly_adder.py creates cumulative stats for each team, week by week
