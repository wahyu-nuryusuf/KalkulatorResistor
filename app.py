from flask import Flask, render_template, request, jsonify

aplikasi = Flask(__name__)

kode_warna = {
    "hitam":  {"angka": 0, "pengali": 1},
    "coklat": {"angka": 1, "pengali": 10, "toleransi": "±1%"},
    "merah":  {"angka": 2, "pengali": 100, "toleransi": "±2%"},
    "oranye": {"angka": 3, "pengali": 1_000},
    "kuning": {"angka": 4, "pengali": 10_000},
    "hijau":  {"angka": 5, "pengali": 100_000, "toleransi": "±0.5%"},
    "biru":   {"angka": 6, "pengali": 1_000_000, "toleransi": "±0.25%"},
    "ungu":   {"angka": 7, "pengali": 10_000_000, "toleransi": "±0.1%"},
    "abu-abu": {"angka": 8, "pengali": 100_000_000, "toleransi": "±0.05%"},
    "putih":  {"angka": 9, "pengali": 1_000_000_000},
    "emas":   {"pengali": 0.1, "toleransi": "±5%"},
    "perak":  {"pengali": 0.01, "toleransi": "±10%"},
    "tidak ada": {"toleransi": "±20%"}
}

@aplikasi.route('/')
def halaman_utama():
    return render_template('index.html')

@aplikasi.route('/hitung', methods=['POST'])
def hitung_resistor():
    data = request.get_json()
    gelang1 = data['gelang1']
    gelang2 = data['gelang2']
    pengali = data['pengali']
    toleransi = data['toleransi']

    try:
        angka1 = kode_warna[gelang1]["angka"]
        angka2 = kode_warna[gelang2]["angka"]
        nilai_pengali = kode_warna[pengali]["pengali"]
        nilai_toleransi = kode_warna[toleransi]["toleransi"]
    except KeyError as e:
        return jsonify({"error": f"Ada kesalahan dalam input warna: {e}"}), 400

    resistansi = (angka1 * 10 + angka2) * nilai_pengali

    return jsonify({
        "resistansi": f"{resistansi} Ω",
        "toleransi": f"Toleransi: {nilai_toleransi}",
        "warna": f"Warna: {gelang1}, {gelang2}, {pengali}, {toleransi}"
    })

if __name__ == '__main__':
    aplikasi.run(debug=True)

