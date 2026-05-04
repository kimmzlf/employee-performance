# Employee Performance and Productivity Data

## Repository Outline
```
1. README.md - Penjelasan gambaran umum project
2. DAG.py - Berisi penggunaan airflow  
3. DAG_graph.png - Screenshot alur graph DAG  
4. GX.ipynb - Penerapan Great Expectation    
5. data_raw.csv - Data original 
6. data_clean.csv - Data yang telah dilakukan Data Cleaning  
7. ddl.txt - Berisi query sql pembuatan table dan input data pada table  
8. images - Folder berisi screenshot hasil visualisasi yang dibuat

```

## Problem Background
Bagi sebuah perusahaan, proses rekrutmen dan training karyawan baru membutuhkan biaya dan waktu yang sangat besar. Tingkat turnover (karyawan yang resign) yang tinggi akan merugikan perusahaan secara finansial dan menghambat laju proyek. Seringkali, karyawan berkinerja tinggi atau yang sudah lama bekerja memutuskan keluar karena masalah yang sebenarnya bisa dideteksi lebih awal, seperti beban kerja yang tidak seimbang (lembur berlebihan), kurangnya apresiasi (promosi), atau ketidakcocokan sistem kerja (remote vs. office).

## Project Output
Output dari project ini adalah visualisasi Dashboard menggunakan kibana dari ElasticSearch.

## Data
Sumber Data : https://www.kaggle.com/datasets/mexwell/employee-performance-and-productivity-data/data

| Feature                        | Deskripsi |
|--------------------------------|----------|
| Employee_ID                    | ID unik untuk setiap karyawan |
| Department                     | Departemen tempat karyawan bekerja (misalnya: Sales, HR, IT) |
| Gender                         | Jenis kelamin karyawan (Laki-laki, Perempuan, Lainnya) |
| Age                            | Usia karyawan (antara 22 hingga 60 tahun) |
| Job_Title                      | Jabatan karyawan (misalnya: Manager, Analyst, Developer) |
| Hire_Date                      | Tanggal karyawan mulai bekerja |
| Years_At_Company               | Lama bekerja di perusahaan (dalam tahun) |
| Education_Level                | Tingkat pendidikan terakhir (SMA, Sarjana, Magister, Doktor) |
| Performance_Score              | Penilaian kinerja karyawan (skala 1 hingga 5) |
| Monthly_Salary                 | Gaji bulanan dalam USD, berkorelasi dengan jabatan dan performa |
| Work_Hours_Per_Week            | Jumlah jam kerja per minggu |
| Projects_Handled               | Total proyek yang ditangani |
| Overtime_Hours                 | Total jam lembur dalam satu tahun terakhir |
| Sick_Days                      | Jumlah hari sakit yang diambil |
| Remote_Work_Frequency          | Persentase kerja jarak jauh (0%, 25%, 50%, 75%, 100%) |
| Team_Size                      | Jumlah anggota dalam tim |
| Training_Hours                 | Jumlah jam pelatihan yang diikuti |
| Promotions                     | Jumlah promosi selama bekerja |
| Employee_Satisfaction_Score    | Tingkat kepuasan karyawan (skala 1.0 hingga 5.0) |
| Resigned                       | Status apakah karyawan telah resign (Ya / Tidak) |


## Stacks
Programming Language : 
- Python 

Libraries : 
- Pandas  
- psycopg2  
- elasticsearch  
- airflow  
- great_expectations  
- datetime

Tools : 
- Visual Studio Code 
- Docker  
- Kibana  
- Postgresql


---
