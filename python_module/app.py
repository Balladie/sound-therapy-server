import sys

if (__name__ == '__main__'):
    mode = sys.argv[1]
    latitude = sys.argv[2]
    longitude = sys.argv[3]

    res = mode + "_" + latitude + "_" + longitude + ".mp3"
    print(res, end='')
