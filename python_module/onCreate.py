import os

def countMp3Files(assetsDir):
    modes = ['adrenaline', 'healing', 'deepsleep', 'focus', 'recovery']
    counts = [0] * len(modes)

    for path, dirnames, filenames in os.walk(assetsDir):
       for filename in filenames:
           if '.mp3' not in filename: continue

           for i, mode in enumerate(modes):
               if mode in path:
                   counts[i] += 1

    return counts

if (__name__ == '__main__'):
    workDir = os.path.dirname(os.path.abspath(__file__))
    assetsDir = workDir + '/../nodejs/sounds'
    counts = countMp3Files(assetsDir)

    with open(workDir + '/logs/numMp3.txt', 'w+') as f:
        for i, count in enumerate(counts):
            if i == len(counts):
                f.write(str(count))
            else:
                f.write(str(count) + '\n')
    print("Count result:", counts)

    print("Finished onCreate.py")
