import VideoClass as VC
from kivy.app import App
#https://github.com/inclement/kivycrashcourse
from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '500')

from kivy.uix.boxlayout import BoxLayout

global ActivPlayers, ent, Sliddas
ActivPlayers, Sliddas = [], []

class MainSetup(BoxLayout):
    def get_slider_val(self, *args):
        label = self.ids['Slider_val']
        slidy = self.ids['Da_Slider']

        label.text = str(int(slidy.value))

    def Add_Sound_Control(self, *args):
        Added_Lad = SoundControl()
        MainApp = self.ids['Main_Box']
        MainApp.add_widget(Added_Lad)

class SoundControl(BoxLayout):
    pass
 
class SoundBoardApp(App):
    def build(self):
        return MainSetup()


if __name__ == '__main__':
    SoundBoardApp().run()