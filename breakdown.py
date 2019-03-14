import pickle
import time

naem = [<names of files>]
sublist = [<names of subs>]
subs = {<dicts with subs as names to lists>}


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
