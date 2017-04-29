from PIL import Image
import sys

for image in sys.argv[1:]:
   print("rotating {}".format(image))
   im = Image.open(image)
   out = im.rotate(180)
out.save(image)
