from BeautifulSoup import BeautifulSoup
import urllib2
import time

years=["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"]


base_url="http://www.sports-reference.com/cfb/years/"
home_url="http://www.sports-reference.com/"
     

##First, find the links for each and every game
for year in years:
    link_library=[]
    year_url=''.join([base_url, year, "-schedule.html"])
    page=urllib2.urlopen(year_url)
    soup=BeautifulSoup(page)
    for a in soup.findAll('a'):
        if 'boxscore' in a['href']:
            if 'htm' in a['href']:
                link_library.append(a['href'])
    
##Now iterate through each game and grab all of the data 
    for game in link_library:
        boxscore_url=''.join([home_url, game])
        print boxscore_url
        game_id = boxscore_url[47:-5]
        print game_id
        page=urllib2.urlopen(boxscore_url)
        soup=BeautifulSoup(page)
        outputfile=''.join(year + '/' + game_id + "_soup.html")
        with open(outputfile, "w") as f:
            f.write(str(soup))


        time.sleep(5)