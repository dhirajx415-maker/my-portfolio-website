# My Portfolio — Jersey & Graphic Design Website

A responsive black-and-gold portfolio built with Python Flask.

## Features
- Premium landing page
- Gallery of jersey and graphic design references
- WhatsApp enquiry links with prefilled messages
- Responsive mobile layout

## Setup (Windows)
1. Install Python 3 from https://www.python.org/downloads/ and enable **Add Python to PATH**.
2. Extract this folder.
3. Open Command Prompt inside the project folder.
4. (Optional but recommended) Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
5. Install Flask:
   ```bash
   pip install -r requirements.txt
   ```
6. Open `app.py` and replace `WHATSAPP_NUMBER = "919000000000"` with your WhatsApp number, including country code and digits only.
7. Start the site:
   ```bash
   python app.py
   ```
8. Open http://127.0.0.1:5000 in your browser.

## Customize
- Change the brand name and text in `templates/index.html`.
- Replace the sample image URLs in `app.py` with your own image links, or download your designs into `static/images/` and use paths such as `/static/images/my-jersey.jpg`.
- Edit the `DESIGNS` list in `app.py` to add, remove, or rename gallery items.

## Important before publishing
- The gallery currently uses sample online images; replace them with artwork you own or have permission to use.
- Set your real WhatsApp number before sharing the website.
- `debug=True` is for local development only. Do not use Flask's development server/debug mode for public production hosting.
- To make it publicly accessible, deploy it to a Python-compatible host using a production WSGI server such as Gunicorn (Linux hosting) or Waitress (Windows hosting).
