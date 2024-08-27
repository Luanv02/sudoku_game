from kivy.app import App
from sudoku import sudoku, sudokuIncompleto
from kivy.config import Config
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class GerenciarTelas(ScreenManager):
    pass

class TelaMenu(Screen):
    pass

class TelaGame(Screen):
    numero_selecionado = None
    text_input_selecionado = None

    def on_enter(self):
        tabuleiroIncompleto = sudokuIncompleto()
        grid_layout = self.ids.tela_jogo_3
        grid_layout.clear_widgets()

        for linha in range(9):
            for col in range(9):
                valor = tabuleiroIncompleto[linha][col]
                text_input = TextInput(
                    text=str(valor) if valor != 0 else "",
                    multiline=False,
                    halign='center',
                    font_size=18,
                    size=(35, 35),
                    input_filter='int',
                    readonly=True
                )
                text_input.bind(on_touch_down=self.selecionar_text_input)
                grid_layout.add_widget(text_input)
    
    def selecionar_text_input(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.text_input_selecionado = instance

    def selecionar_numero(self, numero):
        self.numero_selecionado = numero
        if self.text_input_selecionado is not None:
            self.text_input_selecionado.text = str(numero)
            self.text_input_selecionado = None
    
    def apagar_numero(self):
        if self.text_input_selecionado is not None:
            self.text_input_selecionado.text = ""
            self.text_input_selecionado = None 

class TelaGameOver(Screen):
    pass

class TelaScore(Screen):
    pass

GUI = Builder.load_file('gameView.kv')

class Sudoku(App):
    def build(self):
        return GUI

if __name__ == '__main__': 
    Sudoku().run()
