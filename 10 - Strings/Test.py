woord = 'python'

#for letter in woord:
    #print(letter)

for i in range(0, len(woord), 2):
    #je hoeft 0 er niet bij te typen maar duidelijk, voor begin
    # telkens 1 minder dan de letters van het woord!
    # letters overslaan -> letters met even index
    print(woord[i])