# Kahve Sipariş Uygulaması

Bu proje, Python kullanılarak geliştirilmiş, genişletilebilir ve test edilebilir bir konsol tabanlı kahve sipariş simülasyonudur. 
Nesne Yönelimli Programlama (OOP) prensipleri ve Temiz Kod (Clean Code) standartları gözetilerek tasarlanmıştır.

## Özellikler

* Tanımlı kahve çeşitleri ve fiyat listesi
* Her kahve için detaylı tarif bilgisi
* Kullanıcıdan konsol üzerinden seçim alma
* Çıkış (exit) seçeneği
* Sayı ve doz formatı desteği
* Geçersiz girişlerde hata yönetimi ve menü tekrarı
* Sipariş hazırlama ve açıklama metni üretimi
* Pytest ile yazılmış kapsamlı birim testler

## Mimari Yapı

```text
kafe_app/
│
├── main.py                 # Program giriş noktası
├── menu.py                 # Menü ve tarif oluşturma
├── models.py               # Sipariş veri modelleri
├── exceptions.py           # Özel exception sınıfı
├── OrderMessageBuilder.py  # Sipariş açıklayıcı (metin üretici)
│
└── tests/                  # Pytest birim testleri
```
Kurulum
Sanal ortam oluşturma:

```bash

python -m venv .venv
```
Ortamı aktif etme (Windows):

```bash

.\.venv\Scripts\activate
```
Bağımlılıkları yükleme:

```bash
pip install -r requirements.txt
```
Çalıştırma
Uygulamayı başlatmak için:

```bash
python main.py
```
Test Çalıştırma
Testleri koşturmak için:

```bash
pytest -v
```
Geliştiren: Ozan Parlayan
