import tkinter as tk
import VideoClass as VC


global ActivPlayers, ent, Sliddas
ActivPlayers, Sliddas = [], []

def ButtClick():
    Play = VC.Playa(ent.get(), None)
    Play.PlayCon()
    ActivPlayers.append(Play)
    Volum(Play.Instas)

def VolumCommand(widget, play):
    CUM = int(round(widget.get()/2))

    play.audio_set_volume(CUM)

def BigPP(play):
    play.pause()

def Order66(play, Slider, kill, PlayPause):
    ActivPlayers.remove(play)

    Slider.destroy()
    kill.destroy()
    PlayPause.destroy()

    play.stop()

def Volum(play):
    Slider = tk.Scale(root, from_=200, to=0,)
    Slider.set(100)
    Sliddas.append(Slider)
    pos = len(Sliddas) * 2
    Slider.grid(row=4, column=(pos - 1))

    #non-setup
    Slider["command"] = lambda Widget = Slider: VolumCommand(Slider, play)

    PlayPause = tk.Button(root, text="P/P")
    PlayPause["command"] = lambda widget = PlayPause: BigPP(play)
    PlayPause.grid(row=3, column=(pos-1))

    Kill = tk.Button(root, text="X")
    Kill["command"] = lambda widget = Kill: Order66(play, Slider, Kill, PlayPause)
    Kill.grid(row=3, column=pos)


root = tk.Tk()
root.geometry("1000x500")
root.title("Fugly SoundBoard")
ent = tk.Entry(root)
ent.grid(row=0, column=1)
BUTT = tk.Button(root, text="...", command=ButtClick)
BUTT.grid(row=0, column=2)


root.mainloop()
