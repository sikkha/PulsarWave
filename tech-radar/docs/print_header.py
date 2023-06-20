import datetime

html_content = '''
<!DOCTYPE html>
<html lang="en">

<head>
<meta http-equiv="Content-type" content="text/html; charset=utf-8">
<meta name="description" content="Geopolitics.Λsia Trend Radar: a tool to visualize trend monitoring, inspired by Tech Radar from Zalando to pick the best technologies for new projects">
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Geopolitics.Asia Trend  Radar</title>
<link rel="shortcut icon" href="https://www.geopolitics.asia/favicon.ico">

<script src="https://d3js.org/d3.v4.min.js"></script>
<script src="radar.js"></script>

<link rel="stylesheet" href="radar.css">
</head>

<body>

<img src="Geopoliticsasialogo.png" alt="Geopolitics.asia" style="max-width: 20%;">

<svg id="radar"></svg>

<script>
radar_visualization({
  svg_id: "radar",
  width: 1450,
  height: 1000,
  colors: {
    background: "#fff",
    grid: '#dddde0',
    inactive: "#ddd"
  },
  title: "Geopolitics.Λsia Trend Radar",
'''

# get the current date in dd/mm/yyyy: hh:mm format
current_date = datetime.datetime.now().strftime('%d/%m/%Y: %H:%M')


html_content += f'date: "{current_date}",\n\n'

html_content += '''
  quadrants: [
    { name: "Societal and Cultural"},
    { name: "Innovation and Law" },
    { name: "Politics/Security" },
    { name: "Economics" },
  ],
  rings: [
    { name: "ENGAGE", color: "#5ba300" },
    { name: "MONITOR", color: "#009eb0" },
    { name: "OBSERVE", color: "#c7ba00" },
    { name: "ACKNOWLEDGE", color: "#e09b96" }
  ],
  print_layout: true,
  links_in_new_tabs: true,
  // zoomed_quadrant: 0,
  //ENTRIES
  entries: [
'''

# Write the HTML content to a file
output_file = 'new_index.html'

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(html_content)

print(f"HTML content written to '{output_file}'")

