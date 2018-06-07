class Song(object) :
    def __init__(self, lyrics) :
        # think of self as "this" from C++
        self.lyrics = lyrics
        print(f"\nNew Song Created!")
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

happy_bday.sing_me_a_song()

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

bulls_on_parade.sing_me_a_song()

my_song = ["This is my song",
            "It is not very long",
            "Now I am done"]

my_song_along = Song(my_song)

my_song_along.sing_me_a_song()