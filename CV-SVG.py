import math
import svg
from datetime import date
import xml.dom.minidom
import yaml
max_x = 100
max_y = 100
elements = []
output_file = './test.svg'

def validate_date(iso_date="2000-01-01"):
    try:
        date.fromisoformat(iso_date)
    except:
        print("Not valid ISO 8601 format date, try again:")
        iso_date = validate_date(input())
    return date.fromisoformat(iso_date)

# defaults
start_date = validate_date("2000-01-01")
end_date = date.today()

def days_between(start = start_date, 
                 end = date(date.today().year,12,31)):
    return (end - start).days

def years_between(start = start_date, 
                 end = date(date.today().year,12,31)):
    return math.ceil((end - start).days / 365.25)

def angle(start = start_date, 
                 end = date(date.today().year,12,31)):
    # print(days_between(start_date, end_date))
    angle = 2 * math.pi * (days_between(start, end)) / days_between()
    # print(angle)
    if (angle == 0):
        return 360.0
    else:
        return math.degrees(angle)

#print (days_between(validate_date("2020-01-01"),validate_date("2025-09-24")), 
#       '/', days_between(), "d")
#print (years_between(validate_date("2020-01-01"),validate_date("2025-09-24")), 
#       '/', math.ceil(days_between() / 365.25) ,"a")
print (angle(validate_date("2020-01-01"), end_date), "degrees.")


def circle(x, y, radius, width, color, fill, opacity=1.0):
    yield svg.Circle(
        cx = x, cy = y, r = radius, 
        fill = fill, stroke = color, stroke_width = width,
        opacity=opacity
    )

def arc(radius, width, color, text_color, opacity=1, start=start_date, end=end_date, text="",id="a"):
    x1 = radius
    y1 = 0.0
    x2 = math.cos(math.radians(angle(start, end))) * radius
    y2 = math.sin(math.radians(angle(start,end))) * radius
    rotation = angle(validate_date("2000-01-01"),start)
    large_arc = bool(angle(start, end) > 180)
    sweep = True

    a = svg.Arc(
        rx=radius, ry=radius, angle=0, 
        large_arc=large_arc,sweep=sweep, 
        x=x2, y=y2
    )

    a = f"M {x1:.1f} {y1:.1f} {a}"

    yield svg.Path(
        d=a, id=id, stroke=color,stroke_width=width,fill='none', opacity=opacity, 
        transform=f"rotate({rotation})"
    )
    
    yield svg.Text(
            text = svg.TextPath(
                href=f"#{id}",
                startOffset="50%",
                text=f"{text}",
            ),
            font_size=4,
            font_family="sans-serif",
            fill=text_color,
            text_anchor="middle",
            dominant_baseline="middle"
        )
    
# Background
elements.extend(circle(0,0,100,1,'#000000','#000000'))


# Arcs background
#elements.extend(circle(0,0,95,9,'#2C2C2C','none'))
elements.extend(circle(0,0,80,19,'#9C59D1','none'))
elements.extend(circle(0,0,60,19,'#ffffff','none'))
elements.extend(circle(0,0,40,19,'#FCF434','none'))
elements.extend(circle(0,0,29.5,0,'none','#dddddd'))


# Year arcs
for year in range(2000, date.today().year + 1):
    if (year % 2 == 0): opacity = 0.35
    else: opacity = 0.65

    elements.extend(
        arc(
            95,9,"#2c2c2c","#cccccc",opacity,
            validate_date(f"{year}-01-01"), 
            validate_date(f"{year}-12-31"),
            f"{year}",f"{year}"
        )
    )

# Job arcs
jobs = []
jobs.extend(
    arc(
        85.5,9,"#2c2c2c","#cccccc",0.35,
        validate_date(f"2019-09-30"), 
        validate_date(f"2024-03-31"),
        "Suomen Rauhanliitto","job_1"
    )
)

jobs.extend(
    arc(
        80,19,"#2c2c2c","#cccccc",0.35,
        validate_date(f"2018-10-04"), 
        validate_date(f"2018-12-17"),
        "2","job_2"
    )
)

jobs.extend(
    arc(
        80,19,"#2c2c2c","#cccccc",0.35,
        validate_date(f"2017-12-07"), 
        validate_date(f"2018-01-26"),
        "3","job_3"
    )
)

jobs.extend(
    arc(
        80,19,"#2c2c2c","#cccccc",0.35,
        validate_date(f"2013-06-10"),
        validate_date(f"2014-06-10"),
        "Barona IT","job_4"
    )
)

jobs.extend(
    arc(
        75.5,9,"#2c2c2c","#cccccc",0.35,
        validate_date(f"2023-07-01"),
        validate_date(f"2023-09-23"),
        "5","job_5"
    )
)

jobs.extend(
    arc(
        75.5,9,"#2c2c2c","#cccccc",0.35,
        validate_date(f"2022-06-14"),
        validate_date(f"2023-06-14"),
        "Lähitaksi","job_6"
    )
)


elements.extend(jobs)

# Schools arcs
schools = []
schools.extend(
    arc(
            60,19,"#2c2c2c","#cccccc",0.65,
            validate_date(f"2024-03-06"), 
            validate_date(f"2025-04-19"),
            "",f"school_1"
        )
)

schools.extend(
    arc(
            60,19,"#2c2c2c","#cccccc",0.65,
            validate_date(f"2015-08-19"), 
            validate_date(f"2023-03-21"),
            "Metropolia ammattikorkeakoulu",f"school_2"
        )
)
elements.extend(schools)

canvas = svg.SVG(
    viewBox=svg.ViewBoxSpec(-max_x, -max_y, 2 * max_x, 2 * max_y),
    elements=elements,
)

with open(output_file, "w") as f:
    raw_xml = canvas.as_str()
    pretty_xml = xml.dom.minidom.parseString(raw_xml).toprettyxml(indent="  ")
    f.write(pretty_xml)

print(f'SVG file ({output_file}) created successfully.')