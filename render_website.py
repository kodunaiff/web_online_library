import json
import os
from urllib.parse import urlsplit

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape
from livereload import Server
from more_itertools import chunked
import math

load_dotenv()
library_path = os.environ['LIBRARY_PATH']
os.makedirs('pages', exist_ok=True)


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
        book['image_link'] = os.path.join('library_folder', image_url)
        book['book_path'] = os.path.join('library_folder', f"{book['book_name']}.txt")

    page_quantity_books = 10
    pages = chunked(library, page_quantity_books)
    quantity_pages = math.ceil(len(library)/page_quantity_books)
    for page_number, page in enumerate(pages, 1):
        rendered_page = template.render(library=chunked(page, 2),
                                        quantity_pages=quantity_pages,
                                        page_number=page_number)
        page_path = os.path.join('pages', f'index{page_number}.html')
        with open(page_path, 'w', encoding="utf8") as file:
            file.write(rendered_page)



on_reload()

server = Server()
server.watch('template.html', on_reload)
server.serve(root='.')
