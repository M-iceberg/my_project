class Music():

    def __init__(self,sound):
        '''general function description:initialize the volume and how many music we want to play at the same time
        param list:(int)sound
        return:none'''
        
        self.sound=sound
        self.channel=None
        
    def play_music(self):
        '''general function description:create a method to play the music with the initialzed volume 0.7
        param list:none
        return:none'''
        
        self.channel.set_volume(0.7)

        self.channel.play(self.sound)

    def stop_music(self):
        '''general function description:create a method to stop the music by set the volume to zero
        param list:none
        return:none'''
        
        self.channel.set_volumn(0.0)

        self.channel.play(self.sound)
