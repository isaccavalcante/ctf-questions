from PIL import Image
im = Image.open('flag.png', 'r')
width, height = im.size
#print(width)
#print(height)
pixel_values = list(im.getdata())

#print(pixel_values)

begin = 0
end = width
for x in range(height):
    print(str(pixel_values[begin:end]).replace("[", "").replace("]", "") + "\n")
    begin = end
    end += width

