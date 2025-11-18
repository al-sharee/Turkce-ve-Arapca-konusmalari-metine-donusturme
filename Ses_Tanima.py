import speech_recognition
import arabic_reshaper
from bidi.algorithm import get_display
from tkinter import *
from tkinter import font

#pencernin ayarlari icin 
root = Tk()
root.geometry("600x300")
root.title("Konuşmalarımızı Tanıma")

#arapca konusup yazmak icin 
def voieReco():
    recognizer=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic,duration=0.2)
        audio=recognizer.listen(mic)
        text=recognizer.recognize_google(audio,language="ar-AR ")
        reshaped_text=arabic_reshaper.reshape(text)
        bidi_text=get_display(reshaped_text)
        print(bidi_text)
        textF.delete("1.0","end")
        textF.insert(END,bidi_text)
        textF.tag_add("center",1.0,"end")

#turkce konusup yazmak icin 
def voiceReco_turkish():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)
        text = recognizer.recognize_google(audio, language="tr-TR")
        textF.delete("1.0", "end")
        textF.insert(END, text)
        textF.tag_add("center", 1.0, "end")







#yazinin ayarlari icin paragraf icin ve button icin 
ButtonFont=font.Font(size=20)
LabelFont=font.Font(size=15)
bilgilendirme=font.Font(size=5)

Label(root,text="METININIZ." ,font=LabelFont).pack()


textF=Text(root,height=5 ,width=52 , font=LabelFont)
textF.tag_configure("center",justify='center')
textF.pack()



Button(root,text="ARAPCA",font=ButtonFont,command=voieReco ).place(x=100, y=200)
Button(root,text="TURKCE",font=ButtonFont,command=voiceReco_turkish).place(x=350,y=200)
Label(root,text="KONUSTUKLARINIZI EKRANDA GOZUKMESI ICIN ONCE KONUSCEGINIZ DILIN BUTTONUNA BASMAIZ GEREKYOR" ,font=bilgilendirme).place(x=100,y=150)







root.mainloop()#pencernin surekli acik olmasi icin 




