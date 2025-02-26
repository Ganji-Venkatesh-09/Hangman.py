
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import random

class HangmanApp(App):
    def build(self):
        self.words = ["PYTHON", "KIVY", "MOBILE", "DEVELOPER", "ANDROID"]
        self.word = random.choice(self.words)
        self.guessed = ["_" for _ in self.word]
        self.attempts = 6

        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.word_label = Label(text=" ".join(self.guessed), font_size=32)
        self.layout.add_widget(self.word_label)
        
        self.status_label = Label(text=f"Attempts left: {self.attempts}", font_size=24)
        self.layout.add_widget(self.status_label)
        
        self.buttons_layout = BoxLayout()
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            btn = Button(text=letter, font_size=20, size_hint=(None, None), size=(50, 50))
            btn.bind(on_press=self.guess)
            self.buttons_layout.add_widget(btn)
        
        self.layout.add_widget(self.buttons_layout)
        return self.layout

    def guess(self, instance):
        letter = instance.text
        instance.disabled = True
        
        if letter in self.word:
            for i, l in enumerate(self.word):
                if l == letter:
                    self.guessed[i] = letter
            self.word_label.text = " ".join(self.guessed)
        else:
            self.attempts -= 1
            self.status_label.text = f"Attempts left: {self.attempts}"
        
        if "_" not in self.guessed:
            self.status_label.text = "You Win! 🎉"
            self.disable_buttons()
        elif self.attempts == 0:
            self.status_label.text = f"Game Over! Word was {self.word}"
            self.disable_buttons()
    
    def disable_buttons(self):
        for btn in self.buttons_layout.children:
            btn.disabled = True

if __name__ == "__main__":
    HangmanApp().run()
