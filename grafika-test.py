from PIL import Image

img = Image.new( 'RGB', (1000,1000), "black") # create a new black image
pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pixels[i,j] = (i, j, 1) # set the colour accordingly

img.show()
for i in range(200):    # for every pixel:
    for j in range(300):
        pixels[i,j] = (i, j, 0) # set the colour accordingly

img.show()
