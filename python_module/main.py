import sys

if (__name__ == '__main__'):
    mode = sys.argv[1]
    latitude = sys.argv[2]
    longitude = sys.argv[3]

    mode_name = ['adrenaline', 'healing', 'deepsleep', 'focus', 'recovery']
    
    res = mode_name[int(mode)] + '/Track-01.mp3'
    print(res, end='')
