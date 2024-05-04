Proyek Akhir: Menyelesaikan Permasalahan Perusahaan JayaJayaJaya
===========================================================

Business Understanding
----------------------

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.
### Permasalahan Bisnis

1.  Tingginya tingkat (attrition) karyawan pada perusahaan JayaJayaJaya.
2.  Apa saja yang menjadi faktor penyebab karyawan melakukan attrition ?
3. Langkah apa yang diperlukan untuk mencegah karyawan akan melakukan attrition ?


### Cakupan Proyek

Proyek ini akan berfokus pada analisis data karyawan perusahaan, terutama faktor-faktor yang memengaruhi tingkat attrition dan kepuasan kerja. Tujuannya adalah untuk mengidentifikasi akar permasalahan dan memberikan rekomendasi solusi yang dapat diimplementasikan oleh perusahaan. 

Selain analisis dari faktor penyebab attrition, kami juga membuat program untuk memprediksi kemungkinan karyawan melakukan attrition atau tidak dengan tingkat akurasi sebesar 88%.

### Persiapan

Sumber data: [JayaJayaJaya](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:

# Setting Up the Environment (Notebook)

Ikuti langkah-langkah berikut untuk mengatur environment dengan packages yang diperlukan:

### Prerequisites

- Python (version 3.7 or higher)
- pip (Python package installer)

### Step 1: Install Required Packages
Buka terminal atau command prompt, ubah direktori sesuai dengan lokasi aplikasi berada dan jalankan perintah berikut untuk menginstal paket yang diperlukan dari file `requirements.txt`:

`pip install -r requirements.txt`

Perintah diatas akan menginstal versi yang ditentukan dari `joblib`, `matplotlib`, `pandas`, `scikit-learn`, `seaborn`, `notebook`, dan `jupyter` secara global di sistem user.

Setelah menjalankan perintah ini, user seharusnya memiliki semua package yang diperlukan dan siap untuk digunakan.

Business Dashboard
------------------

Dashboard ini menampilkan informasi penting tentang tingkat attrition karyawan, faktor-faktor yang memengaruhinya, dan bagaimana attrition tersebut bervariasi berdasarkan departemen, peran pekerjaan, tingkat pendidikan dan lain-lain. Dashboard ini bertujuan untuk membantu manajemen memahami situasi terkini dan mengidentifikasi area yang memerlukan perhatian khusus.

[Link dashboard](https://public.tableau.com/views/Dicoding_Submission1/Dashboard1?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link)

Attrition Predictor Application
----------
Seperti yang sudah dibahas pada cakupan proyek, kami juga menyediakan aplikasi prediksi attrition karyawan sederhana menggunakan tkinter sebagai GUI.

### Setting Up the Environment (Application)

Ikuti langkah-langkah berikut untuk mengatur environment dengan packages yang diperlukan:

#### Prerequisites

- Python (version 3.7 or higher)
- pip (Python package installer)

#### Install Required Packages
Buka terminal atau command prompt, ubah direktori sesuai dengan lokasi aplikasi berada dan jalankan perintah berikut untuk menginstal paket yang diperlukan dari file `requirements.txt`:

`pip install -r requirements.txt`

Perintah diatas akan menginstal versi yang ditentukan dari requirements.txt secara global di sistem user.

Setelah menjalankan perintah ini, user dapat mencoba menjalankan aplikasi dengan mengikuti langkah-langkah berikut ini.

#### Step 1
Buka folder `Deployment` lalu buka aplikasi app.py

#### Step 2
Masukkan nilai-nilai yang menjadi faktor kemungkinan karyawan melakukan attrition.

#### Step 3
Setelah semua form diisi, klik Predict maka di paling bawah antarmuka aplikasi akan keluar hasil prediksinya.

Happy Predict!

Conclusion
----------

Berdasarkan analisis data dari dashboard Dicoding Attrition, dapat disimpulkan beberapa informasi penting sebagai berikut:

-  Tingkat attrition di perusahaan ini adalah 16.9%, dengan total 179 karyawan melakukan attition dengan total keseluruhan 1058 karyawan.
- Secara gender, karyawan laki-laki mendominasi tingkat attrition dengan persentase 60,34%, sedangkan karyawan perempuan 39,66%.
- Departemen dengan tingkat attrition tertinggi adalah Penelitian & Pengembangan (Research & Development) dengan persentase 59,78%, diikuti oleh Sumber Daya Manusia (Human Resources) 36,87%, dan Penjualan (Sales) 3,35%.
- Berdasarkan tingkat pendidikan, karyawan dengan gelar Sarjana (Bachelor) memiliki tingkat attrition tertinggi, diikuti oleh karyawan dengan gelar Sarjana (Master), dan terakhir karyawan di bawah tingkat Sarjana (Below College).
- Mayoritas karyawan yang mengalami attrition memiliki jarak tempat tinggal lebih dari 10 km dari kantor, dengan persentase 43,02%.
- Karyawan dengan rentang gaji rendah (0 - 5k) memiliki tingkat attrition yang lebih tinggi dibandingkan dengan rentang gaji yang lebih tinggi.
- Meskipun sebagian besar karyawan yang mengalami attrition menilai keseimbangan antara kehidupan kerja dan pribadi (Work-Life Balance) cukup baik dengan mayoritas menilai 3 dari skala 4, namun mereka memiliki tingkat kepuasan yang cenderung rendah terhadap lingkungan kerja (Environment Satisfaction) dan pekerjaan (JobSatisfaction) yang dilakukan.

Kesimpulan ini memberikan gambaran umum mengenai pola dan karakteristik karyawan yang mengalami attrition di perusahaan tersebut, yang dapat membantu dalam mengidentifikasi faktor-faktor penyebab dan mengambil langkah-langkah perbaikan yang diperlukan.

### Rekomendasi Action Items

- Melakukan analisis lebih mendalam untuk mengidentifikasi faktor-faktor utama yang menyebabkan tingginya tingkat attrition karyawan dan mengembangkan strategi untuk mengatasi masalah tersebut, seperti program 
retensi karyawan, peningkatan kompensasi, atau perbaikan lingkungan kerja.

- Memperluas program perekrutan untuk menarik lebih banyak calon karyawan dengan gelar Bachelor atau mempertimbangkan pelatihan dan pengembangan karyawan yang ada untuk meningkatkan kualifikasi mereka.

- Mengeksplorasi opsi kerja jarak jauh atau menyediakan tempat tinggal berupa mess di kantor untuk mengurangi jarak tempuh karyawan dan meningkatkan keseimbangan kehidupan-kerja.
