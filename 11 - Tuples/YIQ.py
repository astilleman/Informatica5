def yiq(rgb):


    #r, g, b = rgb

    #y = 0.299 * r + 0.587 * g + 0.144 * b
    #i = 0.596 * r - 0.274 * g - 0.322 * b
    #q = 0.211 * r - 0.523 * g + 0.312 * b

    y = 0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]
    i = 0.596 * rgb[0] - 0.274 * rgb[1] - 0.322 * rgb[2]
    q = 0.211 * rgb[0] - 0.523 * rgb[1] + 0.312 * rgb[2]

    return round(y, 4), round(i, 4), round(q, 4)

print(yiq((0, 0, 255)))

#round(y, 4), round(i, 4), round(q, 4)