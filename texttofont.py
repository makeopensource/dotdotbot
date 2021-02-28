from PIL import ImageFont


def letter_to_ascii(letter):
    retval = ""
    with open(f'characters/{letter}.txt', 'r') as f:
        for line in f:
            retval += line.replace('0', ' ').replace('1', letter)
    return retval


def word_to_ascii(word):
    font = ImageFont.truetype('Deftone-Stylus/DEFTONE.ttf', 12)
    height = font.getsize('a')[1]

    retval = ""
    for row in range(height):
        for letter in word:
            width = font.getsize(letter)[0]
            height = font.getsize(letter)[1]
            mask = [x for x in font.getmask(letter)]

            bitmap = []
            for r in range(height):
                bitmap.append(mask[r*width:r*width + width])

            row_bitmap = bitmap[row]
            if len(row_bitmap) == 0:
                retval += width * ' '
            for pixel in row_bitmap:
                if pixel < 100:
                    retval += ' '
                else:
                    retval += '1'
            retval += '   '
        retval = retval.rstrip()
        retval += '\n'
    return retval.rstrip()
