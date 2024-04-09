import customtkinter
import customtkinter
import PIL as pil

# Zadanie 1
# W tym zadaniu okno loginu do Banku jest już gotowe. Niestety brakuje w nim części odpowiedzialnej za logowanie.
# Twoim zadaniem jest dodać elementy CTkEntry odpowiedzialne za wprowadzenie maila i hasła oraz przycisk CTkButton
# odpowiedzialny za zalogowanie. Po kliknięciu przycisku zaloguj, program powinien wypisywać dane na konsoli.

# Linki do dokumentacji Button i Entry:
# https://github.com/TomSchimansky/CustomTkinter/wiki/CTkButton
# https://github.com/TomSchimansky/CustomTkinter/wiki/CTkEntry

window = customtkinter.CTk()
window.geometry("420x740")
window.title("Zad1")

# Dodatki estetyczne
Magenta_Circle_img = customtkinter.CTkImage(dark_image=pil.Image.open("Circle_magenta.png"), size=(150, 150))
Magenta_Cirlce_Label = customtkinter.CTkLabel(window, image=Magenta_Circle_img, text="")
Magenta_Cirlce_Label.place(x=30, y=50, anchor="center")

Yellow_Circle_img = customtkinter.CTkImage(dark_image=pil.Image.open("Circle_yellow.png"), size=(200, 200))
Yellow_Cirlce_Label = customtkinter.CTkLabel(window, image=Yellow_Circle_img, text="")
Yellow_Cirlce_Label.place(x=350, y=200, anchor="nw")

Blue_Circle_img = customtkinter.CTkImage(dark_image=pil.Image.open("Circle_blue.png"), size=(300, 300))
Blue_Cirlce_Label = customtkinter.CTkLabel(window, image=Blue_Circle_img, text="")
Blue_Cirlce_Label.place(x=300, y=700, anchor="center")

# Logo banku
Bank_Logo = customtkinter.CTkLabel(window, height=110, width=110, fg_color="#E62569", text="Py", font=("Arial Rounded MT Bold", 60),
                                 text_color="white", corner_radius=20)
Bank_Logo.place(relx=0.5, rely=0.3, anchor="e")
Bank_Text = customtkinter.CTkLabel(window, height=110, width=110, text="Bank", font=("Arial Rounded MT Bold", 50), text_color="black")
Bank_Text.place(relx=0.5, rely=0.3, anchor="w")

# Tutaj dodaj elementy interfejsu, pamiętająć żeby znajduowały się poniżej Logo banku

entry=customtkinter.CTkEntry(window, placeholder_text="login", width=150, height=20)
entry.place(relx=0.5, rely=0.5, anchor="center")
entry=customtkinter.CTkEntry(window, placeholder_text="password", width=150, height=20)
entry.place(relx=0.5, rely=0.54, anchor="center")

window.mainloop()
