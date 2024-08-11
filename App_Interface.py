import tkinter as tk
from tkinter import ttk
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image, ImageTk

# Load the pre-trained model
from DeepLearning_Model import scaler
model = load_model('car_price_model578.keras')  # Adjust the path as necessary
def tahmin_et():
    try:
        # Get user input
        yil = int(yil_kutu.get())
        kilometre = int(kilometre_entry.get())
        motor_hacmi = int(motor_hacmi_entry.get())
        motor_gucu = int(motor_gucu_entry.get())

        # Get values from comboboxes
        vites_tipi = vites_tipi_kutu.get()
        yakit_tipi = yakit_tipi_kutu.get()
        kasa_tipi = kasa_tipi_kutu.get()
        renk = renk_kutu.get()
        cekis = cekis_kutu.get()
        kimden = kimden_kutu.get()
        model_name = model_kutu.get()

        # Prepare input for the model
        input_features = np.zeros(89)
        input_features[0] = yil
        input_features[1] = kilometre
        input_features[2] = motor_hacmi
        input_features[3] = motor_gucu

        # Map combobox values to indices
        vites_tipi_dict = {"Düz": 0, "Otomatik": 1, "Yarı Otomatik": 2}
        yakit_tipi_dict = {"Benzin": 0, "Dizel": 1, "LPG & Benzin": 2}
        kasa_tipi_dict = {"Cabrio": 0, "Coupe": 1, "Hatchback": 2, "Sedan": 3, "Station wagon": 4}
        renk_dict = {"Beyaz": 0, "Diğer": 1, "Gri": 2, "Mavi": 3, "Siyah": 4}
        cekis_dict = {"4WD (Sürekli)": 0, "Arkadan İtiş": 1, "Önden Çekiş": 2}
        kimden_dict = {"Galeriden": 0, "Sahibinden": 1}
        model_dict = {
            "316i Advantage": 0, "316i Comfort": 1, "316i Compact": 2, "316i Luxury Line": 3,
            "316i M Sport": 4, "316i Modern Line": 5, "316i Premium": 6, "316i Sport Line": 7,
            "316i Standart": 8, "316i Techno Plus": 9, "316i Technology": 10, "316ti Compact": 11,
            "318d M Plus": 12, "318d Sport Plus": 13, "318i 40th Year Edition": 14, "318i Edition M Sport": 15,
            "318i Edition Sport Line": 16, "318i Joy": 17, "318i Premium Line": 18, "318i Prestige": 19,
            "318i Standart": 20, "318is": 21, "318ti Compact": 22, "320Ci": 23, "320d Advantage": 24,
            "320d Comfort": 25, "320d Edition Comfort": 26, "320d Edition Sport Line": 27, "320d M Sport": 28,
            "320d Modern Line": 29, "320d Premium": 30, "320d Premium Line": 31, "320d Sport Line": 32,
            "320d Standart": 33, "320d Techno Plus": 34, "320d Touring": 35, "320d xDrive M Sport": 36,
            "320d xDrive Sport Line": 37, "320d xDrive Techno Plus": 38, "320i": 39, "320i 50th Year M Edition": 40,
            "320i Cabrio": 41, "320i Coupe": 42, "320i ED 40th Year Edition": 43, "320i ED Luxury Line": 44,
            "320i ED Luxury Line Plus": 45, "320i ED M Plus": 46, "320i ED Modern Line": 47, "320i ED Modern Line Plus": 48,
            "320i ED Sport Line": 49, "320i ED Sport Plus": 50, "320i ED Standart": 51, "320i ED Techno Plus": 52,
            "320i Edition M Sport": 53, "320i Executive M Sport": 54, "320i First Edition Luxury Line": 55,
            "320i First Edition M Sport": 56, "320i First Edition Sport Line": 57, "320i M Sport": 58,
            "320i Premium": 59, "320i Sport Line": 60, "325i Standart": 61, "328i M Sport": 62, "Diğer": 63
        }

        # Update input features array based on combobox selections
        input_features[5 + vites_tipi_dict.get(vites_tipi, 0)] = 1
        input_features[8 + yakit_tipi_dict.get(yakit_tipi, 0)] = 1
        input_features[11 + kasa_tipi_dict.get(kasa_tipi, 0)] = 1
        input_features[16 + renk_dict.get(renk, 0)] = 1
        input_features[21 + cekis_dict.get(cekis, 0)] = 1
        input_features[24 + kimden_dict.get(kimden, 0)] = 1
        input_features[26 + model_dict.get(model_name, 0)] = 1

        ## Scaling
        input_features_scaled = scaler.transform([input_features])

        # Model predictions
        prediction = model.predict(input_features_scaled)[0]
        # Ensure prediction is converted to a scalar
        predicted_price = float(prediction)

        # Display the result
        sonuc_label.config(text=f"Hesaplanan Fiyat: {predicted_price:.2f} TL")
    except Exception as e:
        sonuc_label.config(text=f"Bir hata oluştu: {str(e)}")


