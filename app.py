import os
import uuid
import webbrowser
from threading import Timer
from flask import Flask, request, send_file, render_template
from pypdf import PdfReader, PdfWriter

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/merge", methods=["POST"])

def merge():
    files = request.files.getlist("pdfs")

    writer = PdfWriter()
    writer.strict = False

    failed_files = []

    for file in files:
        filename = str(uuid.uuid4()) + ".pdf"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        try:
            reader = PdfReader(filepath)
            for page in reader.pages:
                writer.add_page(page)
        except:
            failed_files.append(file.filename)

    output_path = os.path.join(UPLOAD_FOLDER, "merged.pdf")
    with open(output_path, "wb") as f:
        writer.write(f)

    return send_file(output_path, as_attachment=True)

def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run(debug=False)
