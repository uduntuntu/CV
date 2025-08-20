import math
import svg
from datetime import date
import xml.dom.minidom
import yaml

current_year = date.today().year
years_count = current_year - 2000 + 1
output_file = "timeline_circle.svg"

def arc_path(cx, cy, r, start_deg, sweep_deg):
    # Calculate start and end points
    start_rad = math.radians(start_deg)
    end_rad = math.radians(start_deg + sweep_deg)
    x1 = cx + r * math.cos(start_rad)
    y1 = cy + r * math.sin(start_rad)
    x2 = cx + r * math.cos(end_rad)
    y2 = cy + r * math.sin(end_rad)
    # Large arc flag (always 0 for <180deg), sweep flag 1 (CW)
    return f"M {x1:.1f} {y1:.1f} A {r} {r} 0 0 1 {x2:.1f} {y2:.1f}"

elements = [
    svg.Rect(
        x=0, y=0, width=2000, height=2000,
        stroke="none", fill="white", stroke_width=0,
    ),
    svg.Circle(
        cx=1000, cy=1000, r=980,
        stroke="none", fill="black", stroke_width=0,
    ),
    svg.Circle(
        cx=1000, cy=1000, r=750,
        stroke="#9B59D0", fill="none", stroke_width=140,
    ),
    svg.Circle(
        cx=1000, cy=1000, r=600,
        stroke="#FFF8E7", fill="none", stroke_width=140,
    ),
    svg.Circle(
        cx=1000, cy=1000, r=450,
        stroke="#FFF433", fill="none", stroke_width=140,
    ),
    svg.Circle(
        cx=1000, cy=1000, r=300,
        stroke="#DDDDDD", fill="#DDDDDD", stroke_width=140,
    ),
]

# Add arcs and texts in the same loop, using href for textPath
i = 0
for year in range(2000, current_year + 1):
    start_deg = i * (360 / years_count)
    sweep_deg = 360 / years_count
    arc_id = f"arc{year}"
    i += 1
    # Arc path
    elements.append(
        svg.Path(
            d=arc_path(1000, 1000, 900, start_deg, sweep_deg),
            stroke="#2D2D2D",
            fill="none",
            stroke_width=140,
            id=arc_id,
        )
    )
    elements.append(
        svg.Text(
            text = svg.TextPath(
                href=f"#{arc_id}",
                startOffset="50%",
                text=f"{year}",
            ),
            font_size=40,
            font_family="sans-serif",
            fill="#FFF8E7",
            text_anchor="middle",
            dominant_baseline="middle",
        )
    )

canvas = svg.SVG(
    width=2000,
    height=2000,
    elements=elements,
)

with open(output_file, "w") as f:
    raw_xml = canvas.as_str()
    pretty_xml = xml.dom.minidom.parseString(raw_xml).toprettyxml(indent="  ")
    f.write(pretty_xml)

print(f'SVG file ({output_file}) created successfully.')