#invoer
tweet = str(input('Geef een tweet: '))
hashtags = ''
#berekening
for i in range(0, len(tweet)):
    if tweet[i] == '#':
        while tweet[i + 1] != ' ':
            hashtags += tweet[i + 1]
            i += 1
        hashtags += '\n'

#uitvoer
print(hashtags)