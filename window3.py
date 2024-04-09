from tkinter import filedialog, Image
import os
import PIL as pil
from PIL import Image, ImageOps
import customtkinter as ctk
import customtkinter
from PIL import ImageOps
from PIL.ImageDraw import ImageDraw

window = ctk.CTk()
window.title("Profil")
window.geometry("420x740+700+20")

Background_Frame = ctk.CTkFrame(window, width=420, height=740)
Background_Frame.place(relx=0, rely=0, anchor="nw")
def My_Upload():
    # Open file dialog for image selection
    file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File",
                                           filetypes=(
                                           ("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")))

    # Check if a file is selected
    if file_path:
        # Open the selected image
        img = Image.open(file_path)

        # Create a mask for circular cropping
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)

        # Apply the circular mask to the image
        output = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)

        # Save the cropped circular image as "uzytkownik.png"
        output.save("uzytkownik.png")

        # Update the Profile_Button image with the newly uploaded image
        updated_profile_img = customtkinter.CTkImage(dark_image=pil.Image.open("uzytkownik.png"), size=(200, 200))
        Profile_Button.configure(image=updated_profile_img)




Profile_Img = ctk.CTkImage(dark_image=pil.Image.open("uzytkownik.png"), size=(200, 200))
Profile_Button = ctk.CTkButton(Background_Frame, image=Profile_Img, text="", width=200, height=200,
                               command=My_Upload,
                               fg_color="transparent")
Profile_Button.place(relx=0.5, rely=0.25, anchor="center")


window.mainloop()