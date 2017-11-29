class Music():

    def __init__(self,sound):

        self.sound=sound
        self.channel=None
        
    def play_music(self):

        self.channel.set_volume(0.7)

        self.channel.play(self.sound)

    def stop_music(self):

        self.channel.set_volumn(0.0)

        self.channel.play(self.sound)
