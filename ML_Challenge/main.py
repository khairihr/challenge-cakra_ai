import requests
import PyPDF2
from flask import Flask, render_template

app = Flask(__name__)

API_KEY = "Bearer 75f7a185-55a8-4aae-b0b2-47e016493b60"
API_URL = "https://saas.cakra.ai/genv2/llms"
PDF_PATH = "E:\khrd\latihan\Cerita_rakyat-1-9-1.pdf"

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

def proses_pertanyaan(teks_dokumen):
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": API_KEY
        }
        payload = {
            "model_name": "brain-v2",
            "messages": [
                {"role": "system", "content": "Buat 5 pertanyaan pilihan ganda ABCD dalam bahasa Indonesia dari teks pdf yang saya lampirkan dan sertakan jawaban yang benar setelah setiap pertanyaan. Dengan format Soal 1: Pertanyaan, ABCD, Jawab dan seterusnya"},
                {"role": "user", "content": teks_dokumen}
            ],
            "max_new_tokens": 500,
            "temperature": 0.7
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            hasil = response.json()
            return hasil.get("choices")[0].get("content", "").strip()
        else:
            print("Error API:", response.status_code, response.text)
            return f"Error API: {response.status_code} {response.text}"
    except Exception as e:
        print("Terjadi error saat proses API:", e)
        return "Error API."

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



if __name__ == "__main__":
    app.run(debug=True)
