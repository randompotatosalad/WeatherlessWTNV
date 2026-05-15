from pathlib import Path
from urllib.parse import quote

BASE_URL = "https://randompotatosalad.github.io/WeatherlessWTNV"

files = sorted(Path(".").glob("*.mp3"))

rss = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>

<title>WeatherlessWTNV</title>
<description>Personal podcast archive</description>
<link>https://randompotatosalad.github.io/WeatherlessWTNV/</link>
<language>en-us</language>

"""

for file in files:
    filename = file.name
    title = filename.replace(".mp3", "")
    encoded = quote(filename)

    rss += f"""
<item>

<title>{title}</title>

<enclosure
url="{BASE_URL}/{encoded}"
type="audio/mpeg"/>

<guid>
{BASE_URL}/{encoded}
</guid>

</item>
"""

rss += """
</channel>
</rss>
"""

with open("feed.xml", "w", encoding="utf-8") as f:
    f.write(rss)

print("feed.xml created successfully!")