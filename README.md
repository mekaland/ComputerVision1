# Görseli Siyah Beyaza Çevirme Uygulaması

Bu proje, kullanıcıların yükledikleri renkli görüntüleri siyah beyaz (gri tonlamalı) görüntülere dönüştüren bir web uygulamasıdır. Uygulama, [Gradio](https://gradio.app/) kütüphanesi kullanılarak oluşturulmuş bir arayüze sahiptir ve [OpenCV](https://opencv.org/) ile görüntü işleme işlemlerini gerçekleştirir.

## Özellikler

- **Görüntü Yükleme:** Kullanıcılar, bilgisayarlarından bir görüntü yükleyebilirler.
- **Gri Tonlamaya Dönüştürme:** Yüklenen renkli görüntü, gri tonlamalı bir görüntüye dönüştürülür.
- **Sonuç Görüntüleme:** Dönüştürülen gri tonlamalı görüntü, kullanıcıya gösterilir.

## Kullanılan Teknolojiler

- **Python:** Projenin temel programlama dili.
- **Gradio:** Web arayüzü oluşturmak için kullanılır.
- **OpenCV:** Görüntü işleme işlemleri için kullanılır.
- **NumPy:** Görüntü verilerini işlemek için kullanılır.

## Kurulum ve Çalıştırma

1. **Gereksinimleri Yükleyin:** Aşağıdaki komutu kullanarak gerekli Python paketlerini yükleyin:

    ```bash
    pip install -r requirements.txt
    ```

2. **Uygulamayı Başlatın:** Aşağıdaki komutu kullanarak uygulamayı çalıştırın:

    ```bash
    python app.py
    ```

3. **Web Arayüzüne Erişin:** Tarayıcınızda `http://localhost:7860` adresine giderek uygulamayı kullanabilirsiniz.

## Dosya Yapısı

- `app.py`: Uygulamanın ana Python dosyası.
- `requirements.txt`: Proje için gerekli Python paketlerini listeleyen dosya.

## Nasıl Kullanılır

1. **Görüntü Yükleyin:** "Görseli siyah beyaza çevir" başlığı altındaki yükleme alanını kullanarak bir görüntü seçin.
2. **Dönüştürme İşlemi:** "Çevir" butonuna tıklayın.
3. **Sonucu Görüntüleyin:** Dönüştürülen gri tonlamalı görüntü, arayüzde görüntülenecektir.

## Canlı Demo

Uygulamayı canlı olarak deneyimlemek için aşağıdaki bağlantıyı kullanabilirsiniz:

[https://huggingface.co/spaces/kadirland/nostalaji](https://huggingface.co/spaces/kadirland/nostalaji)

## Katkıda Bulunun

Herhangi bir hata bildirimi veya iyileştirme öneriniz varsa, lütfen bir [issue](https://github.com/kullaniciadi/proje-adi/issues) oluşturun veya bir [pull request](https://github.com/kullaniciadi/proje-adi/pulls) gönderin.

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.
