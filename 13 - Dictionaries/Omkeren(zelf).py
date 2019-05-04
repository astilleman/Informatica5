def omkeren(dictionary):
    mijn_dictionary = {}
    for key, value in dictionary.items():
        mijn_dictionary[value] = key
    return mijn_dictionary

print(omkeren({'blauw': 10 ,'geel' : 3, 'groen' : 9}))
