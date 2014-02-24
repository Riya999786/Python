import time

class Song(object):

    def __init__(self, lyrics):
      self.lyrics = lyrics

    def sing_me_a_song(self):
      for line in self.lyrics:
        print line

    def sing_song_slowly(self, speed):
      line = ' '.join(self.lyrics)
      words = line.split()
      for word in words:
        print word
        time.sleep(speed)


happy_bday = Song(["Happy birthday to you",
                  "I don't want to get sued",
                  "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

happy_bday.sing_song_slowly(.5)

bulls_on_parade.sing_song_slowly(.5)