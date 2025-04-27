# Clipboard Manager

Clipboard geçmişini yöneten basit bir Python uygulamasıdır.  
Bu uygulama arka planda bir servis olarak çalışır ve kopyalanan içerikleri yönetir.

---

## Gereksinimler

- Python 3
- pip paket yöneticisi
- `xclip` (Linux üzerinde pyperclip kütüphanesi için gereklidir)

### Gerekli Python kütüphanelerini kurmak için:

```bash
pip install -r requirements.txt
```

`requirements.txt` içeriği:

```
pyperclip
keyboard
```

---

## Sistem Servisi Kurulumu

Uygulamayı sürekli arka planda çalıştırmak için bir **systemd** servisi oluşturuyoruz.

1. Servis dosyasını oluştur:

```bash
sudo nano /etc/systemd/system/clipboard_manager.service
```

İçine şunları yapıştır:

```ini
[Unit]
Description=Clipboard Manager Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/solussola/Desktop/Clipboard_Manager/main.py
WorkingDirectory=/home/solussola/Desktop/Clipboard_Manager
Restart=always

[Install]
WantedBy=multi-user.target
```

Düzenlemeyi kaydetmek için:  
**CTRL + O** → Enter → **CTRL + X**

---

2. Değişiklikleri sisteme okut:

```bash
sudo systemctl daemon-reload
```

3. Servisi başlat ve otomatik başlasın diye aktif et:

```bash
sudo systemctl enable clipboard_manager
sudo systemctl start clipboard_manager
```

4. Servis durumunu kontrol et:

```bash
sudo systemctl status clipboard_manager
```

Başarıyla çalışıyorsa şöyle bir çıktı göreceksiniz:

```
● clipboard_manager.service - Clipboard Manager Service
     Active: active (running)
```

---

## Ekstra

Eğer clipboard ile ilgili hata alırsanız, şu paketleri kurmayı unutmayın:

```bash
sudo apt update
sudo apt install xclip
```

---

## Notlar

- Servis **root yetkisi** ile çalışmaktadır. Çünkü `keyboard` kütüphanesi düşük seviyeli giriş yakalama (hotkey dinleme) için root izinlerine ihtiyaç duyar.
- Servis dosyasındaki `User=` satırı bu yüzden kaldırılmıştır.

---
