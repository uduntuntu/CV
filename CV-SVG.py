import math
import svg
from datetime import date
import xml.dom.minidom
import yaml
max_x = 100
max_y = 100
circles = []
output_file = './test.svg'

def validate_date(iso_date="2000-01-01"):
    try:
        date.fromisoformat(iso_date)
    except:
        print("Not valid ISO 8601 format date, try again:")
        iso_date = validate_date(input())
    return date.fromisoformat(iso_date)

def days_between(start_date = date.fromisoformat('2000-01-01'), 
                 end_date = date(date.today().year,12,31)):
    return (end_date - start_date).days

def years_between(start_date = date.fromisoformat('2000-01-01'), 
                 end_date = date(date.today().year,12,31)):
    return math.ceil((end_date - start_date).days / 365.25)

def angle(start_date = date.fromisoformat('2000-01-01'), 
                 end_date = date(date.today().year,12,31)):
    # print(days_between(start_date, end_date))
    angle = 2 * math.pi * (days_between(start_date, end_date)) / days_between()
    # print(angle)
    if (angle == 0):
        return 360.0
    else:
        return math.degrees(angle)

#print (days_between(validate_date("2020-01-01"),validate_date("2025-09-24")), 
#       '/', days_between(), "d")
#print (years_between(validate_date("2020-01-01"),validate_date("2025-09-24")), 
#       '/', math.ceil(days_between() / 365.25) ,"a")
print (angle(validate_date("2020-01-01"),date.today()), "degrees.")


def circle(x, y, radius, width, color, fill, opacity=1.0):
    yield svg.Circle(
        cx = x, cy = y, r = radius, 
        fill = fill, stroke = color, stroke_width = width,
        opacity=opacity
    )

# Background
circles.extend(circle(0,0,100,0,'none','#000000'))


# Arcs background
circles.extend(circle(0,0,95,9,'#2C2C2C','none',0.7))
circles.extend(circle(0,0,80,19,'#9C59D1','none'))
circles.extend(circle(0,0,60,19,'#ffffff','none'))
circles.extend(circle(0,0,40,19,'#FCF434','none'))
circles.extend(circle(0,0,29.5,0,'none','#dddddd'))


canvas = svg.SVG(
    viewBox=svg.ViewBoxSpec(-max_x, -max_y, 2 * max_x, 2 * max_y),
    elements=circles,
)

with open(output_file, "w") as f:
    raw_xml = canvas.as_str()
    pretty_xml = xml.dom.minidom.parseString(raw_xml).toprettyxml(indent="  ")
    f.write(pretty_xml)

print(f'SVG file ({output_file}) created successfully.')