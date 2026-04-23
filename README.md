# 📄 PDF Stitcher (Offline)

A simple, privacy-first tool to merge PDFs locally using a browser interface.

---

## 🧠 Why I built this

I frequently needed to merge multiple PDF documents, often containing sensitive information.

Most online tools require uploading files, which wasn’t an option.

Existing desktop tools felt heavy or clunky for quick, repeated use.

So I built a lightweight, offline solution that runs locally in the browser.

---

## 🚀 What it does

* Add PDFs in multiple batches
* Drag & drop files directly into the browser
* Reorder files before merging (move up/down)
* Remove unwanted files
* Merge into a single PDF
* Custom output filename
* Clear all for quick reset
* Fully offline (no uploads)

---

## ⚙️ Tech Stack

* Python
* Flask (local server)
* pypdf (PDF processing)
* HTML + JavaScript (UI)

---

## ▶️ How to run

### 1. Install dependencies

```bash
pip install flask pypdf
```

### 2. Run the app

```bash
python app.py
```

### 3. Open in browser

The app will automatically open at:

```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
PDF-Stitcher/
│
├── app.py
├── templates/
│   └── index.html
├── uploads/        # auto-created during runtime
├── README.md
```

---

## 🔒 Privacy

* All processing happens locally
* No files are uploaded anywhere
* Safe for sensitive documents

---

## ⚡ Key Improvements Implemented

* Unique file handling (prevents overwrite issues)
* Custom output file naming
* Add files in multiple batches
* Drag & drop support
* Simple and fast UI

---

## 💡 Future Improvements

* Show page count per PDF
* Display total pages in final merged file
* Drag-and-drop reordering (advanced UI)
* Convert into standalone desktop app (.exe)
* Remember last used filename

---

## 🧪 Use Cases

* Merging reports
* Combining invoices
* Alumni / administrative documentation
* Financial or sensitive document handling

---

## 🙌 Notes

This tool was built to solve a real, recurring problem efficiently.

It focuses on:

* simplicity
* speed
* privacy

Feel free to use, modify, or extend it as per your needs.

---

## 📌 License

This project is open for personal and educational use.
