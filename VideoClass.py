import pafy, vlc

class Playa(object):
    def __init__(self, Url, Instas):
        self.Url = Url
        self.Instas = Instas
    
    def PlayCon(self):
        if self.Url != None:
            video = pafy.new(self.Url)
            best = video.getbestaudio()
            playUrl = best.url
            
            Instance = vlc.Instance('--input-repeat=99999999999')
            player = Instance.media_player_new()
            Media = Instance.media_new(playUrl)

            vlc.VideoDisplayCb()

            Media.get_mrl()
            player.set_media(Media)
            player.play()

            player.audio_set_volume(50)
            self.Instas = player
