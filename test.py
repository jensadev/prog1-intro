
# Äventyr: Buffé och magont med [att spara] och [att välja] - Tkinter-version
import tkinter as tk
from tkinter import messagebox


def visa_resultat(val):
    if val == "sallad":
        messagebox.showinfo(
            "Resultat", "Du äter sallad. Fräscht och gott! Du mår bra.")
    elif val == "kyckling":
        messagebox.showinfo(
            "Resultat", "Du äter kyckling. Mums! Men du känner dig lite konstig i magen.")
    elif val == "skaldjur":
        messagebox.showinfo(
            "Resultat", "Du äter skaldjur. Det smakar bra, men efter en stund får du ont i magen!")
    elif val == "glass":
        messagebox.showinfo(
            "Resultat", "Du äter glass. Gott! Men du får lite ont i magen av all socker.")
    else:
        messagebox.showinfo(
            "Resultat", "Du valde något som inte fanns på buffén. Du går hungrig därifrån.")


root = tk.Tk()
root.title("Buffé-äventyr")

label = tk.Label(root, text="Du är på en buffé. Vad vill du äta?")
label.pack(pady=10)

for mat in ["sallad", "kyckling", "skaldjur", "glass"]:
    btn = tk.Button(root, text=mat.capitalize(), width=20,
                    command=lambda m=mat: visa_resultat(m))
    btn.pack(pady=2)

root.mainloop()
