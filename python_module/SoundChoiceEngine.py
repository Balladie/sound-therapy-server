import os
import json
import random

class SoundChoice:
    def __init__(self, modeIdx, weatherMain, timeRange):
        self.modeIdx = modeIdx
        self.weatherMain = weatherMain
        self.timeRange = timeRange

        self.modes = ['adrenaline', 'healing', 'deepsleep', 'focus', 'recovery']

        self.workDir = os.path.dirname(os.path.abspath(__file__))
        with open(self.workDir + '/logs/numMp3.txt') as f:
            self.numSounds = [int(cnt) for cnt in f.readlines()]

        self.linkMode = self.modes[self.modeIdx] + '/'
        self.links = []

    def getBestSound(self, algorithm='representative'):
        if algorithm == 'representative':
            return self.representative()
        elif algorithm == 'kangMapV1':
            return self.kangMapV1()
        else:
            print("[SoundChoice] Error: No such an algorithm there - '" + algorithm + "'")

    def fromIntsToLinks(self, ints):
        for val in ints:
            self.links.append(self.linkMode + 'Track-%02d.mp3' % val)

        return self.links

    def representative(self):
        return [self.linkMode + 'Track-01.mp3', self.linkMode + 'Track-02.mp3']

    # map w/ main weather + time range
    def kangMapV1(self):
        code = json.load(open(self.workDir + "/data/kangMapV1.json"))[self.modes[self.modeIdx]][self.weatherMain][self.timeRange]
        res = []

        #debug
        #print("+"*10, "kangMapV1", "+"*10)
        #print("modeIdx:", self.modeIdx)
        #print("weatherMain:", self.weatherMain)
        #print("timeRange:", self.timeRange)

        substrs = code.split('/')
        for substr in substrs:
            indicesStr = substr.split(',')
            indices = []
            for idxStr in indicesStr:
                indices.append(int(idxStr))
            random.shuffle(indices)
            res.extend(indices)

        return self.fromIntsToLinks(res)
