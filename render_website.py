import json
import os
from urllib.parse import urlsplit

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked

load_dotenv()
library_path = os.environ['LIBRARY_PATH']


def on_reload():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    with open(f"{library_path}\\library.json", "r", encoding="utf8") as my_file:
        library_json = my_file.read()
    library = json.loads(library_json)
    for book in library:
        image_link = urlsplit(book["image_link"])
        image_url = image_link.path.split('/')[2]
        book['image_link'] = f'library_folder/{image_url}'

    rendered_page = template.render(library=chunked(library, 2))
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


on_reload()

server = Server()
server.watch('template.html', on_reload)
server.serve(root='.')
