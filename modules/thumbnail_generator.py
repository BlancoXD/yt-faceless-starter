from PIL import Image, ImageDraw, ImageFont
import uuid
import os

def generate_thumbnail(title):
    width, height = 1280, 720
    output_path = f"output/thumbnails/{uuid.uuid4()}.jpg"

    img = Image.new("RGB", (width, height), color=(20, 20, 20))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except:
        font = ImageFont.load_default()

    margin = 50
    lines = []
    words = title.split(" ")
    line = ""
    for word in words:
        if draw.textlength(line + " " + word, font=font) < (width - 2 * margin):
            line += " " + word
        else:
            lines.append(line.strip())
            line = word
    lines.append(line.strip())

    y = height // 2 - (len(lines) * 60) // 2
    for line in lines:
        line_width = draw.textlength(line, font=font)
        x = (width - line_width) // 2
        draw.text((x, y), line, font=font, fill="white")
        y += 70

    img.save(output_path)
    return output_path
