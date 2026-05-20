import os
import shutil
import tempfile

from flask import Flask, after_this_request, flash, redirect, render_template, request, send_file, url_for

from app import download_video


app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret")


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/download")
def download():
    url = request.form.get("url", "").strip()
    file_type = request.form.get("file_type", "mp4").strip().lower()
    quality = request.form.get("quality", "").strip()

    if not url:
        flash("Please provide a YouTube URL.")
        return redirect(url_for("index"))

    temp_dir = tempfile.mkdtemp(prefix="yt-download-")
    try:
        file_path, filename = download_video(url, file_type, quality, output_dir=temp_dir)
    except ValueError as exc:
        shutil.rmtree(temp_dir, ignore_errors=True)
        flash(str(exc))
        return redirect(url_for("index"))

    @after_this_request
    def cleanup(response):
        shutil.rmtree(temp_dir, ignore_errors=True)
        return response

    return send_file(file_path, as_attachment=True, download_name=filename)


if __name__ == "__main__":
    app.run(debug=True)
