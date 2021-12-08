class MusicNotes():
    def __init__(self):
        self.freq_diff = 2 ** (1 / 12)
        self.first_la = 55
        self.index = 0

    def round(self, num):
        return round(num * 100) / 100

    def __iter__(self):
        return self

    def __next__(self):
        current_freq = self.round(self.first_la * self.freq_diff ** self.index)
        if current_freq >= self.first_la * 2 ** 5:
            raise StopIteration()

        if self.index % 12 == 2 or self.index % 12 == 7:
            self.index += 1
        else:
            self.index += 2
        return current_freq


notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq)