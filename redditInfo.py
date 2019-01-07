import praw
import pickle
import time

filename = 'SIPdata'
subsList = ['republicans','democrats','politics','bossfight']
try:
    infile = open(filename,'rb')
    data = pickle.load(infile)
    infile.close()

except:
    data = {}
    for x in subsList:
        data[x] = {'title':[],'posts':[],'comments':[]}

reddit = praw.Reddit('SIPbot')

def collect(sub):
    for post in reddit.subreddit(sub).hot(limit=2):
        x = len(data[sub]['posts'])
        if x == 0:
            data[sub]['title'].append(post.title)
            data[sub]['posts'].append(post.selftext)
            p=0
            for y in post.comments:
                    data[sub]['comments'].append(post.comments[p].body)
                    p = p+1
        else:
            if data[sub]['posts'][x-1] != post.selftext:
                data[sub]['title'].append(post.title)
                data[sub]['posts'].append(post.selftext)
                p=0
                for y in post.comments:
                    data[sub]['comments'].append(post.comments[p].body)
                    p = p+1

while (1<2):
    for i in subsList:
        time.sleep(600)
        collect(i)
        with open(filename,'wb') as file:
            pickle.dump(data,file)
        print("I did it")
        print(data)


