import os
import math
import random
from PIL import Image, ImageDraw

from PIL import ImageDraw
def draw_clock_circle(size, num_hours, draw):
    angle_per_hour = 360 / num_hours

    center = (size // 2, size // 2)
    radius = size // 2 - 10  
    for i in range(num_hours):
        angle = math.radians(i * angle_per_hour - 90) 
        x1 = center[0] + radius * math.cos(angle)
        y1 = center[1] + radius * math.sin(angle)
        x2 = center[0] + (radius - 10) * math.cos(angle)
        y2 = center[1] + (radius - 10) * math.sin(angle)
        draw.line((x1, y1, x2, y2), fill='black', width=2)

def get_points(origin, radius, separation_angle=30):
    """
        orgin: cordinates of the origins,
        radius: radius of the circle,
        separation_angle: the separation angle (the angle by which to divide 360)
    """
    cordinates = []
    for i in range(0, 360 // separation_angle):
        deg_angle = (separation_angle * (i + 1)) * (3.14 / 180) #
        x = round(radius * math.cos(deg_angle))
        y = round(radius * math.sin(deg_angle))
        cordinates.append((origin[0] + x, origin[1] + y))

    return cordinates


def create_dataset(sample_size, images_per_folder, folder,
                   seed, image_size, radius_hours, radius_minutes):
    """
        The minutes_coordinates and hours_coordinates that we
        receive from get points are labeled acoording to PIL library.
        And Same goes for minutes and hours. Change it if you know
        what you are doing.
        sample_size: "number of iteration to perform, value between 500-1000 work better"
        images_per_folder: "number of images to generate per folder"
        folder: "name of folder to generate images in"
        seed: "random seed"
        image_size: "image height and width both must be same"
        radius_hours: "radius of hours hand"
        radius_minutes: "radius of minutes hand"
    """
    random.seed(seed)
    line_lenght = image_size // 2
    # change if you know what you are doing
    minutes = ["20", "25", "30", "35", "40", "45", "50", "55", "00", "05", "10", "15"]
    hours = ["04", "05", "06", "07", "08", "09", "10", "11", "12", "01", "02", "03"]

    minutes_cordinates = get_points((line_lenght, line_lenght), radius=radius_minutes, separation_angle=30)
    hours_cordinates = get_points((line_lenght, line_lenght), radius=radius_hours, separation_angle=30)

    SAMPLE_SIZE = sample_size
    random_minutes = random.choices(minutes_cordinates, k=SAMPLE_SIZE)
    random_hours = random.choices(hours_cordinates, k=SAMPLE_SIZE)

    for i in range(SAMPLE_SIZE):
        im = Image.new("RGB", (image_size, image_size), color="white")
        draw = ImageDraw.Draw(im)

        # draw the cirle
        draw_clock_circle(size=image_size, num_hours=12, draw=draw)
        # draw minutes 
        draw.line([(line_lenght, line_lenght), random_minutes[i]], fill=0, width=2)
        # draw hours 
        draw.line([(line_lenght, line_lenght), random_hours[i]], fill=0, width=3) 

        hour = hours[hours_cordinates.index(random_hours[i])]
        minute = minutes[minutes_cordinates.index(random_minutes[i])]

        #
        directory_path = f"{folder}/{hour}_{minute}"

        if not os.path.exists(directory_path):
        # Create the directory
            os.makedirs(directory_path)
            for i in range(0, images_per_folder):
                im.save(f"{directory_path}/{i}.png")
        else:
            print("Directory already exists:", directory_path)
