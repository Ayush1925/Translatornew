from tkinter import *
from translate import Translator


screen = Tk()
screen.title("Language Translator")
screen.geometry("400x400")

InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()

LanguageChoices = {
"Bengali","Bhojpuri","Chinese (Simplified)",
"Chinese (Traditional)","Dutch","English","German","Gujarati","Hindi",
"Italian","Japanese","Malayalam","Tamil","Tatar","Telugu","Thai","Tigrinya","Tsonga","Turkish","Turkmen","Twi",
"Ukrainian","Urdu","Uyghur","Uzbek","Vietnamese","Welsh","Xhosa","Yiddish","Yoruba","Zulu"
}

InputLanguageChoice.set('English')
TranslateLanguageChoice.set('Hindi')

def Translate():
    translator = Translator(from_lang = InputLanguageChoice.get(),to_lang = TranslateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)

InputLanguageChoiceMenu = OptionMenu(screen,InputLanguageChoice,*LanguageChoices)
Label(screen,text="Translate From").grid(row=0,column=1)
InputLanguageChoiceMenu.grid(row=1,column=1)

NewLanguageChoiceMenu = OptionMenu(screen,TranslateLanguageChoice,*LanguageChoices)
Label(screen,text="Translate To").place(x=50,y=150)
NewLanguageChoiceMenu.place(x=65,y=170)

Label(screen,text="Enter Text").grid(row=2,column=0)
TextVar = StringVar()
TextBox = Entry(screen,textvariable=TextVar).place(x=60,y=55,width=300,height=80)


Label(screen,text="Output").place(x=1,y=210)
OutputVar = StringVar()
TextBox = Entry(screen,textvariable=OutputVar).place(x=60,y=210,width=300,height=80)

B = Button(screen,text="Translate",command=Translate,relief=GROOVE).place(x=200,y=160)

mainloop()