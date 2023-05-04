# Парсер документации PEP

## Описание

Парсер собирает информацию с сайта https://peps.python.org/ о статусах документов pep.  

## Стек технологий:

```
Python 3.7  
Scrapy 2.5.1
```

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Natulishka/scrapy_parser_pep.git
cd scrapy_parser_pep/
```

Создать и активировать виртуальное окружение и установить зависимости:
```
python -m venv venv
source venv/Scripts/activate
```
Обновить pip и установить зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Запустить парсер
```
scrapy crawl pep
```
Будет сформировано 2 файла:
```
pep_ДатаВремя.csv - номара, названия и статусы всех документов pep

status_summary_ДатаВремя.csv - сводный файл с количеством документов pep в разрезе статусов
```
