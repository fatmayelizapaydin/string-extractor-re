<div align="center">
  <a href="https://istinye.edu.tr">
    <img src="https://upload.wikimedia.org/wikipedia/tr/c/c5/Istinye_Universitesi_logo.png" alt="Istinye University" width="180"/>
  </a>

  # ReStatic: Automated Static Analysis & Intelligence Tool

  ![GitHub](https://img.shields.io/badge/GitHub-Public-blue?style=flat-square&logo=github)
  ![Language](https://img.shields.io/badge/Language-Python-blue?style=flat-square)
  ![Status](https://img.shields.io/badge/Status-Completed-green?style=flat-square)
  ![Course](https://img.shields.io/badge/Course-BGT210-purple?style=flat-square)
  ![License](https://img.shields.io/badge/License-Educational-green?style=flat-square)
</div>

---

## 🎓 Instructor / Danışman
| | |
|---|---|
| **Name / Ad** | Keyvan Arasteh |
| **GitHub** | [@keyvanarasteh](https://github.com/keyvanarasteh) |
| **Email** | [keyvan.arasteh@istinye.edu.tr](mailto:keyvan.arasteh@istinye.edu.tr) |

## 👤 Student / Öğrenci
| | |
|---|---|
| **Name / Ad Soyad** | Fatma Yeliz Apaydın |
| **Student ID / Öğrenci No** | `[Numaranızı Buraya Yazın]` |

## 📚 Course Information / Ders Bilgileri
| | |
|---|---|
| **Course Name / Ders Adı** | Reverse Engineering (Tersine Mühendislik) |
| **Course Code / Ders Kodu** | BGT210 |
| **Semester / Dönem** | 2025-2026 Spring (Bahar) |
| **Institution / Üniversite** | [Istinye University](https://istinye.edu.tr) |

---

## 📋 Project Overview / Proje Özeti
**ReStatic**, statik analiz süreçlerini hızlandırmak ve hedef ikili (binary) dosyalar, APK paketleri veya ham log verileri içerisindeki gizli IoC (Indicators of Compromise) verilerini otomatik olarak ayıklamak için geliştirilmiş bir güvenlik aracıdır. Proje, özellikle tersine mühendislik aşamalarındaki "hızlı ön analiz" ihtiyacını karşılamak amacıyla tasarlanmıştır.

## 🔬 Methodology / Metodoloji
Proje, ders kapsamında işlenen statik analiz prensiplerine dayanmaktadır. Uygulama, belirtilen veri setlerini Regex (Düzenli İfadeler) motoru ile tarar ve bulguları kritiklik seviyelerine göre sınıflandırır:
1. **Pattern Matching:** Hassas verileri (API keyler, tokenlar, şifreler) tespit etmek için özelleştirilmiş desen eşleme.
2. **Data Extraction:** URL, IP adresi ve e-posta gibi ağ verilerinin yapısal olarak ayrıştırılması.
3. **Risk Categorization:** Tespit edilen verilerin "Kritik", "Orta" ve "Düşük" seviyelerine göre puanlanması.

## 🗂 Repository Structure / Repo Yapısı
```text
.
├── README.md           # Teknik dokümantasyon
├── src/
│   └── main.py         # Çekirdek analiz motoru
└── docs/
    └── research/       # Araştırma notları# string-extractor-re
## 🚀 Getting Started / Kurulum
Projenin yerel ortamda çalıştırılması için herhangi bir ek kütüphane kurulumu gerekmemektedir; Python standart kütüphaneleri yeterlidir.

1. Repoyu klonlayın:
```bash
   git clone [https://github.com/fatmayelizapaydin/string-extractor-re](https://github.com/fatmayelizapaydin/string-extractor-re)
---

## 🛠️ Technical Details / Teknik Detaylar
- **Regex Engines:** Veri ayıklama süreçlerinde Python'ın `re` modülü kullanılarak yüksek performanslı desen eşleme sağlanmıştır.
- **Complexity Analysis:** Proje, O(n) zaman karmaşıklığı ile çalışarak büyük boyutlu log dosyalarında bile verimli analiz sunar.
- **Zero-Dependency Policy:** Bağımlılık (dependency) sorunlarını ortadan kaldırmak için sadece Python standart kütüphaneleri kullanılmıştır.

## ⚠️ Security Policy / Güvenlik Politikası
Bu araç, statik analiz süreçlerini hızlandırmak amacıyla tasarlanmıştır. Kullanıcıların, üzerinde analiz yaptıkları dosyaların telif ve güvenlik haklarına riayet etmeleri beklenir. Yalnızca yetkili olduğunuz sistemlerde kullanın.
