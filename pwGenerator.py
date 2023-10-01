import customtkinter as ctk
import random

ch1 = 'a'
ch2 = ''

print(ch1+ch2)

# !@#$ use these characs only dumbo
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")
appWindow = ctk.CTk()
appWindow.geometry("600x600")
appWindow.resizable(False, False)
appWindow.title('Password Generator by Sol Studios(SOLO)')

introLabel = ctk.CTkLabel(appWindow, bg_color= "transparent", text="Password Generator", font=("JetBrains Mono", 24)).place(x=160, y=20)
helpLable = ctk.CTkLabel(appWindow,bg_color= "transparent", text="<Choose from below to strengthen your PASSWORD>", 
                         font=("JetBrains Mono", 16)).place(x=50, y=90)

includeNumbers = ctk.StringVar(value="off")
includeSpecial = ctk.StringVar(value="off")
numberCheckBox = ctk.CTkCheckBox(appWindow, text="Include Numbers(0-9)", font=("JetBrains Mono", 16),variable= includeNumbers,
                                 offvalue="off", onvalue="on").place(x=50,y=170)
specialCheckBox = ctk.CTkCheckBox(appWindow, text="Include Special Characters(#&$%)", font=("JetBrains Mono", 16),variable= includeSpecial,
                                 offvalue="off", onvalue="on").place(x=50,y=210)

beep = ""
pwTextBox = ctk.CTkTextbox(appWindow, font=("JetBrains Mono", 20), height=50)
pwTextBox.place(x=180, y=410)
pwTextBox.insert("0.0",beep)

sliderDescLabel = ctk.CTkLabel(appWindow, text="Password Length:", font=("JetBrains Mono", 16))
sliderDescLabel.place(x=80, y=245)
sliderLabel = ctk.CTkLabel(appWindow, text="8", font=("JetBrains Mono", 16))
sliderLabel.place(x=55, y=280)
sliderValue = ctk.IntVar(value=8)

def sliderLabelChange(self):
    global sliderValue, sliderLabel
    labelChangeVal = str(sliderValue.get())
    sliderLabel.configure(text=labelChangeVal)

limitSlider = ctk.CTkSlider(appWindow, from_=8, to=15, variable=sliderValue, command=sliderLabelChange)
limitSlider.place(x=80, y=285)


def generator():
    global beep, pwTextBox, sliderValue
    pwTextBox.delete("0.0","end")
    password = ""

    while len(password) != sliderValue.get():
        randomizer = random.randint(1,4)
        if(randomizer == 1):
            ranLetter = str(chr(random.randint(ord('a'), ord('z'))))
            password = password+ranLetter
        if(randomizer == 2):
            ranUpperLetter = str(chr(random.randint(ord('A'), ord('Z'))))
            password = password+ranUpperLetter
        if(randomizer == 3):
            if(includeNumbers.get() == "on"):
                ranNums = str(random.randint(0,9))
                password = password+ranNums
        if(randomizer == 4):
            if(includeSpecial.get() == "on"):
                ranSpecials = str(chr(random.randint(ord('#'), ord('&'))))
                password = password+ranSpecials
    pwTextBox.insert("0.0",text=password)

generateButton = ctk.CTkButton(appWindow, command=generator, text="Generate", font=("JetBrains Mono", 16),
                               height=38, width=160).place(x=200, y=480)

appWindow.mainloop()