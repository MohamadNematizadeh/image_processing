# from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
#  


# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Open an Image
img = Image.open('input/Unequalized_Hawkes_Bay_NZ.jpg')

# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)

# Custom font style and font size
myFont = ImageFont.truetype('font/Vazir-Black.ttf', 65)

# Add Text to an image
text = 'این یک متن فارسی است'
reshaped_text = arabic_reshaper.reshape(text)
display_text = get_display(reshaped_text)
I1.text((10, 10), display_text, font=myFont, fill =(255, 0, 0))

# Display edited image
img.show()

# Save the edited image
img.save("car2.png")
