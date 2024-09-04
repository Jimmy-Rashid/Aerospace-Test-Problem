import os
import pandas as pd
import openpyxl
from PIL import Image

wb = openpyxl.open("main.xlsx")
ws = wb.active

data_path = "data/"
pixel_table = []

for pokemon in os.listdir(data_path):
    ws.append([pokemon])

wb.save("output.xlsx")

# pokemon = Image.open("data/abomasnow-mega.png")

# print(pokemon.size)
