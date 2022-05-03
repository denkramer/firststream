from PIL import Image
width = 400
height = 300
img  = Image.new( mode = "RGB", size = (width, height), color=(0, 0, 0) )

pixels = img.load() # create the pixel map

pixelstuple = (400, 300)

for i in range(img.size[0]): # for every pixel:
	for j in range(100, 200):
		pixels[i, j] = (255, 255, 255)

img.show()

