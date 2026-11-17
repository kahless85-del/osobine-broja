from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

import osnovno
import specijalni
import zapis

# Opcionalno za testiranje na računalu
Window.size = (400, 600)

class GlavniEkran(BoxLayout):
    def __init__(self, **kwargs):
        super(GlavniEkran, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15

        # Dinamička veličina fonta ovisno o visini prozora
        # Možeš prilagoditi faktor (npr. prozor.height * 0.025)
        self.bind(size=self.update_fonts)

        # Uputa
        self.lbl_uputa = Label(
            text="Unesite prirodan broj:", 
            font_size=20, 
            size_hint_y=None, 
            height=40,
            halign='center',
            valign='middle'
        )
        self.lbl_uputa.bind(size=self.lbl_uputa.setter('text_size'))
        self.add_widget(self.lbl_uputa)
        
        # Polje za unos s centriranim tekstom
        self.entry_broj = TextInput(
            text='', 
            multiline=False, 
            font_size=22, 
            size_hint_y=None, 
            height=50,
            input_filter='int',
            halign='center'  # Centriran tekst unutar unosa
        )
        self.entry_broj.bind(on_text_validate=self.provjeri_broj)
        self.add_widget(self.entry_broj)

        # Gumb
        self.btn_provjeri = Button(
            text="Prikaži osobine",
            font_size=18,
            bold=True,
            size_hint_y=None,
            height=55,
            background_color=(0.1, 0.5, 0.8, 1)
        )
        self.btn_provjeri.bind(on_press=self.provjeri_broj)
        self.add_widget(self.btn_provjeri)

        # Scrollable polje za ispis rezultata
        self.scroll = ScrollView(size_hint=(1, 1))
        
        self.lbl_rezultat = Label(
            text="Ovdje će se prikazati osobine broja...",
            font_size=16, # Početna veličina, automatski se prilagođava
            halign='left',
            valign='top',
            size_hint_y=None
        )
        self.lbl_rezultat.bind(texture_size=self.update_text_size)
        
        self.scroll.add_widget(self.lbl_rezultat)
        self.add_widget(self.scroll)

    def update_fonts(self, *args):
        # Automatski mijenja veličinu fonta rezultata ovisno o visini ekrana
        # Faktor 0.023 znači da će font pratiti otprilike 2.3% visine zaslona
        novi_font = max(14, int(self.height * 0.023))
        self.lbl_rezultat.font_size = novi_font

    def update_text_size(self, *args):
        self.lbl_rezultat.text_size = (self.scroll.width - 20, None)
        self.lbl_rezultat.height = self.lbl_rezultat.texture_size[1]

    def provjeri_broj(self, instance):
        unos = self.entry_broj.text.strip()
        try:
            n = int(unos)
            if n <= 0:
                self.prikazi_gresku("Unešeni broj nije prirodan (mora biti veći od 0).")
                return
        except ValueError:
            self.prikazi_gresku("Unešeni podatak nije valjan prirodan broj.")
            return

        djelitelji_str = ", ".join(str(d) for d in osnovno.djelitelji(n))
        faktori = osnovno.prostifaktori(n)
        faktori_str = " · ".join(str(f) for f in faktori) if faktori else "Nema (broj 1 nema prostih faktora)"

        rezultati = [
            f"Osobine prirodnog broja {n}:",
            "-" * 35,
            f"Paran: {'Da' if osnovno.paran(n) else 'Ne'}",
            f"Prost: {'Da' if osnovno.prost(n) else 'Ne'}",
            f"Potpun kvadrat: {'Da' if bool(osnovno.kvadrat(n)) else 'Ne'}",
            f"Djelitelji: {djelitelji_str}",
            f"Prosti faktori: {faktori_str}",
            f"Savršen: {'Da' if specijalni.savrsen(n) else 'Ne'}",
            f"Armstrongov: {'Da' if specijalni.armstrongov(n) else 'Ne'}",
            f"Lijep: {'Da' if specijalni.lijep(n) else 'Ne'}",
            f"Palindrom: {'Da' if zapis.palindrom(n) else 'Ne'}",
            f"Zbroj znamenki: {zapis.zbroj_znamenki(n)}",
            f"Binarni zapis: {zapis.binarni(n)}"
        ]

        self.lbl_rezultat.text = "\n".join(rezultati)
        self.entry_broj.text = ""

    def prikazi_gresku(self, poruka):
        self.lbl_rezultat.text = f"[GRESKA] {poruka}"
        self.entry_broj.text = ""


class BrojApp(App):
    def build(self):
        self.title = "Osobine prirodnog broja"
        return GlavniEkran()


if __name__ == '__main__':
    BrojApp().run()
