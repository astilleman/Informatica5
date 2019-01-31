#invoer
s1 = input('Geef woord 1: ')
s2 = input('Geef woord 2: ')

#berekening gemeenschappelijke prefix
langste_woord = ''

if len(s1) == min(len(s1), len(s2)):
    kortste_woord = s1

else:
    kortste_woord = s2

gem_prefix, einde_p_prefix, i = '', 0, 0

while s1[i] == s2[i]:
    gem_prefix += s1[i]
    einde_p_prefix = i
    i += 1

#berekening gemeenschappelijke suffix
omgekeerd_s1 = s1[::-1]
omgekeerd_s2 = s2[::-1]
gem_suffix, begin_p_suffix, i = '', 0, 0

while omgekeerd_s1[i] == omgekeerd_s2[i]:
    gem_suffix += omgekeerd_s1[i]
    begin_p_suffix = - i - 1
    i += 1

gem_suffix = gem_suffix[::-1]

#berekening stam
if len(gem_prefix) == 0 and len(gem_suffix) != 0:
    stam1 = s1[0:begin_p_suffix]
    stam2 = s2[0:begin_p_suffix]

elif len(gem_suffix) == 0 and len(gem_prefix) != 0:
    stam1 = s1[einde_p_prefix + 1:len(s1)]
    stam2 = s2[einde_p_prefix + 1:len(s2)]

elif len(gem_prefix) == 0 and len(gem_suffix) == 0:
    stam1 = s1
    stam2 = s2

else:
    stam1 = s1[einde_p_prefix + 1:begin_p_suffix]
    stam2 = s2[einde_p_prefix + 1:begin_p_suffix]

#langste stam
if len(stam1) > len(stam2):
    langste_stam = stam1
    kortste_stam = stam2

else:
    langste_stam = stam2
    kortste_stam = stam1

# vorm
message = '{:^{}}┏{}┓{}'.format('', len(gem_prefix), stam1.center(len(langste_stam)), '')
message += '\n{}┫{:{}}┣{}'.format(gem_prefix, '', len(langste_stam), gem_suffix)
message += '\n{:^{}}┗{}┛{}'.format('', len(gem_prefix), stam2.center(len(langste_stam)), '')


#uitvoer
print(message)
