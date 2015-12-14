NCAA Rankings
-----

Example webpage (raw data, formatted):
http://www.sports-reference.com/cfb/boxscores/2000-08-27-penn-state.html

html found in tmp/2000-08-27-penn-state_soup.html

All instances of "Texas A&M" changed to "Texas AM" because of a processing bug (rendering as 'Texas A&amp;M', which throws fits in csv files) with: sed -i 's|Texas A&amp;M|Texas AM|g' 

All instances of "Southern California" changed to "USC" because Southern California/California in csv files gets funky


(Only done for 2000.... will convert 2001-2014 once stat compilation is complete)

####Workflow:
1. compile_database.py generates a weekly database of cummulative stats
2. stat_parser.py iterates through game files to parse out stats, add team stats to weekly databases
3. weekly_adder.py creates cumulative stats for each team, week by week

Execute at once with workflow.sh

Errors to handle:
1.Army-Navy game throws an error in 2000, so for now, in stat_parser.py, I'm iterating up to last game
2. How to collect stats from D1-AA opponents (currently ignoring them... maybe no stats count, and team penalized just in S.O.S?)
