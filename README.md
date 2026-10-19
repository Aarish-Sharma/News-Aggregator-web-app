# News Aggregator Web Application

A small Flask web application that fetches top headlines from NewsAPI and displays article titles, descriptions, and images in an HTML page.

## Features

- Retrieves top headlines from ABC News, BBC News, CNN, and Fox News.
- Uses Flask to serve the web page.
- Uses a Jinja template to render article information dynamically.
- Reads the NewsAPI key from an environment variable rather than hardcoding it in source code.

## Requirements

- Python 3.9 or newer
- A NewsAPI API key

## Setup

1. Clone or download this repository.
2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .venv\\Scripts\\Activate.ps1
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env`.
5. Replace `your_newsapi_key_here` in `.env` with your own NewsAPI key. Do not commit `.env` to GitHub.
6. Run the application:

   ```bash
   python App.py
   ```

7. Open the local URL printed by Flask in your browser (usually `http://127.0.0.1:5000`).

## Project structure

```text
news-aggregator-flask/
├── App.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── templates/
    └── index.html
```

## Security note

Keep API keys out of source code and version control. If an API key was previously committed or shared publicly, revoke or rotate it and use a new key in your local `.env` file.

## Limitations

This is a learning project, not a production deployment. NewsAPI plan limits, source availability, and API errors can affect which headlines are returned.
