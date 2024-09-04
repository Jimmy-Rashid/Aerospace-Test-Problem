import os
from PIL import Image

with Image.open("data/absol.png") as pokemon:
    pokemon = pokemon.convert("HSV")

width = pokemon.size[0]
length = pokemon.size[1]

red_pixel_count = 0

pixel_table= []

for x in range(0, width):
    for y in range(0, length):
        pixel = pokemon.getpixel((x,y))
        if pixel != (0,0,0):
            red_pixel_count += 1
        
print(red_pixel_count)

data_path = "data/"
pokemon_dict = {}

# for pokemon in os.listdir(data_path):
    
#     pokemon_dict[pokemon] = "test"
    
# print(pokemon_dict)
    
