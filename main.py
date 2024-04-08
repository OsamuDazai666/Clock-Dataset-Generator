import math
import random
from PIL import Image, ImageDraw

def get_points(origin, radius, separation_angle=30):
    """ 
        orgin: cordinates of the origins,
        radius: radius of the circle,
        separation_angle: the separation angle (the angle by which to divide 360)
    """
    cordinates = []
    for i in range(0, int(360/separation_angle)):
        deg_angle = (separation_angle * (i + 1)) * (3.14 / 180) #
        x = round(radius * math.cos(deg_angle))
        y = round(radius * math.sin(deg_angle))
        cordinates.append((origin[0] + x, origin[1] + y))

    return cordinates

minutes = ["20", "25", "30", "35", "40", "45", "50", "55", "00", "05", "10", "15"]
hours = ["04", "05", "06", "07", "08", "09", "10", "11", "12", "01", "02", "03"]

minutes_cordinates = get_points((50,50), radius=40, separation_angle=30)
hours_cordinates = get_points((50,50), radius=27, separation_angle=30)

SAMPLE_SIZE = 100
random_minutes = random.choices(minutes_cordinates, k=SAMPLE_SIZE)
random_hours = random.choices(hours_cordinates, k=SAMPLE_SIZE)

for i in range(SAMPLE_SIZE):
    im = Image.new("RGB", (100, 100), color="white")
    draw = ImageDraw.Draw(im)

    draw.arc([(5, 5), (95, 95)], 0, 360, fill=0, width=2) # draw the cirle
    draw.line([(50, 50), random_minutes[i]], fill=0, width=1) # draw minutes
    draw.line([(50, 50), random_hours[i]], fill=0, width=2) # draw hours

    hour = hours[hours_cordinates.index(random_hours[i])]
    minute = minutes[minutes_cordinates.index(random_minutes[i])]

    im.save(f"{hour}.{minute}.png")

