from flask import render_template, request, redirect, url_for
from yt_dlp import YoutubeDL
from youtube_search import YoutubeSearch

from modules.classes import AdlessYTBPlayer

app = AdlessYTBPlayer(__name__)

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
def play(video_id):
    # Tu dois avoir la logique pour récupérer la vidéo actuelle et les résultats
    video_src, title = get_video_url(video_id)
    query = request.args.get("query", "")
    results = search(query) if query else []

    return render_template(
        "player.html", title=title, video_url=video_src, query=query, results=results
    )


if not app.vercel_project_production_url:
    app.run(host="localhost", port=5000, debug=True)
