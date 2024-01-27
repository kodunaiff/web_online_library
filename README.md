# Сайт электронной библиотеки 

Проект представляет из себя сайт электронной библиотеки [ссылка](https://kodunaiff.github.io/web_online_library/pages/index1.html).
Он создан на основе известного [интернет-ресурса tululu](https://tululu.org/).

![Image alt](pic1.png)

## Как установить
Склонируйте репозиторий на свой компьютер.

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

## Как запустить скрипт

Электронная библиотека формируется на основе json файла, который мы сформировали ранее ([ссылка](https://github.com/kodunaiff/Parsing_online_library)).

У скрипта есть два дополнительных параметра: "--file_folder" и "--page_folder" их трогать, необязательно т.к. у них есть дефолтные значения.

Первый параметр служит, чтоб указать путь хранения рабочих файлов (книги, картинки книг), 
так же в нем распологается наш json файл.

Второй используется для хранения наших html страниц.


### Пример запуска кода

````
py render_website.py

py render_website.py --page_folder pages

````

После запуска пройдите по ссылке http://127.0.0.1:5500


### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
