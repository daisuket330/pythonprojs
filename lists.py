# from pickle import APPEND


# anime = ['FMAB', 'PMMM', 'msgz', 'boruto']
# bad = 'boruto'
# good = '0083'
# print(anime)

# if bad in anime:
#     anime.remove(bad)
#     print(anime)
#     # anime.append(good)

# if good in anime:
#     print('good list'):
# else anime.APPEND(good)


list = {}
list['1'] = '1st'
list['2'] = '2nd'
list['3'] = '3rd'
list['4'] = '4th'
list['5'] = '5th'
definition = list.get('7')
print(definition)
print(list)

acronyms = {
    'LOL': 'laugh out loud',
    'IDK': "I don't know",
    'TBH': 'to be honest'}

sentence = 'IDK' + ' what happened ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')
print('sentence:' ,  sentence)
print('translation:' ,  translation)