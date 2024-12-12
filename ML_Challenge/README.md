# Membuat Pertanyaan Pilihan Ganda dari File PDF menggunakan Flask dan LLM API Cakra AI


## Yang saya gunakan

### **1. Library dan bahasa yang digunakan**
- **Python**: Bahasa pemrograman utama
- **Flask**: Framework web untuk menampilkan hasil di browser
- **PyPDF2**: Library untuk membaca teks dari file PDF
- **Cakra AI LLM API**: API yang digunakan untuk menghasilkan pertanyaan dari teks dokumen yang disediakan tim rekrutmen

### **2. Struktur Proyek**
```
.
├── main.py       # File utama untuk backend Flask
├── templates/
│   └── index.html # Template HTML untuk menampilkan hasil
├── README.md     # Dokumentasi proyek
└── requirements.txt # Daftar dependensi Python
```

---

## Cara Kerja (How It Works)

### **1. Membaca Dokumen PDF**
- Menggunakan **PyPDF2**, dokumen PDF dibaca dan teksnya diekstraksi.

### **2. Memproses Pertanyaan Menggunakan API**
- Teks dari dokumen PDF dikirim ke **Cakra LLM API**
- Format permintaan dikustomisasi untuk menghasilkan pertanyaan dengan jawaban yang didapatkan dari API LLM Cakra AI

### **3. Menampilkan Hasil di Web**
- Flask digunakan untuk membuat server web
- Hasil diproses dan dirender ke halaman HTML

---

## Implementasi

### **1. Prasyarat (Requirements)**
Pastikan kamu memiliki:
- Python 3.8 atau versi yang lebih baru
- Dependensi Python: Flask, PyPDF2, dan requests

Instal dependensi:
```bash
pip install -r requirements.txt
```

### **2. Menjalankan Proyek**
1. Clone repositori ini
2. Letakkan file PDF yang ingin diproses di direktori proyek
3. variabel yang harus disesuaikan berikut di `main.py`:
   - `API_KEY`: Token API dari **Cakra AI LLM API**
   - `PDF_PATH`: Path file PDF yang akan diproses
4. Jalankan server Flask:
   ```bash
   python main.py
   ```
5. Buka browser dan akses `http://127.0.0.1:5000/`

---

## Penjelasan Kode

### **File: main.py**
#### Membaca Dokumen PDF
```python
def baca_dokumen(pdf_path):
    teks = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for halaman in reader.pages:
                teks += halaman.extract_text()
    except Exception as e:
        print("Gagal membaca file PDF:", e)
    return teks
```
- Fungsi ini membaca teks dari semua halaman di file PDF yang diberikan

#### Memproses API
```python
def proses_pertanyaan(teks_dokumen):
    headers = {
        "Content-Type": "application/json",
        "Authorization": API_KEY
    }
    payload = {
        "model_name": "brain-v2",
        "messages": [
            {"role": "system", "content": "Buat 5 pertanyaan pilihan ganda ABCD..."},
            {"role": "user", "content": teks_dokumen}
        ],
        "max_new_tokens": 500,
        "temperature": 0.7
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json().get("choices")[0].get("content", "")
```
- Fungsi ini mengirim teks dokumen ke API dan mengembalikan hasilnya

#### Halaman Web
```python
@app.route("/", methods=["GET"])
def halaman_utama():
    teks_dokumen = baca_dokumen(PDF_PATH)
    if teks_dokumen:
        status = "Dokumen berhasil dimuat"
        raw_output = proses_pertanyaan(teks_dokumen)
        hasil_split = raw_output.split("\n")
        pertanyaan = []
        for baris in hasil_split:
            baris_bersih = baris.lstrip("12345. ")
            if baris_bersih:
                pertanyaan.append(baris_bersih.strip())
    else:
        status = "Gagal memuat dokumen"
        pertanyaan = []
    return render_template("index.html", status=status, pertanyaan=pertanyaan)
```
- Fungsi ini memproses hasil dari API dan menampilkannya di halaman web

#### Template HTML
File: `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aplikasi Pilihan Ganda Cakra.AI</title>
</head>
<body>
    <h1>Status Dokumen: {{ status }}</h1>
    <h2>Pertanyaan:</h2>
    {% for p in pertanyaan %}
        <p>{{ p }}</p>
        <hr>
    {% endfor %}
</body>
</html>
```
- Template untuk menampilkan pertanyaan di browser

---

