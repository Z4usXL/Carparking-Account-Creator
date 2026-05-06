🚗 Car Parking Multiplayer Account Generator

Bu proje, belirli bir API endpoint’ine istek göndererek rastgele e-posta adresleri ile hesap oluşturmayı otomatikleştiren bir Python scriptidir.

---

⚙️ Özellikler

- 🎲 Rastgele e-posta oluşturma
- 🔁 Sürekli çalışan worker sistemi
- 🌐 Proxy desteği (opsiyonel)
- 💾 Oluşturulan hesapları dosyaya kaydetme
- 🧵 Thread (çoklu işlem) desteği

---

🧠 Çalışma Mantığı

- "mm()" → Rastgele email üretir
- "worker()" → API’ye istek gönderir
- Başarılı olursa:
  - Hesap bilgilerini alır
  - Dosyaya kaydeder
- Thread sayesinde sürekli tekrar eder

---

📦 Gereksinimler

pip install requests

---

🚀 Kullanım

python script.py

✔️ Başarılı hesaplar:

- Terminalde gösterilir
- "cpm.txt" dosyasına kaydedilir

---

📁 Dosya Yapısı

.
├── script.py
├── cpm.txt

---

🌐 Proxy Kullanımı

pp = [
    "ip:port",
    "ip:port"
]

---

🛑 Durdurma

CTRL + C

---

⚠️ Uyarı

Bu script:

- Eğitim amaçlıdır
- API kullanım şartlarına aykırı olabilir
- Sorumluluk kullanıcıya aittir
