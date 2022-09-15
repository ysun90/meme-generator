# Project: Motivational Meme Generator

## Overview

The goal of this project is to build a "meme generator" – a multimedia
application to dynamically generate memes, including an image with an overlaid
quote.


## Instructions for setting up and running the program

The program was developed with python3.9, with the following dependencies:

certifi==2022.6.15.1
charset-normalizer==2.1.1
click==8.1.3
Flask==2.2.2
idna==3.3
importlib-metadata==4.12.0
itsdangerous==2.1.2
Jinja2==3.1.2
lxml==4.9.1
MarkupSafe==2.1.1
numpy==1.23.3
pandas==1.4.4
Pillow==9.2.0
python-dateutil==2.8.2
python-docx==0.8.11
pytz==2022.2.1
requests==2.28.1
six==1.16.0
urllib3==1.26.12
Werkzeug==2.2.2
zipp==3.8.1

The program have two running modes: command-line interface (CLI) and flask app.

### CLI Application

Open bash terminal and make sure you are in the root directory of the project,
then run one of the following commands:

```
python3 meme.py
python3 meme.py --path [picture_path]
python3 meme.py --body [quote_body] --author [author]
python3 meme.py --path [picture_path] --body [quote_body] --author [author]
```

When parameters are empty, the program chooses randomly using data from _data.


### Flask App

Open terminal and go to the project root, run:

```
python3 app.py
```

Open the webpage according to the instructions from the terminal, on local
machine, it should generally be: http://127.0.0.1:5000/


## Description of the modules and how to use them

The application includes two sub-modules:

### QuoteEngine module

The Quote Engine module is responsible for ingesting many types of files that
contain quotes. For our purposes, a quote contains a body and an author:

"This is a quote body" - Author

Currently, this sub-module can parse 4 filetypes: docx, pdf, csv and txt,
implemented by **DocxIngestor**, **PDFIngestor**, **CSVIngestor**,
**TXTIngestor**. All specific ingestors are encapsulated into **Ingestor**
to realise the ingestor interface in **IngestorInterface**.

Run `Ingestor.parse('path_of_file')` to parse the file and get a list of quotes.

In addition, **xpdf** is required to convert pdf to txt before parsing,
run `apt-get install -y xpdf` for ubuntu or `brew install xpdf` for mac.

### MemeEngine module

The Meme Engine Module is for manipulating and drawing text onto images.

Create an instance by `meme = MemeEngine('path_of_output_picture')`, then call
`meme.make_meme('path_of_image', 'text_to_be_put_on_image', 'author')` to
draw a quote (text + author) on the image.

The packase **Pillow** is requird for this sub-module.
