from os import system, getlogin
from random import randint

urlstring = open('/home/'+getlogin()+'/Видео/видео.txt')
urllist = [i[:-1] for i in urlstring]
number = randint(0, len(urllist)-1)
url = urllist[number]
tm = str(120 + randint(1, 100))

system('sleep '+tm+'m; \
    amixer sset Master on -D pulse; \
    amixer sset Master 40% -D pulse; \
    DISPLAY=:0 mpv --fullscreen '+url)

