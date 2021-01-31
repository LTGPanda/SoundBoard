import VideoClass as VC
from kivy.app import App
#https://github.com/inclement/kivycrashcourse
from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '500')

from kivy.uix.boxlayout import BoxLayout
global LastPlayer, LastControll
global ActivPlayers, ent, Sliddas
ActivPlayers, Sliddas = [], []

class SoundControl(BoxLayout):
    def __init__(self, play, **kwargs):
        self.Play = play
        self.ids['Da_Slider'].on_touch_move(self.VolComand(self, self.Play.Instas))
        self.ids['Death'].on_press(self.Order66(self.Play))
        self.ids['PP'].on_press(self.BigPP(self.Play, Sliddas))
        super(play, self).__init__(**kwargs)

    def VolComand(self, Slider, play):
            CUM = int(round(Slider.ids['Da_Slider'].value/2))

            play.audio_set_volume(CUM)

            label = self.ids['Slider_val']
            slidy = self.ids['Da_Slider']
            label.text = str(int(slidy.value))

    def BigPP(play):
        play.pause()

    def Order66(play, Slider):
        ActivPlayers.remove(play)

        Slider.destroy()
        kill.destroy()
        PlayPause.destroy()

        play.stop()

class MainSetup(BoxLayout):
    def get_slider_val(self, *args):
        label = self.ids['Slider_val']
        slidy = self.ids['Da_Slider']

        label.text = str(int(slidy.value))

    def Add_Sound_Control(self, *args):
        MainApp = self.ids['Scroller']
        

        Play = VC.Playa(str(self.ids['Link_input'].text), None)
        Play.PlayCon()
        Added_Lad = SoundControl(Play)
        MainApp.add_widget(Added_Lad)
        Sliddas.append(Added_Lad)
        ActivPlayers.append(Play)
        #Event_Binder(self, Added_Lad, Play)
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