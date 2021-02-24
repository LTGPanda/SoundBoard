import VideoClass as VC
from kivy.app import App
#https://github.com/inclement/kivycrashcourse
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.clock import Clock
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '500')

from kivy.uix.boxlayout import BoxLayout
global ActivPlayers, ent, Sliddas #hwo bo dees
ActivPlayers, Sliddas = [], [] #do i do the need?

class SoundControl(BoxLayout):
    The_Slider = ObjectProperty()
    def __init__(self, play, root, **kwargs):
        self.Play = play
        self.root = root
        super(SoundControl, self).__init__(**kwargs)

    def VolComand(self):
            CUM = int(round(self.ids['The_Slider'].value/2))
            self.Play.VolSet(CUM)

            label = self.ids['Slider_val']
            slidy = self.ids['The_Slider']
            label.text = str(int(slidy.value))

    def BigPP(self):
        self.Play.PauseSound()

    def Order66(self):
        ActivPlayers.remove(self.Play)
        self.Play.StopSound()
        self.parent.remove_widget(self)

class MainSetup(BoxLayout):
    def get_slider_val(self, *args):
        label = self.ids['Slider_val']
        slidy = self.ids['Da_Slider']

        label.text = str(int(slidy.value))

    def Add_Sound_Control(self, *args):
        MainApp = self.ids['Scroller']
        
        Play = VC.Playa(str(self.ids['Link_input'].text), None)
        Play.PlayCon()
        Added_Lad = SoundControl(Play, self)
        MainApp.add_widget(Added_Lad)
        Sliddas.append(Added_Lad)
        ActivPlayers.append(Play)
        LastPlayer = Play
        LastControll = Added_Lad

        #Added_Lad.ids['Da_Slider'].on_touch_move(Added_Lad.VolComand(Added_Lad, Play.Instas))
        #Event_Binder(Added_Lad, Play)
        #Exception has occurred: AttributeError
        #'NoneType' object has no attribute 'grab_current'
        #Added_Lad.ids['Death'].on_press(Added_Lad.Order66(Play))
        #Added_Lad.ids['PP'].on_press(Added_Lad.BigPP(Play, Sliddas))

 
class SoundBoardApp(App):
    def build(self):
        return MainSetup()


if __name__ == '__main__':
    SoundBoardApp().run()