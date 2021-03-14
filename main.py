import VideoClass as VC
import json
import os.path
import requests

from kivy.app import App#clean up
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '500')

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
        self.Play.StopSound()
        self.parent.remove_widget(self)

    def SaveLad(self, tags):#TODO parse Tags, fix att save butt inte sparar men startar popup
        Save_Data = {
            'Name': str(self.ids['SoundName'].text),
            'Link' : str(self.Play.GetUrl()),
            'tags' : tags
        }#tags ska vara str?
        with open('LinkDB.json', 'r') as f:
            data = json.load(f)
            temp = data['SavedLink']
            temp.append(Save_Data)
            f.close()

        with open('LinkDB.json', 'w') as f:
            json.dump(data, f, indent=4)



class LoadedItem(BoxLayout):
    def __init__(self, *args, **kwargs):
        self.Name = "STDN"
        self.URL = "STDN-URL"
        super(LoadedItem, self).__init__(**kwargs)

    def Update(self):
        self.ids['DaLabel'].text = self.Name



class Loader(Screen):
    def __init__(self, **kwargs):
        super(Loader, self).__init__(**kwargs)
        self.LoadSettup()
        print(self.data)

    def Createjson(self):
        with open('LinkDB.json', 'w+') as f:
            saveData = {
                'Tags' : ['Forest', 'city', 'Sea', 'Market', 'Boat', 'Tavern', 'Battle', 'Battle-Epic', 'Royal', 'Death', 'Cave', 'Dungeon'],
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
            self.Tags = data['Tags']
            f.close()

    def LoadSettup(self):
        self.FileLoad()
        for item in self.data:
            print(item['Name'])
            newItem = LoadedItem()
            newItem.URL = item['Link']
            newItem.Name = item['Name']
            newItem.Update()
            self.ids['ScrollyLad'].add_widget(newItem)



class MainSetup(Screen):
    def get_slider_val(self, *args):
        label = self.ids['Slider_val']
        slidy = self.ids['Da_Slider']

        label.text = str(int(slidy.value))

    def Add_Sound_Control(self, url):
        match = "https://www.youtube.com/watch"
        i = 0
        if url == "":
            return
        for char in match:
            if char != url[i]:
                return
            i += 1

        try:
            response = requests.get(url)
            MainApp = self.ids['Scroller']
        
            Play = VC.Playa(str(url), None)
            Play.PlayCon()
            MainApp.add_widget(SoundControl(Play, self))


        except requests.ConnectionError as exception:
            return

        

class SoundBoardApp(App):
    def build(self):#taken straight from the kivy docs
        sm = ScreenManager()
        sm.add_widget(MainSetup(name='Soundboard'))
        sm.add_widget(Loader(name='SoundLoader'))
        return sm


if __name__ == '__main__':
    SoundBoardApp().run()