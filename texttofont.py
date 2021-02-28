from PIL import ImageFont


class AsciiSentence:
    def __init__(self, sentence, kerning):
        self.sentence = sentence
        self.kerning = kerning

    def word_to_ascii(self):
        font = ImageFont.truetype('Deftone-Stylus/DEFTONE.ttf', 12)
        height = font.getsize('a')[1]

        retval = []
        for row in range(height):
            line = ""
            for letter in self.sentence:
                width = font.getsize(letter)[0]
                height = font.getsize(letter)[1]
                mask = [x for x in font.getmask(letter)]

                bitmap = []
                for r in range(height):
                    bitmap.append(mask[r * width:r * width + width])

                row_bitmap = bitmap[row]
                if len(row_bitmap) == 0:
                    line += width * ' '
                for pixel in row_bitmap:
                    if pixel < 100:
                        line += ' '
                    else:
                        line += '1'
                line += ' ' * self.kerning
            retval.append(line.strip())
        return retval

#
#
# def letter_to_ascii(letter):
#     retval = ""
#     with open(f'characters/{letter}.txt', 'r') as f:
#         for line in f:
#             retval += line.replace('0', ' ').replace('1', letter)
#     return retval