# Create the main window
pencere = tk.Tk()
pencere.title("BMW M3 Price Calculator")
pencere.geometry("360x640")  # Expanded window size


image = Image.open("BMW_m3.jpg")  # Insert image path here
background_image = ImageTk.PhotoImage(image)

# Create Canvas and add image as background
canvas = tk.Canvas(pencere, width=360, height=640)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Create and place manual input fields
tk.Label(pencere, text="Yıl:").place(x=20, y=70)
yil_kutu = ttk.Combobox(pencere, values=[str(year) for year in range(1980, 2024)])
yil_kutu.place(x=120, y=70)

tk.Label(pencere, text="Kilometre:").place(x=20, y=110)
kilometre_entry = tk.Entry(pencere)
kilometre_entry.place(x=120, y=110)

tk.Label(pencere, text="Motor Hacmi:").place(x=20, y=150)
motor_hacmi_entry = tk.Entry(pencere)
motor_hacmi_entry.place(x=120, y=150)

tk.Label(pencere, text="Motor Gücü:").place(x=20, y=190)
motor_gucu_entry = tk.Entry(pencere)
motor_gucu_entry.place(x=120, y=190)

# Create and place comboboxes for categorical inputs
tk.Label(pencere, text="Vites Tipi:").place(x=20, y=230)
vites_tipi_kutu = ttk.Combobox(pencere, values=["Düz", "Otomatik", "Yarı Otomatik"])
vites_tipi_kutu.place(x=120, y=230)

tk.Label(pencere, text="Yakıt Tipi:").place(x=20, y=270)
yakit_tipi_kutu = ttk.Combobox(pencere, values=["Benzin", "Dizel", "LPG & Benzin"])
yakit_tipi_kutu.place(x=120, y=270)

tk.Label(pencere, text="Kasa Tipi:").place(x=20, y=310)
kasa_tipi_kutu = ttk.Combobox(pencere, values=["Cabrio", "Coupe", "Hatchback", "Sedan", "Station wagon"])
kasa_tipi_kutu.place(x=120, y=310)


tk.Label(pencere, text="Renk:").place(x=20, y=350)
renk_kutu = ttk.Combobox(pencere, values=["Beyaz", "Diğer", "Gri", "Mavi", "Siyah"])
renk_kutu.place(x=120, y=350)

tk.Label(pencere, text="Çekiş:").place(x=20, y=390)
cekis_kutu = ttk.Combobox(pencere, values=["4WD (Sürekli)", "Arkadan İtiş", "Önden Çekiş"])
cekis_kutu.place(x=120, y=390)

tk.Label(pencere, text="Kimden:").place(x=20, y=420)
kimden_kutu = ttk.Combobox(pencere, values=["Galeriden", "Sahibinden"])
kimden_kutu.place(x=120, y=420)

tk.Label(pencere, text="Model:").place(x=20, y=470)
model_kutu = ttk.Combobox(pencere, values=[
    "316i Advantage", "316i Comfort", "316i Compact", "316i Luxury Line", "316i M Sport",
    "316i Modern Line", "316i Premium", "316i Sport Line", "316i Standart",
    "316i Techno Plus", "316i Technology", "316ti Compact", "318d M Plus",
    "318d Sport Plus", "318i 40th Year Edition", "318i Edition M Sport",
    "318i Edition Sport Line", "318i Joy", "318i Premium Line", "318i Prestige",
    "318i Standart", "318is", "318ti Compact", "320Ci", "320d Advantage",
    "320d Comfort", "320d Edition Comfort", "320d Edition Sport Line",
    "320d M Sport", "320d Modern Line", "320d Premium", "320d Premium Line",
    "320d Sport Line", "320d Standart", "320d Techno Plus", "320d Touring",
    "320d xDrive M Sport", "320d xDrive Sport Line", "320d xDrive Techno Plus",
    "320i", "320i 50th Year M Edition", "320i Cabrio", "320i Coupe",
    "320i ED 40th Year Edition", "320i ED Luxury Line", "320i ED Luxury Line Plus",
    "320i ED M Plus", "320i ED Modern Line", "320i ED Modern Line Plus",
    "320i ED Sport Line", "320i ED Sport Plus", "320i ED Standart",
    "320i ED Techno Plus", "320i Edition M Sport", "320i Executive M Sport",
    "320i First Edition Luxury Line", "320i First Edition M Sport",
    "320i First Edition Sport Line", "320i M Sport", "320i Premium",
    "320i Sport Line", "325i Standart", "328i M Sport", "Diğer"
])
model_kutu.place(x=120, y=470)

# Calculate Button
tahmin_butonu = tk.Button(pencere, text="Hesapla", command=tahmin_et)
tahmin_butonu.place(x=120, y=510)

# Result Label
sonuc_label = tk.Label(pencere, text="")
sonuc_label.place(x=120, y=550)

# Mainloop
pencere.mainloop()

