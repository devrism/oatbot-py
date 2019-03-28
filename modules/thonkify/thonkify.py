from PIL import Image
from dictionary import dictionary

def thonkify(input):
    input = input.content
    input = input[10:]
    cleaned = input
    tracking = Image.open("images/misc/tracking.png")

    #remove characters thonkify can't parse
    for character in input:
        if character not in dictionary:
            cleaned = cleaned.replace(character, "")

    x = 0
    y = 896
    image = Image.new('RGBA', [x, y], (0, 0, 0))
    for character in cleaned:
        value = dictionary.get(character)
        addedimg = Image.new('RGBA', [x + value.size[0] + tracking.size[0], y], (0, 0, 0))
        addedimg.paste(image, [0, 0])
        addedimg.paste(tracking, [x, 0])
        addedimg.paste(value, [x + tracking.size[0], 0])
        image = addedimg
        x = x + value.size[0] + tracking.size[0]
        #TODO add some space between the letters and make a transparent one

    #does shrinking the file increase upload and save speed?
    maxsize = 1024, 896
    if (image.size[0] > maxsize[0]):
        image.thumbnail(maxsize, Image.ANTIALIAS)

    image.save('result.png', 'PNG')
