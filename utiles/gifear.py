# Gifea todos los .mov que se encuentren en la carpeta de ejecución

import os

for fn in os.listdir():
    f = fn.lower()
    if f.endswith('.mov'):
        g = f.replace('.mov', '.gif')
        os.system(f'ffmpeg -loglevel error -i "{f}" -pix_fmt rgb8 -filter:v scale=720:-1 -r 10 -n "{g}"')


