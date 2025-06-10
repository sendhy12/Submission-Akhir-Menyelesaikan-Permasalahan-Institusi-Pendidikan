# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
**Jaya Jaya Institut** adalah sebuah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan memiliki reputasi yang baik dalam mencetak lulusan berkualitas. Namun, seiring berjalannya waktu, mereka menghadapi tantangan serius terkait tingginya angka siswa yang tidak menyelesaikan pendidikan alias *dropout*. Tingginya tingkat *dropout* ini tidak hanya berdampak pada citra institusi, tetapi juga memengaruhi efektivitas operasional, akreditasi, dan kepuasan stakeholder, termasuk mahasiswa, orang tua, dan lembaga pendanaan. Untuk mengatasi permasalahan tersebut, Jaya Jaya Institut berinisiatif mengadopsi pendekatan berbasis data untuk mendeteksi siswa yang berpotensi mengalami *dropout* sejak dini, sehingga bisa diberikan intervensi dan bimbingan yang tepat. Mereka juga menginginkan sebuah *dashboard* interaktif yang dapat memantau performa siswa dan memberikan wawasan yang mudah dipahami bagi pihak manajemen.

### Permasalahan Bisnis
1. **Tingginya angka siswa yang mengalami *dropout*.**
   Hal ini menimbulkan kekhawatiran terhadap kualitas institusi dan efektivitas proses pendidikan yang berjalan.

2. **Ketiadaan sistem prediktif yang dapat mengenali siswa berisiko tinggi.**
   Saat ini belum ada sistem yang dapat mendeteksi potensi *dropout* secara proaktif dan berbasis data.

3. **Kebutuhan akan visualisasi performa siswa yang informatif.**
   Pihak manajemen membutuhkan *dashboard* untuk memantau perkembangan siswa secara berkala dan mengambil keputusan yang tepat berdasarkan data.

4. **Kesulitan dalam memahami faktor-faktor yang memengaruhi status kelulusan siswa.**
   Pihak institusi ingin memahami variabel mana saja yang paling berkontribusi terhadap kemungkinan siswa lulus, *dropout*, atau masih *enrolled*.

### Cakupan Proyek
Proyek ini akan berfokus pada pembangunan solusi berbasis data untuk membantu Jaya Jaya Institut dalam mengidentifikasi siswa yang berisiko mengalami *dropout* dan memberikan wawasan yang berguna bagi pengambilan keputusan melalui visualisasi interaktif. Adapun cakupan proyek ini meliputi:

1. **Eksplorasi dan Pembersihan Data**
   Melakukan eksplorasi dataset yang telah disediakan oleh Jaya Jaya Institut, termasuk pembersihan data, transformasi, dan identifikasi fitur penting.

2. **Analisis Eksploratif (Exploratory Data Analysis/EDA)**
   Melakukan analisis visual untuk memahami distribusi data, hubungan antar variabel, serta karakteristik siswa berdasarkan status kelulusan.

3. **Pra-pemrosesan Data dan Reduksi Dimensi**
   Melakukan standardisasi data dan reduksi dimensi menggunakan PCA (Principal Component Analysis) untuk meningkatkan efisiensi dan akurasi model.

4. **Pembangunan Model Prediktif**
   Membangun dan melakukan *hyperparameter tuning* terhadap beberapa algoritma klasifikasi (Decision Tree, Random Forest, Gradient Boosting) untuk memprediksi status siswa (Graduate, Dropout, Enrolled).

5. **Evaluasi Model**
   Mengevaluasi performa model menggunakan metrik klasifikasi seperti precision, recall, f1-score, dan confusion matrix.

6. **Identifikasi Fitur Penting**
   Menganalisis fitur asli yang paling memengaruhi hasil prediksi menggunakan kontribusi terhadap komponen PCA.

7. **Pembuatan Dashboard Interaktif**
   Mendesain dashboard visual menggunakan tools seperti Streamlit, Dash, atau Tableau (jika diperlukan), agar pihak manajemen dapat memantau kondisi dan performa siswa secara real time.
   
8. **Pengembangan Prototype Model**
   Mengimplementasikan solusi machine learning yang telah dibangun ke dalam bentuk prototype interaktif menggunakan **Streamlit**. Prototype ini memungkinkan pengguna (misalnya pihak akademik atau konselor) untuk memprediksi status siswa baru secara langsung.

9. **Rekomendasi Tindak Lanjut**
   Berdasarkan hasil analisis dan prediksi model, akan disusun beberapa **action items** yang dapat digunakan oleh Jaya Jaya Institut dalam upaya menurunkan angka dropout. Rekomendasi ini akan dituangkan dalam dokumen Markdown (.md) agar mudah diakses oleh pemangku kepentingan institusi.


### Persiapan

