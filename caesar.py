
from tkinter import *

def caesar(text, code=3):
    neuer_text = ''
    for buchstabe in text:
        if ('a' <= buchstabe and buchstabe <= 'z'):
            zahl = ord(buchstabe)
            neue_zahl = zahl + code
            if (neue_zahl > ord('z')):
                neue_zahl = neue_zahl - ord('z') + ord('a') - 1

            neuer_text += chr(neue_zahl)
            
        elif ('A' <= buchstabe and buchstabe <= 'Z'):
            zahl = ord(buchstabe)
            neue_zahl = zahl + code
            if (neue_zahl > ord('Z')):
                neue_zahl = neue_zahl - ord('Z') + ord('A') - 1

            neuer_text += chr(neue_zahl)
            
        else:
            neuer_text += buchstabe

    return neuer_text

def verschluesseln():
    code = codeWahl.get()
    text = textFeld.get(1.0,END)
    neuesTextFeld.config(state=NORMAL)
    neuesTextFeld.delete(1.0,END)
    neuesTextFeld.insert(END, caesar(text, code))
    neuesTextFeld.config(state=DISABLED)
    

def entschluesseln():
    code = codeWahl.get()
    text = textFeld.get(1.0,END)
    neuesTextFeld.config(state=NORMAL)
    neuesTextFeld.delete(1.0,END)
    neuesTextFeld.insert(END, caesar(text, 26-code))
    neuesTextFeld.config(state=DISABLED)
    

fenster = Tk()
fenster.title("Caesar Verschlüsselung")
fenster.resizable(width=False, height=False)

ueberschrift = Label(fenster, pady=5,
                     font="Arial, 16", text="Caesar - Verschüsselung")
ueberschrift.pack()
textFrame = LabelFrame(fenster, text="Text", padx=5, pady=5)
textFrame.pack(padx=10, pady=10, fill=BOTH)
textFeld = Text(textFrame, height=6, width=50)
textFeld.pack(fill=BOTH)

einstellungsFrame = Frame(fenster)
einstellungsFrame.pack()
codeWahl = Scale(einstellungsFrame, label="Code:", orient=HORIZONTAL,
                 from_=0, to=26, length=200)
codeWahl.set(3)
codeWahl.pack(side=TOP)
verschluesselnButton = Button(einstellungsFrame, text="Verschlüsseln",
                              command=verschluesseln)
verschluesselnButton.pack(side=LEFT, padx=10, pady=10)
entschluesselnButton = Button(einstellungsFrame, text="Entschlüsseln",
                              command=entschluesseln)
entschluesselnButton.pack(side=LEFT, padx=10, pady=10)

neuerTextFrame = LabelFrame(fenster, text="Ver- bzw. entschlüsselter Text", padx=5, pady=5)
neuerTextFrame.pack(padx=10, pady=10, fill=BOTH)
neuesTextFeld = Text(neuerTextFrame, height=6, width=50, state=DISABLED)
neuesTextFeld.pack(fill=BOTH)

fenster.mainloop()

