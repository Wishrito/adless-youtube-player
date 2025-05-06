from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch

app = Flask(__name__)
app.template_folder = Path(__file__).parent / "templates"
app.static_folder = Path(__file__).parent / "src"

def get_video_url(youtube_url: str):
    ydl_opts = {
        "quiet": True,
        "format": "best[ext=mp4][protocol=https]",
        "noplaylist": True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        return info.get("url"), info.get("title")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form.get("query")
        return redirect(url_for("search", query=query))
    return render_template("index.html")

@app.route("/search/<query>")
def search(query: str):
    results = YoutubeSearch(query, max_results=10).to_dict()
    return render_template("results.html", results=results, query=query)

@app.route("/play/<video_id>")
def play(video_id: str):
    url = f"https://www.youtube.com/watch?v={video_id}"
    video_url, title = get_video_url(url)
    return render_template("player.html", video_url=video_url, title=title)


if __name__ == "__main__":
    app.run(debug=True)
