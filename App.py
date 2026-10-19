import os

from flask import Flask, render_template
from newsapi import NewsApiClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    api_key = os.getenv("NEWSAPI_KEY")

    if not api_key:
        return (
            "Missing NEWSAPI_KEY. Copy .env.example to .env and add your NewsAPI key.",
            500,
        )

    try:
        newsapi = NewsApiClient(api_key=api_key)
        sources = ["abc-news", "bbc-news", "cnn", "fox-news"]
        response = newsapi.get_top_headlines(sources=",".join(sources))
        articles = response.get("articles", [])

        context = [
            (
                article.get("title") or "Untitled article",
                article.get("description") or "No description available.",
                article.get("urlToImage") or "",
            )
            for article in articles
        ]

        return render_template("index.html", context=context)

    except Exception:
        app.logger.exception("Unable to retrieve news from NewsAPI")
        return "Unable to retrieve news right now. Please try again later.", 502


if __name__ == "__main__":
    app.run(debug=True)
