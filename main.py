import VideoClass as VC
import json
import os.path
from kivy.app import App
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
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

    def SaveLad(self):
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

class LoadedItem(BoxLayout):
    #def __init__(self, *args):
    #    pass

    def LoadLink(self, *args):
        #self.manager.
        #OtherScreen = App.root_window.get_screen('Soundboard')
        #self.parent.ms.current = 'Soundboard'
        #self.root.manager.current = 'Soundboard'
        #self.manager.current.Add_Sound_Control(self.data['Link'])
        self.manager.get_screen('Soundboard').Add_Sound_Control(self.url)
        #no rows or cols set fuk

class Loader(Screen):
    def __init__(self, **kwargs):
        super(Loader, self).__init__(**kwargs)
        self.LoadSettup()
        print(self.data)

    def Createjson(self):
        with open('LinkDB.json', 'w+') as f:
            saveData = {
                'SavedLink': []
            }
            json.dump(saveData, f)
            f.close()

    def FileLoad(self):
        if os.path.isfile('LinkDB.json') == False:
            self.Createjson()
        with open('LinkDB.json', 'r') as f:
            data = json.load(f)
            self.data = data['SavedLink']
            f.close()

    def LoadSettup(self):
        self.FileLoad()
        for item in self.data:
            #MainGrid = GridLayout()
            #MainGrid.add_widget(Label(text=item['Name']))
#
            #BUTT = Button(text='Load')
            #BUTT.size_hint_x = None
            #BUTT.width = 100
            #url = item['Link']
            #BUTT.bind(on_press=self.LoadLink(url))
#
            #MainGrid.add_widget(BUTT)
            newItem = LoadedItem()
            newItem.url = item['Link']
            newItem.namn = item['Name']
            self.ids['Scrolly'].add_widget(newItem)


class MainSetup(Screen):
    def get_slider_val(self, *args):
        label = self.ids['Slider_val']
        slidy = self.ids['Da_Slider']

        label.text = str(int(slidy.value))

    def Add_Sound_Control(self, url):
        MainApp = self.ids['Scroller']
        
        Play = VC.Playa(str(url), None)
        Play.PlayCon()
        MainApp.add_widget(SoundControl(Play, self))

        ActivPlayers.append(Play)

class SoundBoardApp(App):
    def build(self):#taken straight from the kivy docs
        sm = ScreenManager()
        sm.add_widget(MainSetup(name='Soundboard'))
        sm.add_widget(Loader(name='SoundLoader'))
        return sm


if __name__ == '__main__':
    SoundBoardApp().run()