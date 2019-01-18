tweet = input('geef tweet: ')

i_hashtag = tweet.find('#')

while i_hashtag != -1:

    # tweet afknippen net na het #-teken
    tweet = tweet[i_hashtag + 1:]
    i_spatie = tweet.find(' ')

    # hashtag  (en printen)
    print(tweet[:i_spatie])

    # tweet inkorten(al gedaan)

    # terug op zoek naar een #
    i_hashtag = tweet.find('#')
