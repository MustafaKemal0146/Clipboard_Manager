# 📋 Clipboard Manager

Bu proje, kopyaladığınız yazıları kaydeden ve bir kısayol tuşu (`CTRL+SHIFT+V`) ile hızlıca erişmenizi sağlayan bir **Clipboard Manager** uygulamasıdır.

---

## 🛠 Gereksinimler

- Python 3
- `python3-tk`
- `pyperclip`
- `keyboard`
- `xclip` (veya `xsel`) - Linux'ta clipboard yönetimi için

Kurulum:
```bash
sudo apt update
sudo apt install python3 python3-tk xclip
pip3 install pyperclip keyboard
```

---

## 🚀 Uygulamayı Başlatma

Geçici çalıştırmak istersen:
```bash
sudo python3 main.py
```
> Not: `keyboard` kütüphanesi Linux'ta root yetkisi gerektirir.

---

## 🔥 Uygulamayı Arka Planda Sürekli Çalıştırmak (Sistem Servisi)

Uygulamayı sürekli çalıştırmak için bir **systemd servisi** tanımlayabiliriz.

1. Aşağıdaki dosyayı oluştur:

```bash
sudo nano /etc/systemd/system/clipboard_manager.service
```

2. İçerisine şunu yapıştır:

```ini
[Unit]
Description=Clipboard Manager Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/kullanici_adi/Desktop/Clipboard_Manager/main.py
WorkingDirectory=/home/kullanici_adi/Desktop/Clipboard_Manager
Restart=always
User=kullanici_adi

[Install]
WantedBy=multi-user.target
```

> DİKKAT:  
> `/home/kullanici_adi/` ve `kullanici_adi` kısımlarını kendi kullanıcı adınla değiştir.

---

3. Servisi aktif hale getir:

```bash
sudo systemctl daemon-reload
sudo systemctl enable clipboard_manager.service
sudo systemctl start clipboard_manager.service
```

Servis durumunu kontrol etmek için:

```bash
sudo systemctl status clipboard_manager.service
```

Servisi durdurmak için:

```bash
sudo systemctl stop clipboard_manager.service
```

---

## 🐛 Olası Hatalar ve Çözümleri

- `Pyperclip could not find a copy/paste mechanism`:  
  Çözüm:  
  ```bash
  sudo apt install xclip
  ```

- `You must be root to use this library`:  
  Çözüm:  
  `sudo` kullanarak scripti çalıştır.
