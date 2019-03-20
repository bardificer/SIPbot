import pickle
import time

naem = ['Set2','Set3','Set4','Set5','Set6']
sublist = ['politics','bossfight','democrats','The_Donald']
subs = {'politics':[],'bossfight':[],'democrats':[],'The_Donald':[]}

def contained(final,string):
    for x in final:
        if x == string:
            return False
    return True

for y in naem:
    infile = open(y,'rb')
    tmp = pickle.load(infile)
    infile.close()

    for x in sublist:
        for y in tmp[x]:
            for z in tmp[x][y]:
                
                if not contained(subs[x],tmp[x][y]):
                    print('add one')
                    print(z)
                    subs[x].append(tmp[x][y])
                    
for x in sublist:
    with open (x,'wb') as file:
        pickle.dump(subs[x],file)
    print('sub ' + x + ' has been dumped')
