from kivy.app import App
from sudoku import sudokuIncompleto
from kivy.core.window import Window
from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.clock import Clock

Window.size = (412,640)
Window.minimum_width = 412
Window.minimum_height = 640

class GerenciarTelas(ScreenManager):
    pass

class TelaMenu(Screen):
    pass

class TelaGame(Screen):
    caixa_selecionada = None
    tabuleiroVerdade = None
    tabuleiroIncompleto = None

    def on_enter(self):
        self.tabuleiroVerdade, self.tabuleiroIncompleto = sudokuIncompleto()
        grid_layout = self.ids.tela_jogo_3
        grid_layout.clear_widgets()

        for linha in range(9):
            for col in range(9):
                valor = self.tabuleiroIncompleto[linha][col]
                text_input = TextInput(
                    text=str(valor) if valor != 0 else "",
                    multiline=False,
                    halign='center',
                    font_size=18,
                    size=(35, 35),
                    input_filter='int',
                    readonly=True,
                    disabled=valor != 0
                )
                text_input.bind(on_touch_down=self.selecionar_caixa)
                text_input.linha = linha
                text_input.col = col
                grid_layout.add_widget(text_input)

    def selecionar_caixa(self, instance, touch):
        if instance.collide_point(*touch.pos):
            self.caixa_selecionada = instance

    def selecionar_numero(self, numero):
        if self.caixa_selecionada is not None:
            self.caixa_selecionada.text = str(numero)

            linha = self.caixa_selecionada.linha
            col = self.caixa_selecionada.col
            self.tabuleiroIncompleto[linha][col] = numero

            self.caixa_selecionada = None 
    
    def apagar_numero(self):
        if self.caixa_selecionada is not None:
            self.caixa_selecionada.text = ""

            linha = self.caixa_selecionada.linha
            col = self.caixa_selecionada.col
            self.tabuleiroIncompleto[linha][col] = 0

            self.caixa_selecionada = None

    def verificacao(self):
        content = BoxLayout(orientation='vertical')
        if self.tabuleiroIncompleto == self.tabuleiroVerdade:
            mensagem = "Parabéns, sudoku completado corretamente!"
        else:
            mensagem = "Sudoku incompleto e/ou incorreto, tente novamente."
        
        content.add_widget(Label(text=mensagem))
        close_button = Button(text='Fechar')
        close_button.bind(on_press=self.fechar_popup)
        content.add_widget(close_button)

        self.popup = Popup(title='Resultado da Verificação',
                           content=content,
                           size_hint=(None, None),
                           size=(400, 200))
        self.popup.open()
    
    def fechar_popup(self, instance):
        self.popup.dismiss()

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