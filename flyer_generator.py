from PIL import Image, ImageDraw, ImageFont
import datetime

def generate_flyer(colors):
    filename = f"flyer_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    img = Image.new("RGB", (800, 600), color=colors[0])
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    d.text((50, 50), "Your Custom Flyer", fill=colors[1], font=font)
    img.save(filename)
    return filename
