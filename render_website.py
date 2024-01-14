from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
import json

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

library_path = 'C:\\Users\\Bato\\Desktop\\dvmn-less\\verstka_3\\library_folder'
with open(f"{library_path}\\library.json", "r", encoding="utf8") as my_file:
    library_json = my_file.read()
library = json.loads(library_json)

#for item_book_path in library:
       # item_book_path['image_link'] = urljoin(general_folder+'/', str(item_book_path['image_link]))


rendered_page = template.render(library=library)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()