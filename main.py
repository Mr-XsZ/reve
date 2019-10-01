# cd /data/data/com.termux/files/usr/bin/.session
import re, os, bs4, sys, time, json, random, requests, interpreter, subprocess

def login():
    req = requests.Session()
    e = raw_input('[!] No Account Detected\n[*] Login Your Fb\n[?] Username: ')
    p = raw_input('[?] Password: ')
    print '[*] Login ...'
    s = req.post('https://mbasic.facebook.com/login', data={'email': e, 'pass': p}).url
    if 'save-device' in s or 'm_sess' in s:
        i = json.dumps({'email': e, 'pass': p, 
           'name': bs4.BeautifulSoup(req.get('https://mbasic.facebook.com/me').text, features='html.parser').find('title').text})
        open('config/config.json', 'w').write(i)
        print '[*] Login Success..'
        time.sleep(2)
        os.system('clear')
        os.system('python2 asu.py')
    if 'checkpoint' in s or 'challange' in s:
        print '[!] Akun Mu Terkunci! (Kena Sesi) Checkpoint\n[!] Silahkan login manual dan izinkan masuk via browser'
        raw_input('[*] Press enter to again...')
        os.system('clear')
        login()
    else:
        print '[!] Login Failed.'
        raw_input('[*] Press enter to again...')
        os.system('clear')
        login()


class regis(object):

    def __init__(self):
        self.kent = 'https://sereware56.000webhostapp.com'
        self.checkSession()

    def akin(self):
        if os.path.exists('config'):
            if os.path.exists('config/config.json'):
                if os.path.exists('config/config.json') != 0:
                    interpreter.ASU()
                else:
                    login()
            else:
                login()
        else:
            os.mkdir('config')
            login()

    def checkSession(self):
        self.dt = '/data/data/com.termux/files/usr/bin/.session'
        if os.path.exists(self.dt):
            if os.path.exists('%s/asu.txt' % self.dt):
                if os.path.getsize('%s/asu.txt' % self.dt) != 0:
                    id = open('%s/asu.txt' % self.dt).read().replace('\n', '')
                    self.id = json.loads(id)
                    z = requests.get('%s/%s' % (self.kent,
                     'registered.txt')).text
                    if len(re.findall(self.id['sessionID'], z)) != 0:
                        self.akin()
                    else:
                        z = requests.get('%s/%s' % (self.kent,
                         'ip.txt')).text
                        if len(re.findall(self.id['sessionID'], z)) != 0:
                            print '[!] username anda sudah diregistrasi'
                            print '[!] silahkan meminta konfirmasi Angga'
                            print '[!] Username Anda: %s' % self.id['username']
                            raw_input('[!] tekan enter untuk menghubungi Angga via WhatsApp...')
                            subprocess.check_output([
                             'am', 'start',
                             'https://api.whatsapp.com/send?phone=6282211661007&text=konfirm%20saya%20dengan%20username:%20' + self.id['username'].replace(' ', '%20') + ''])
                        else:
                            self.generateSession()
                else:
                    self.generateSession()
            else:
                self.generateSession()
        else:
            os.mkdir(self.dt)
            self.generateSession()

    def generateSession(self):
        self.ab = list('abcdefghijklmnopqrstuvwxyz1234567890')
        self.gen = [
         random.choice(self.ab),
         random.choice(self.ab).upper(),
         random.choice(self.ab),
         random.choice(self.ab).upper(),
         random.choice(self.ab),
         random.choice(self.ab).upper(),
         random.choice(self.ab),
         random.choice(self.ab).upper(),
         random.choice(self.ab),
         random.choice(self.ab).upper(),
         random.choice(self.ab),
         random.choice(self.ab).upper(),
         random.choice(self.ab),
         random.choice(self.ab).upper(),
         random.choice(self.ab),
         random.choice(self.ab).upper()]
        self.ok = ('').join(self.gen)
        self.p = requests.get('%s/%s' % (self.kent, 'ip.txt')).text
        if len(re.findall(self.ok, self.p)) != 0:
            print '[!] ID Exists: %s' % self.ok
            self.generateSession()
        else:
            self.username()

    def username(self):
        print '[!] ASU USERS ID: %s' % self.ok
        print '[*] Create Username'
        self.cre()

    def cre(self):
        self.user = raw_input('[?] Username: ')
        if self.user == '':
            self.cre()
        else:
            print requests.post('%s/new.php' % self.kent, data={'ip': self.ok, 'nama': '%s ----> V5' % self.user}).text
            f = json.dumps({'sessionID': self.ok, 'username': self.user})
            open('%s/asu.txt' % self.dt, 'w').write(f)
            print '[*] silahkan meminta konfirmasi kepada Angga'
            raw_input('[!] Tekan Enter Untuk Menghubungi Angga via WhatsApp...')
            subprocess.check_output([
             'am', 'start',
             'https://api.whatsapp.com/send?phone=6282211661007&text=konfirm%20saya%20dengan%20username:%20' + self.user.replace(' ', '%20') + ''])