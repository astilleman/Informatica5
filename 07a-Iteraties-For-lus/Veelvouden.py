r = (int(input('getal: ')))
som_veelvouden = 0

#overloop alle veelvouden van r
for i in range(r, 101, r):
    som_veelvouden += i

print(som_veelvouden)

