# 🍗 Los Pollos Hermanos — Restaurant Information System

> "When you’re here, you’re family. And chicken is our legacy." 🐓🔥

Sebuah **sistem informasi berbasis web** yang dikembangkan dengan **Django Framework** untuk mengelola restoran fiktif *Los Pollos Hermanos*.  
Website ini mencakup fitur **pemesanan online, manajemen menu, reservasi, dan laporan penjualan** untuk mendukung operasional restoran modern.

---

## 🚀 Tech Stack

- **Framework:** Django (Python)  
- **Database:** SQLite / PostgreSQL  
- **Frontend:** Django Template + Bootstrap  
- **Version Control:** Git & GitHub  

---

## 👥 Team Members

| Nama | Role |
|------|------|
| 🧑‍💻 M. Manunggaling Aji P | **Fullstack Developer** |
| ⚙️ Sheva Arvandi | **Backend Developer** |
| 📂 Fika Karuna Saputri | **Project Management** |
| 🎨 Arif Fadillah | **UI/UX Designer** |
| 📝 Nanda Asfa Priyambada | **Documentation Project** |
| 🧪 M. Ibnu Naziep | **QA Tester** |

---

## 📸 Preview (Mockup)

![Preview Website](https://via.placeholder.com/800x400?text=Los+Pollos+Hermanos+Django+Website)

---

## 📌 Features

✅ Manajemen menu makanan & minuman  
✅ Pemesanan online (order system)  
✅ Reservasi meja restoran  
✅ Dashboard admin (laporan, pelanggan, stok)  
✅ Sistem login user & staff  

---

## 🏗️ System Architecture

```mermaid
graph TD
A[User] --> B[Django Views + Template]
B --> C[Django Models]
C --> D[Database]

# clone repo
git clone https://github.com/ajipangestuu/los-pollos-hermanos.git

# masuk folder
cd los-pollos-hermanos

# install virtualenv (kalau belum ada)
pip install virtualenv

# buat virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# install dependencies
pip install -r requirements.txt

# migrasi database
python manage.py migrate

# jalankan server
python manage.py runserver

✨ Credits

Made with ❤️ by Kelompok Los Pollos Hermanos Team
📅 Tahun: 2025
