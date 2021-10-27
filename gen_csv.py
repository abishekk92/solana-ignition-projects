from bs4 import BeautifulSoup
from glob import iglob
from itertools import islice
import pandas as pd

def parse_project(project_html):
    tagline = project_html.select_one("p.tagline").text.strip("\n").strip()
    name = project_html.select_one("div.software-entry-name h5").text.strip()
    image = project_html.select_one("img.software_thumbnail_image")["src"]
    url = project_html.select_one("a.link-to-software")["href"]
    hearts = project_html.select_one("span.like-count").text.strip()
    return {"Description" : tagline, "Project": name, "image_url" : image, "Project URL" : url, "Community Likes": int(hearts)}

all_data = []
for file_name in iglob("data/*.html"):
    document = BeautifulSoup(open(file_name).read())
    projects = document.select("div.gallery-item")
    all_data += list(map(parse_project, projects))

df = pd.DataFrame(all_data).drop_duplicates(subset=['Project'], keep='first')
df.to_csv("all_projects.csv", index=False)
