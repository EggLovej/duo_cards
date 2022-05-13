import duolingo
import json

lingo = duolingo.Duolingo('Jonas434669', 'LOLOp0123459876')
print(lingo.get_languages(abbreviations=True))
l = lingo.get_vocabulary('pt')
s = json.dumps(l)
jdata = json.loads(s)

wordlist = []
for i in range(len(jdata['vocab_overview'])):
    wordlist.append(jdata['vocab_overview'][i]['word_string'])
wordlist = lingo.get_translations(wordlist, source='pt', target='en')

for item in wordlist:
    print(item, end="  :")
    for j in wordlist.get(item):
        print(j, end=', ')
    print(" ")