Sumber data: [students' performance](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv)

## Setup Environment

Untuk menjalankan proyek prediksi risiko dropout mahasiswa **Jaya Jaya Institut**, ikuti langkah berikut:

### Requirements

* Python 3.8 atau lebih tinggi
* Daftar pustaka (lihat `requirements.txt`), beberapa di antaranya:

  * `pandas`, `numpy`, `scikit-learn`
  * `streamlit`, `joblib`

### Struktur File

```
project/
│
├── dataset for dashboard.xlsx     # Dataset untuk visualisasi dashboard
├── app.py                         # Aplikasi Streamlit (antarmuka pengguna)
├── data_preprocessing.py          # Pipeline preprocessing
├── prediction.py                  # Fungsi prediksi menggunakan model
├── gboost_model.joblib            # Model Gradient Boosting yang sudah dilatih
├── scaler_pca.joblib              # Scaler dan PCA (gabungan)
├── label_encoder.joblib           # Label encoder
├── requirements.txt               # Daftar dependensi Python
├── README.md                      # Penjelasan proyek
└── notebook/                      # Notebook eksplorasi dan modeling
```

### Instalasi Lingkungan

Aktifkan environment virtual dan instal semua dependensi dengan perintah berikut:

```bash
pip install -r requirements.txt
```

---

## Business Dashboard

Business dashboard dibuat untuk memberikan **visualisasi komprehensif** terkait faktor-faktor yang memengaruhi tingkat dropout mahasiswa di Jaya Jaya Institut.

### Fitur Dashboard

* Ringkasan metrik utama: % Dropout, % Beasiswa, % Debitur, % Pembayaran Tepat Waktu
* Visualisasi dropout berdasarkan gender dan status beasiswa
* Dropout berdasarkan urutan pilihan program studi (application order)
* Dropout rate per program studi (course)

Dashboard ini ditujukan untuk membantu pihak manajemen akademik dalam:

* Mengidentifikasi kelompok mahasiswa berisiko tinggi
* Mengevaluasi program studi dengan tingkat dropout tinggi
* Menyusun strategi intervensi dan perbaikan

### Link Akses (jika sudah tersedia online):

> [Dashboard Dropout - Jaya Jaya Institut](https://public.tableau.com/views/SubmissionAkhirMenyelesaikanPermasalahanInstitusiPendidikan/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link)

---

## Menjalankan Sistem Machine Learning

Sistem prediksi dropout dibuat sebagai prototipe berbasis **Streamlit**, yang mengintegrasikan pipeline preprocessing dan model machine learning yang sudah dilatih.

### Cara Menjalankan

1. Jalankan perintah berikut di terminal:

```bash
streamlit run app.py
```

2. Aplikasi akan terbuka di browser lokal (biasanya di: `http://localhost:8501`)

### File Penting

* `app.py`: Antarmuka pengguna berbasis Streamlit
* `data_preprocessing.py`: Pipeline transformasi data (scaling, encoding, PCA)
* `prediction.py`: Fungsi prediksi berdasarkan model
* `gboost_model.joblib`: Model Gradient Boosting terlatih
* `scaler_pca.joblib`: Skaler dan PCA
* `label_encoder.joblib`: Encoder kategori

### Link Akses Prototype

> [Prototype Prediksi Dropout](https://dss2sendhy.streamlit.app/)

---

## Conclusion
Berdasarkan proyek analisis data dan pengembangan model machine learning untuk memprediksi status mahasiswa di Jaya Jaya Institut, ditemukan bahwa beberapa fitur memiliki pengaruh besar terhadap hasil reduksi dimensi PCA, yang kemudian digunakan untuk melatih model prediksi.

Fitur-fitur yang paling berpengaruh terhadap PCA (dan secara tidak langsung terhadap performa model) antara lain:
- **Scholarship_holder**
- **Gender**
- **Application_order**
- **Debtor**
- **Displaced**
- **Tuition_fees_up_to_date**

Fitur-fitur ini memberikan sinyal penting terkait kemungkinan seorang mahasiswa untuk lulus, dropout, atau masih terdaftar (*enrolled*). Model Gradient Boosting yang dilatih menunjukkan performa yang baik dalam membedakan ketiga kelas tersebut.

Model ini sudah dibungkus ke dalam prototipe interaktif berbasis Streamlit, dan dapat dijalankan di cloud untuk kemudahan akses bagi tim akademik dan manajemen kampus.

### Rekomendasi Action Items
Berdasarkan hasil proyek ini, berikut adalah beberapa langkah yang dapat diambil oleh Jaya Jaya Institut:

- **Tindak lanjuti mahasiswa yang tidak up-to-date dalam membayar biaya kuliah**  
  Mahasiswa dengan status *Tuition_fees_up_to_date = No* cenderung memiliki risiko dropout yang lebih tinggi. Institusi dapat membentuk tim khusus untuk menghubungi dan memberikan dukungan kepada mereka.

- **Berikan perhatian khusus pada mahasiswa yang bukan penerima beasiswa**  
  Mahasiswa tanpa beasiswa (*Scholarship_holder = No*) tampaknya memiliki hubungan kuat terhadap kemungkinan dropout. Menyediakan program bantuan finansial atau beasiswa tambahan bisa menjadi strategi pencegahan.

- **Gunakan hasil model prediksi untuk sistem peringatan dini**  
  Terapkan model dalam sistem akademik untuk mengidentifikasi mahasiswa dengan risiko tinggi secara otomatis. Mahasiswa tersebut kemudian dapat dimasukkan ke dalam program mentoring atau bimbingan belajar.

- **Cermati urutan pilihan jurusan saat pendaftaran (Application_order)**  
  Mahasiswa yang mendaftar ke jurusan sebagai pilihan kesekian memiliki kecenderungan dropout lebih tinggi. Evaluasi ulang proses penempatan jurusan dan tingkatkan konseling akademik di awal studi.

- **Lakukan monitoring khusus terhadap mahasiswa dengan status *Debtor* atau *Displaced***  
  Kedua kondisi ini berkontribusi besar terhadap prediksi model. Penanganan kasus personal dengan pendekatan psikososial dapat membantu mereka tetap terlibat dan berkomitmen.
