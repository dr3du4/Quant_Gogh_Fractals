
import customtkinter

# Zadanie 2
# W tym zadaniu warto wykazać się kreatywnością! Nasz Bank potrzebuje osobnego okna ustawień.
# Używając różnych elemntów takich jak: CTkSlider, CTkOptionMenu, CTkCheckBox, CTkSwitch, itd.
# stwórz okno, które pozwoli użytkownikowi dostosować ustawienia aplikacji do swoich potrzeb.
# (Wybrane ustawienia nie muszą nic zmieniać w aplikacji, w końcu poruszamy tylko temat GUI :P)
# Minimum 4 różne elementy, ale im więcej tym lepiej! Nie zapomnij też dodać odpowiedni label, aby
# użytkownik wiedział, co dany element zmienia.

# Linki do dokumentacji:
# Slider - https://github.com/TomSchimansky/CustomTkinter/wiki/CTkSlider
# OptionMenu - https://github.com/TomSchimansky/CustomTkinter/wiki/CTkOptionMenu
# CheckBox - https://github.com/TomSchimansky/CustomTkinter/wiki/CTkCheckBox
# Switch - https://github.com/TomSchimansky/CustomTkinter/wiki/CTkCTkSwitch

window = customtkinter.CTk()
window.geometry("420x740")
window.title("Zad2")

# Label "Ustawienia"
Setting_Label = customtkinter.CTkLabel(window, height=60, width=110, padx=10, pady=10, corner_radius=10,
                                          text="Ustawienia", font=("Arial", 30, "bold"), text_color="white", fg_color="#E62569")
Setting_Label.place(relx=0.5, rely=0.1, anchor="center")

# CTkSlider - Slider
slider_label = customtkinter.CTkLabel(window, text="Głośność", font=("Arial", 12))
slider_label.place(relx=0.5, rely=0.25, anchor="center")
slider = customtkinter.CTkSlider(window, from_=0, to=100)
slider.place(relx=0.5, rely=0.3, anchor="center")

# CTkOptionMenu - Option Menu
option_label = customtkinter.CTkLabel(window, text="Język", font=("Arial", 12))
option_label.place(relx=0.5, rely=0.4, anchor="center")
options2 = ["Polski", "Angielski", "Niemiecki"]
option_menu = customtkinter.CTkOptionMenu(window,values= options2)
option_menu.place(relx=0.5, rely=0.45, anchor="center")

# CTkCheckBox - Check Box
checkbox_label = customtkinter.CTkLabel(window, text="Tryb nocny", font=("Arial", 12))
checkbox_label.place(relx=0.5, rely=0.55, anchor="center")
checkbox = customtkinter.CTkCheckBox(window, text="Włącz tryb nocny")
checkbox.place(relx=0.5, rely=0.6, anchor="center")

# CTkSwitch - Switch
switch_label = customtkinter.CTkLabel(window, text="Automatyczne aktualizacje", font=("Arial", 12))
switch_label.place(relx=0.5, rely=0.7, anchor="center")
switch = customtkinter.CTkSwitch(window)
switch.place(relx=0.5, rely=0.75, anchor="center")

window.mainloop()