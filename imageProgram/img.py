from PIL import Image , ImageFilter
 
img = Image.open('./Coolimg.jpeg')
img.thumbnail((400,400))
filteredImg=img.filter(ImageFilter.SHARPEN)
filteredImg.save('new.png','png')

