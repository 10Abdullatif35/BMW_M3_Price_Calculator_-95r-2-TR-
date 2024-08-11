# BMW_M3_Price_Calculator_-95r-2-TR-

# BMW Araç Fiyat Tahmin Projesi

## Genel Bakış

Bu proje, derin öğrenme modeli kullanarak BMW araçlarının fiyatlarını tahmin etmek amacıyla tasarlanmıştır. Uygulama, veri ön işleme, model eğitimi ve test edilmesi ile Tkinter tabanlı kullanıcı dostu bir arayüz içermektedir.

## Proje Yapısı

- **Data_Preprocessing.ipynb**: Araç veri setini ön işlemek için gerekli adımları içeren bir Jupyter Notebook.
- **Model_Test__95_R^2.ipynb**: Model test sürecini gösteren ve modelin %95 R² skorunu elde ettiğini gösteren bir Jupyter Notebook.
- **DeepLearning_Model.py**: Derin öğrenme modelinin tanımlandığı ve eğitildiği Python dosyası.
- **App_Interface.py**: Kullanıcıların araç özelliklerini girmesi ve fiyat tahmini alması için Tkinter tabanlı bir grafik kullanıcı arayüzü (GUI) sağlayan bir Python dosyası.

## Kullanılan Teknolojiler

- **Python 3.x**
- **TensorFlow/Keras** derin öğrenme modelini oluşturmak ve eğitmek için.
- **Pandas & NumPy** veri manipülasyonu ve ön işleme için.
- **Tkinter** GUI oluşturmak için.
- **PIL (Pillow)** Tkinter arayüzünde resim işleme ve görüntüleme için.
- **Jupyter Notebook** veri ön işleme ve model performansını deneyimlemek ve görselleştirmek için.

## Kurulum Talimatları

1. **Depoyu klonlayın:**
2. **Gerekli Python kütüphanelerini yükleyin:**
3. **Önceden eğitilmiş modeli indirin:**
   - Model dosyasının (`car_price_model578.keras`) `App_Interface.py` ile aynı dizinde olduğundan emin olun.
   - Eğer model dosyasına sahip değilseniz, `DeepLearning_Model.py` kullanarak eğitebilirsiniz.
4. **Uygulamayı çalıştırın:**
   ```bash
   python App_Interface.py
   ```
## Kullanım

- **Araç özelliklerini girin**: Kullanıcı `Kilometre`, `Motor Hacmi`, `Motor Gücü` gibi belirli özellikleri manuel olarak girmeli ve `Yıl`, `Vites Tipi`, `Yakıt Tipi` gibi özellikler için açılır menülerden seçim yapmalıdır.
- **Fiyat tahmini alın**: Girilen özelliklere dayalı olarak tahmin edilen fiyatı almak için "Hesapla" butonuna tıklayın.

## Örnek

- **Yıl**: 2018
- **Kilometre**: 40000
- **Motor Hacmi**: 1600
- **Motor Gücü**: 120
- **Vites Tipi**: Otomatik
- **Yakıt Tipi**: Benzin
- **Kasa Tipi**: Sedan
- **Renk**: Beyaz
- **Çekiş**: Önden Çekiş
- **Kimden**: Sahibinden
- **Model**: 320i Sport Line

Bu bilgileri girdikten ve "Hesapla" butonuna tıkladıktan sonra, uygulama tahmin edilen fiyatı gösterecektir.

## Geliştirilebilecek  Taraflar

- Modeli diğer araç markaları ve modellerini içerecek şekilde genişletin.
- Kullanıcı arayüzünü daha etkileşimli öğelerle geliştirin.
- Model tahminlerinin doğru kalmasını sağlamak için gerçek zamanlı veri güncellemeleri entegre edin.

# BMW Car Price Prediction Project

## Overview

This project is designed to predict the prices of BMW cars using a deep learning model. The application includes data preprocessing, model training and testing, and a user-friendly interface built with Tkinter.

## Project Structure

- **Data_Preprocessing.ipynb**: A Jupyter Notebook that contains all the necessary steps for preprocessing the car dataset.
- **Model_Test__95_R^2.ipynb**: A Jupyter Notebook that demonstrates the model testing process and shows that the model achieved an R² score of 95%.
- **DeepLearning_Model.py**: A Python script where the deep learning model is defined and trained.
- **App_Interface.py**: A Python script that provides a Tkinter-based graphical user interface (GUI) for users to input car features and get price predictions.

## Technologies Used

- **Python 3.x**
- **TensorFlow/Keras** for building and training the deep learning model.
- **Pandas & NumPy** for data manipulation and preprocessing.
- **Tkinter** for building the GUI.
- **PIL (Pillow)** for handling and displaying images in the Tkinter interface.
- **Jupyter Notebook** for experimenting and visualizing data preprocessing and model performance.

## Setup Instructions

1. **Clone the repository:**
2. **Install the necessary Python libraries:**

3. **Download the pre-trained model:**
   - Ensure that the model file (`car_price_model578.keras`) is in the same directory as `App_Interface.py`.
   - If you don't have the model file, you can train it using `DeepLearning_Model.py`.

4. **Run the application:**
   ```bash
   python App_Interface.py
   ```
## Usage

- **Input the car's features**: The user will need to manually input certain features such as `Kilometre`, `Motor Hacmi`, `Motor Gücü`, and select options from dropdown menus for features like `Yıl`, `Vites Tipi`, `Yakıt Tipi`, etc.
- **Get the price prediction**: Click on the "Hesapla" button to get the predicted price based on the input features.

## Example

- **Year**: 2018
- **Kilometre**: 40000
- **Motor Hacmi**: 1600
- **Motor Gücü**: 120
- **Vites Tipi**: Otomatik
- **Yakıt Tipi**: Benzin
- **Kasa Tipi**: Sedan
- **Renk**: Beyaz
- **Çekiş**: Önden Çekiş
- **Kimden**: Sahibinden
- **Model**: 320i Sport Line

After entering these details and clicking "Hesapla", the application will display the predicted price.


---


