from flask import Flask, render_template, request, send_file
import io
from reportlab.pdfgen import canvas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/print', methods=['POST'])
def print_nota():
    nama = request.form.get('nama')
    barang = request.form.get('barang')
    harga = request.form.get('harga')

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(100, 750, "Nota Program Kasih")
    pdf.drawString(100, 720, f"Nama: {nama}")
    pdf.drawString(100, 700, f"Barang: {barang}")
    pdf.drawString(100, 680, f"Harga: {harga}")
    pdf.save()

    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="nota.pdf", mimetype="application/pdf")

if __name__ == "__main__":
    app.run()
