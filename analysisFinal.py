import readability
import pickle
import syntok.segmenter as segmenter

loadfile = open('finals','rb')
finals = pickle.load(loadfile)
loadfile.close()
print('loaded')

subs = ['democrats','The_Donald','politics','bossfight']

for x in subs:
    
    print('analyzing ' + x)
    string = x + ' Analysis: \n'
    tokenized = '\n\n'.join(
     '\n'.join(' '.join(token.value for token in sentence)
        for sentence in paragraph)
     for paragraph in segmenter.analyze(finals[x]))

    print('boo')
    results = readability.getmeasures(tokenized, lang='en')
    with open(x+'.txt','a')as text_file:
        text_file.write('Readability Indexes: \n')
        print('next')
        text_file.write('FleschReadingEase: ' + str(results['readability grades']['FleschReadingEase']) + ' \n')
        print('next')
        text_file.write('Kincaid: ' + str(results['readability grades']['Kincaid']) + ' \n')
        print('next')
        text_file.write('SMOGIndex: ' + str(results['readability grades']['SMOGIndex']) + ' \n')
        print('next')
        text_file.write('\n' + 'Sentence Structure Information: \n')
        print('next')
        text_file.write('Average characters per word: ' + str(results['sentence info']['characters_per_word']) + ' \n')
        print('next')
        text_file.write('Average syllables per word: ' + str(results['sentence info']['syll_per_word']) + ' \n')
        print('next')
        text_file.write('Average words per sentence: ' + str(results['sentence info']['words_per_sentence']) + ' \n')
        print('next')
        text_file.write('Average sentences per paragraph: ' + str(results['sentence info']['sentences_per_paragraph']) + ' \n')
        print('next')
        text_file.write('Type token ratio: ' + str(results['sentence info']['type_token_ratio']) + ' \n')
        print('next')
        text_file.write('Total characters: ' + str(results['sentence info']['characters']) + ' \n')
        print('next')
        text_file.write('Total syllables: ' + str(results['sentence info']['syllables']) + ' \n')
        print('next')
        text_file.write('Total words: ' + str(results['sentence info']['words']) + ' \n')
        print('next')
        text_file.write('Total sentences: ' + str(results['sentence info']['sentences']) + ' \n')
        print('next')
        text_file.write('Total paragraphs: ' + str(results['sentence info']['paragraphs']) + ' \n')
        print('next')
        text_file.write('Total long words: ' + str(results['sentence info']['long_words']) + ' \n')
        print('next')
        text_file.write('Total complex words: ' + str(results['sentence info']['complex_words']) + ' \n')
        print('next')
        text_file.write('Words to complex words ratio: ' + str(results['sentence info']['words']/results['sentence info']['complex_words']) + ' \n')
        print('finished one')
