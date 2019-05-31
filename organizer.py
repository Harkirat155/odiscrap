import json

print('Things are nearly done!!!')

readLink = []
with open("player.json", "r") as read_file:
    readLink = json.load(read_file)

player_names=[]
for link in readLink:
    player_names.append(link['text'])

det={}
with open("finalresfile.json", "r") as read_file:
    det = json.load(read_file)

print("DONE!!!")

print('1.List of all players')
print('2.Search Players')
print('3.Quit')
print("Enter what you want to do...")

q=input('-->')


name=''
while(q!=3):
    if(q==1):
        print(det.keys())
    else:
        print("Enter player name of whom you want to know about")
        name=input('-->')

        option=[]
    #    if(type(det[name]) is not dict):
        for n in player_names:
            if name in n:
                option.append(n)
        print(option)
        print("if you like to know about any of above players, then type their name exctly...")
        name=input('-->')

        print('1.Runs Scored across the years in career...')
        print('2.Sum of Runs scored across the career...')
        print('3.Sum of runs scored across the period of years(as required)')
        print('Enter corresponding number to the option you seek...')
        inter=input('-->')
        if(inter == 1):
            print(det[name])
        if(inter == 2):
            runs=0
            for i in det[name]:
                runs+=int(det[name][i])
            print('{n} scored {r} in his whole ODI career...'.format(n=name, r=runs))
        if(inter == 3):
            print("Input year Period")
            print("from")
            start=input('-->')
            print("to")
            end=input('-->')
            start=int(start)
            end=int(end)
            runs=0
            for i in det[name]:
                if int(i[5:]) in range(start,end):
                    runs+=int(det[name][i])
            print('{n} scored {r} runs from {s} to {e}...'.format(n=name, r=runs, s=start, e=end))
        else:
            if(inter not in [1,2,3]):
                print('You did not enter appropriate value, but still...')
                runs=0
                for i in det[name]:
                    runs+=int(det[name][i])
                print('{n} scored {r} in his whole ODI career...'.format(n=name, r=runs))
    print('2.Search More Players')
    print('3.Quit')

    q=input('-->')

print('Bye!!!')