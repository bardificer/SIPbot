import pickle
data = {}
infile = open('SIPdata','rb')
data = pickle.load(infile)
infile.close()

print(data)
