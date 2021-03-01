from PIL import ImageFont


class AsciiSentence:
    def __init__(self, sentence, font, kerning):
        self.sentence = sentence
        self.kerning = kerning
        self.font = font

    def word_to_ascii(self):
        font = ImageFont.truetype(self.font, 12)
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
                        line += str(letter)
                line += ' ' * self.kerning
            retval.append(line.strip())
        return retval
