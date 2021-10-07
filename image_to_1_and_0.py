# Pillow 7.0.0
from PIL import Image, ImageDraw, ImageFont

img = Image.open("Keanu.jpg")
# img.show()
WIDTH, HEIGHT = img.size

font = ImageFont.truetype("C:/Windows/Fonts/BRITANIC.ttf", 20)
cell_width, cell_height = 20, 20

img = img.resize((int(WIDTH / cell_width), int(HEIGHT / cell_height)), Image.NEAREST)
new_width, new_height = img.size
img = img.load()

new_img = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
d = ImageDraw.Draw(new_img)

for i in range(new_height):
    for j in range(new_width):
        r, g, b = img[j, i]
#         r, g, b, a = img[j, i] # use this line if you have an image with alpha value
        k = int((r + g + b) / 3)
        if k < 128:
            text = "1"
        else:
            text = "0"
        d.text((j * cell_width, i * cell_height), text=text, font=font, fill=(0, g, 0))

# new_img.show()
new_img.save("Keanu_0_1.png")
