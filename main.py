import VideoClass as VC
import json
import os.path
from kivy.app import App
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '500')

from kivy.uix.boxlayout import BoxLayout
global ActivPlayers, ent, Sliddas #hwo bo dees
ActivPlayers, Sliddas = [], [] #do i do the need?

class SoundControl(BoxLayout):
    The_Slider = ObjectProperty()#clean upp?
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

    def Createjson(self):
        with open('LinkDB.json', 'w+') as f:
            saveData = {
                'SavedLink': []
            }
            json.dump(saveData, f)
            f.close()

    def SaveLad(self):
        if os.path.isfile('LinkDB.json') == False:
            self.Createjson()

        Save_Data = {
            'Name': str(self.ids['SoundName'].text),
            'Link' : str(self.Play.GetUrl())
        }
        with open('LinkDB.json', 'r') as f:
            data = json.load(f)
            temp = data['SavedLink']
            temp.append(Save_Data)
            f.close()

        with open('LinkDB.json', 'w') as f:
            json.dump(data, f, indent=4)

class Loader(App):
    def LoadLinks():
        print("cunt")

class MainSetup(BoxLayout):
    def get_slider_val(self, *args):
        label = self.ids['Slider_val']
        slidy = self.ids['Da_Slider']

        label.text = str(int(slidy.value))

    def Add_Sound_Control(self, *args):
        MainApp = self.ids['Scroller']
        
        Play = VC.Playa(str(self.ids['Link_input'].text), None)
        Play.PlayCon()
        MainApp.add_widget(SoundControl(Play, self))

        ActivPlayers.append(Play)

    def LoadLoader(self):
        Loader()

class SoundBoardApp(App):
    def build(self):
        return MainSetup()


if __name__ == '__main__':
    SoundBoardApp().run()