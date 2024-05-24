import os

script_list = ['from os import system, getlogin\n', 'from random import randint\n', '\n', "urlstring = open('/home/'+getlogin()+'/Видео/видео.txt')\n", 'urllist = [i[:-1] for i in urlstring]\n', 'number = randint(0, len(urllist)-1)\n', 'url = urllist[number]\n', 'tm = str(120 + randint(1, 100))\n', '\n', "system('sleep '+tm+'m; \\\n", '    amixer sset Master on -D pulse; \\\n', '    amixer sset Master 40% -D pulse; \\\n', "    DISPLAY=:0 mpv --fullscreen '+url)\n"]

service_list = ['[Unit]\n', 'Description=autolaunch_mpv\n', '\n', '[Service]\n', 'Type=oneshot\n', 'ExecStart=/usr/bin/python /path-to-python-file/python_file.py\n', '\n', '[Install]\n', 'WantedBy=default.target\n']

os.system('touch /home/' + os.getlogin() + '/Видео/видео.txt')

ppath = '/home/' + os.getlogin()
dirname = '/Документы/.autolaunchmpv'
path = ppath+dirname
serfpath = ppath+'/.config/systemd/user'

try:
    os.mkdir(path)
except:
    print('directory for script already exists')
try:
    os.makedirs(serfpath)
except:
    print('directory for service already exists')

scpath = path+'/autolaunchmpv.py'
script = open(scpath, 'w')
for s in script_list:
    script.writelines(s)
script.close()
os.system('chmod +x ' + scpath)

servicepath = serfpath+'/autolaunchmpv.service'
service = open(servicepath, 'w')
for s in service_list:
    if 'ExecStart' in s:
        s = s.replace('/path-to-python-file/python_file.py', scpath)
    service.writelines(s)
service.close()
os.system('systemctl --user enable autolaunchmpv.service; systemctl --user start autolaunchmpv.service')
exit()


