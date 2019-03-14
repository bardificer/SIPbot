import readability
import pickle
import syntok.segmenter as segmenter
subs = ['The_Donald','democrats','politics','bossfight']

finals = {'The_Donald':'','democrats':'','politics':'','bossfight':''}

for x in subs:
    file = open(x,'rb')
    print('opened')
    z = pickle.load(file)
    file.close()
    
    string = ''
    for y in z:
        string = string + '\n' + y
        print('thinking...')
    finals[x] = string

with open ('finals','wb') as file:
        pickle.dump(finals,file)

for x in finals:
    string = x + ' Analysis: \n'
    tokenized = '\n\n'.join(
     '\n'.join(' '.join(token.value for token in sentence)
        for sentence in paragraph)
     for paragraph in segmenter.analyze(x))

    print(tokenized)
    results = readability.getmeasures(tokenized, lang='en')
    with open(x+'.txt','a')as text_file:
        text_file.write('FleschReadingEase: ' + str(results['readability grades']['FleschReadingEase']) + ' \n')
        text_file.write('Kincaid: ' + str(results['readability grades']['Kincaid']) + ' \n ')
        text_file.write('SMOGIndex: ' + str(results['readability grades']['SMOGIndex']) + ' \n ')



