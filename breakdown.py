import pickle
import time

naem = ['Set2','Set3','Set4','Set5','Set6']
sublist = ['politics']
subs = {'politics':[]}


for y in naem:
    infile = open(y,'rb')
    tmp = pickle.load(infile)
    infile.close()

    for x in sublist:
        subs[x] = subs[x] + tmp[x]['title'] + tmp[x]['posts'] + tmp[x]['comments']
for x in sublist:
    with open (x,'wb') as file:
        pickle.dump(subs[x],file)
    print('sub ' + x + ' has been dumped')
    time.sleep(30)
