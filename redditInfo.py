import praw
import pickle
import time

filename = 'SIPdata'
subsList = ['The_Donald','democrats','politics','bossfight']
try:
    infile = open(filename,'rb')
    data = pickle.load(infile)
    infile.close()

except:
    data = {}
    for x in subsList:
        data[x] = {'title':[],'posts':[],'comments':[]}

reddit = praw.Reddit('SIPbot')

def contained(post,sub)
    for x in data[sub]['posts']:
        if x == post:
            return True
    return False


def collect(sub):
    try:
        for post in reddit.subreddit(sub).hot(limit=2):
            if not contained(post,sub):
                data[sub]['title'].append(post.title)
                data[sub]['posts'].append(post.selftext)
                p=0
                for y in post.comments.replace_more(limit=0):
                    data[sub]['comments'].append(post.comments[p].body)
                    p = p+1

while (1<2):
    for i in subsList:
        time.sleep(2)
        collect(i)
        with open(filename,'wb') as file:
            pickle.dump(data,file)
        print("I did it")
        print(data)


