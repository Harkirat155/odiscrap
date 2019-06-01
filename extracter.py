import json
import requests
from bs4 import BeautifulSoup

print("Collected Players...\n Now collecting their details...")
print("We are trying our best...")

readLink = []
with open("player.json", "r") as read_file:
    readLink = json.load(read_file)

start_urls=[]
player_names=[]

for link in readLink:
    dia = link['link']
    dia = dia[12:]
    start_urls.append('http://stats.espncricinfo.com/ci/engine/{val}?class=2;template=results;type=batting'.format(val = dia)) 
    player_names.append(link['text'])


def check(runs):
    try:
        int(runs)
    except:
        return 'error'

def check(runs):
    try:
        int(runs)
    except:
        return 'error'

def detcall(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('table', attrs={'class': 'engineTable'})
    result2= results[3].find_all('tbody')
    result3=result2[4].find_all('tr', attrs={'class': 'data1'})
    

    #check year
    yearres=str(result3[1].find('b').text)
    if('year' not in yearres):
        result3=result2[5].find_all('tr', attrs={'class': 'data1'})
    
    result3=result3[1:]

    #check run
    runwrapcheck=False
    siblingres=[]
    for sibling in result3[0].td.next_siblings:
        siblingres.append(repr(sibling))
#    print(siblingres)
    runyeartagind=9
#    print(runyeartagind)
    runyeartag=siblingres[runyeartagind]
    start=runyeartag.find('<td>')
    end=runyeartag.find('</td>')
    runsres=runyeartag[start+4: end]
    if (check(runsres) == 'error'):
        if('nowrap' in runsres):
            runwrapcheck=True
        else:
            runyeartagind=7
#        print('changed',runyeartagind)

    dictres={}
    for res in result3:
        #find year
        yearres=str(res.find('b').text)
        # print(yearres)
        # if('year' not in yearres):
        #     return {}
        
        #find runs in that year
        siblingres=[]
        for sibling in res.td.next_siblings:
            siblingres.append(repr(sibling))
        runyeartag=siblingres[runyeartagind]
        start=runyeartag.find('<td>')
        end=runyeartag.find('</td>')
        runsres=runyeartag[start+4: end]
        #add result found to the result dictionary
        if('nowrap' in runsres):
            runsres='0'
        dictres[yearres]=runsres

    return dictres


final_res={}

for i in range(len(player_names)):
    print(player_names[i], start_urls[i], i)
    detrun=detcall(start_urls[i])
    print(player_names[i], detrun)
    final_res[player_names[i]]=detrun


with open("finalresfile.json", "w") as write_file:
    json.dump(final_res, write_file)

