class SoundChoice:
    def __init__(self, modeIdx, weatherMain, timeRange):
        self.modeIdx = modeIdx
        self.weatherMain = weatherMain
        self.timeRange = timeRange

        self.modes = ['adrenaline', 'healing', 'deepsleep', 'focus', 'recovery']

        workDir = os.path.dirname(os.path.abspath(__file__))
        with open(workDir + '/logs/numMp3.txt') as f:
            self.numSounds = [int(cnt) for cnt in f.readlines()]

        self.link = self.modes[self.modeIdx] + '/'

    def getBestSound(self, algorithm='representative'):
        if algorithm == 'representative':
            return self.representative()
        else:
            print("[SoundChoice] Error: No such an algorithm there - '" + algorithm + "'")

    def representative(self):
        return self.link + 'Track-01.mp3'
