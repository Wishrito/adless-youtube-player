from flask import redirect, render_template, request, url_for
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL
from yt_dlp.utils import YoutubeDLError

from modules.classes import app


def get_video_url(youtube_url: str, cookie: str):
    ydl_opts = {
        "headers": {"Cookie": cookie},
        "quiet": True,
        "format": "best[ext=mp4][protocol=https]",
        "noplaylist": True,
    }
    try:

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            return info.get("url"), info.get("title")
    except YoutubeDLError:
        app.get_cookies()
        get_video_url(youtube_url, app.webCookies)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form.get("query")
        return redirect(url_for("search", query=query))
    return render_template("index.j2")

@app.route("/search/<query>")
def search(query: str):
    results = YoutubeSearch(query, max_results=10).to_dict()
    return render_template("results.j2", results=results, query=query)


@app.route("/play/<video_id>")
def play(video_id: str):

    video_src, title = get_video_url(video_id, app.webCookies)
    query = request.args.get("query", "")
    results = search(query) if query else []

    return render_template(
        "player.j2", title=title, video_url=video_src, query=query, results=results
    )


# si l'application n'est pas lancée sur Vercel, lancement en mode debug
if not app.vercel_project_production_url:
    app.run(host="localhost", port=5000, debug=True)
