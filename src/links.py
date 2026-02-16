import requests
from bs4 import BeautifulSoup
from pathlib import Path

URL = "https://en.wikipedia.org/wiki/Abraham_Lincoln"

headers = {
    'User-Agent': 'WikiSpeedrunBot'
}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="mw-content-text")

for ref in results.find_all("sup", class_="reference"):
    ref.decompose()

to_remove = [
    ".infobox",          
    ".noprint",           
    ".mw-references-wrap",
    "#normdaten",        
    ".catlinks",          
    ".navbox",            
    "style"               
    ".reference",         
    ".mw-editsection",   
    ".printfooter",      
    ".new",
    ".mw-file-description", 
    ".thumb",                
    "figure",
    ".external",        
    ".navbox",          
    ".sistersitebox"    

]

for selector in to_remove:
    for element in results.select(selector):
        element.decompose()


links = results.find_all("a")

clean_links_list = []

for link in links:
    href = link.get('href', '')
    if href.startswith("/wiki/") and ":" not in href:
        if href not in clean_links_list: 
            clean_links_list.append(href)


for i in clean_links_list:
    print(i)

title_tag = soup.find(id="firstHeading")
filename = title_tag.get_text().strip().replace(" ", "_") if title_tag else "unknown_article"


data_dir = Path("./data")
data_dir.mkdir(parents=True, exist_ok=True)  
file_path = data_dir / f"{filename}.txt"


with file_path.open("w", encoding="utf-8") as f:
    f.write(f"{filename}\n")
    for i in clean_links_list:
        f.write(f"https://en.wikipedia.org{i}\n")