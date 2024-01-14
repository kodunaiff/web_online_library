from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
from urllib.parse import urlsplit
from dotenv import load_dotenv
import os

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

load_dotenv()
library_path = os.getenv('LIBRARY_PATH')
with open(f"{library_path}\\library.json", "r", encoding="utf8") as my_file:
    library_json = my_file.read()
library = json.loads(library_json)

for book in library:
    image_link = urlsplit(book["image_link"])
    image_url = image_link.path.split('/')[2]
    book['image_link'] = f'library_folder/{image_url}'


rendered_page = template.render(library=library)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()