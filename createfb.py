import os, sys, re, requests, bs4, time, random, json, string
from bs4 import BeautifulSoup
from faker import Faker
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip install requests > /dev/null')
try:
    import bs4
except ImportError:
    print ('\n [×] Modul Bs4 Not installed!...\n')
    os.system('pip install bs4')
def convert(cok):
    __for = 'datr=' + cok['datr'] + ';' + ('sb=' + cok['sb']) + ';' + ('fr=' + cok['fr']) + ';' + ('c_user=' + cok['c_user']) + ';' + ('xs=' + cok['xs'])
    return __for
def inbox(session):
    time.sleep(1)
    ses = requests.Session()
    __ = str(time.time()).replace('.', '')[:13]
    data = ses.get(f"https://10minutemail.net/address.api.php?sessionid={session}&_={str(__)}").json()
    if len(data["mail_list"]) !=1:
        address = data["mail_list"][0]["subject"]
        session = address.replace('FB-', '').replace('is your Facebook confirmation code', '')
        return session
def KHALID():
    android = f"{random.randint(4, 11)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    firefox = f"{random.randint(50, 100)}.0"
    antm = f"{random.randint(4, 5)}.{random.randint(0, 9)}"
    kios = f"{random.randint(3, 4)}.{random.randint(0, 9)}.{random.randint(0, 99)}"
    hcf = f"{random.randint(3, 4)}.{random.randint(0, 9)}.{random.randint(0, 99)}"
    achot = ''.join(random.choices(string.ascii_uppercase, k=8))
    braaz = random.choice(["Dalvik/2.1.0","Mozilla/5.0"])
    dev = random.choice(["GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820","SM-A12F", "SM-A13F", "SM-A22F", "SM-A22G", "SM-A225F",
    "SM-A227M", "SM-A315F", "SM-A325F", "SM-A325M", "SM-A326U", "SM-A415F",
    "SM-A425F", "SM-A425M", "SM-A426U", "SM-A505GT", "SM-A505N", "SM-A515F",
    "SM-A515U", "SM-A526U1", "SM-A528U1", "SM-A529B", "SM-A535F", "SM-A537F0",
    "SM-A622U", "SM-A705GM", "SM-A715F", "SM-A725M", "SM-A727V", "SM-A730F",
    "SM-A735F", "SM-A825F", "SM-A905F", "SM-A908B", "SM-A920F", "SM-A925F",
    "SM-A926U", "SM-A102U1", "SM-A105FN", "SM-A105G", "SM-A105M", "SM-A107M",
    "SM-A202K", "SM-A205G", "SM-A205U1", "SM-A2070", "SM-A217M", "SM-A220F",
    "SM-A227F", "SM-A305G", "SM-A307FN", "SM-A307G", "SM-A307GN", "SM-A307GT",
    "SM-A310N0", "SM-A315G", "SM-A317M", "SM-A320Y", "SM-A325N", "SM-A405FM",
    "SM-A405FN", "SM-A405GN", "SM-A405S", "SM-A415U", "SM-A505F", "SM-A507FN",
    "SM-A510F", "SM-A510K", "SM-A510L", "SM-A510M", "SM-A515U1", "SM-A520F",
    "SM-A520K", "SM-A520L", "SM-A520S", "SM-A530F", "SM-A530W", "SM-A535U", "SM-A600F",
    "SM-A600FN", "SM-A600G", "SM-A600GN", "SM-A600N", "SM-A605F", "SM-A605FN",
    "SM-A605G", "SM-A605GN", "SM-A606Y", "SM-A705MN", "SM-A705U", "SM-A705W",
    "SM-A707F", "SM-A707FN", "SM-A710F", "SM-A710K", "SM-A710L", "SM-A710M",
    "SM-A710S", "SM-A715U", "SM-A715W", "SM-A7160"])

 
    user_agent = random.choice([f"{braaz} (Linux; Android {android}; {dev} ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.{firefox}.7{antm} Mobile Safari/537.36{hcf}",f"{braaz} (Android {android}; Mobile; {dev}; rv:{firefox}) Gecko/{firefox} Firefox/{firefox} {achot}/{kios}"])
    
    return user_agent
    
logo4 = """
\x1b[1;91m
\x1b[1;92m
\x1b[1;96m
\x1b[1;92m         {|} {|}  {|} {|}{|}{|} {|}{|}{|}
\x1b[1;97m         {|} {|}  {|}    {|}       {|}
\x1b[1;93m         {|} {|}  {|}    {|}       {|}
\x1b[1;96m         {|} {|}  {|}    {|}       {|}
\x1b[1;94m     {|}{|}   {|}{|}     {|}       {|}
\x1b[1;93m
\x1b[1;92m         Jutt Badshah Brand~
\x1b[1;91m-----------------------------------------------
\x1b[1;97m> Author : Jutt Badshah
\x1b[1;97m> updated by : ABU-KHALID
\x1b[1;97m> Github : https://github.com/SHOOTER-MAKER
\x1b[1;97m> Facebok: Jutt Badshah
\x1b[1;97m> Version: auto create facebook
\x1b[0;97m-----------------------------------------------"""
def bn1(limitism):
    faker = Faker()
    bn = [faker.name_male() for _ in range(limitism)]
    return bn

def gn1(limitism):
    faker = Faker()
    gn = [faker.name_female() for _ in range(limitism)]
    return gn
limitism = 1000
b1 = bn1(limitism)
b2 = gn1(limitism)
boy = random.choice(b1)
girl = random.choice(b2)
ok = []
cp = []
def menu():
    os.system('clear')
    print (logo4)
    print ('            Auto create tool')
    print (47*'-')
    print ('[1]auto creat')
    print ('[2]join Facebok group')
    print ('[3] join whatsapp group')
    print (47*'-')
    sel = input('Select: ')
    if sel in['1', '01']:
        create().start()
    elif sel in ['2', '02']:
        os.system('xdg-open https://www.facebook.com/groups/262660289344669/?ref=share_group_link')
        menu()
    elif sel in ['3', '03']:
        os.system('xdg-open https://chat.whatsapp.com/C4EokyLxEaZGBlyJ99M3pA')
        menu()
    else:
        print ('select valid option')
        time.sleep(3)
        menu()
class create:

    def __init__(self):
        self.loop = 0
        self.gender = []

    def start(self):
        os.system('clear')
        print (logo4)
        print ('[1] Boys name ids')
        print ('[2] girls name ids')
        print (47*'-')
        gen = input('select: ')
        print (47*'-')
        if gen in ['1', '01']:
            self.gender.append('boy')
        elif gen in ['2', '02']:
            self.gender.append('girl')
        else:
            self.gender.append('boy')
        print ('Example 1000, 2000, 5000, 10000')
        lim = int(input('limit: '))
        os.system('clear')
        print (logo4)
        agent = KHALID()
        headers = {
            'authority': 'free.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': agent,
            'viewport-width': '980',
        }
        headers1 = {
            'authority': 'free.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
            'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': agent,
        }
        OO = '\033[0;97m'
        for x in range(lim):
            self.loop += 1
            sys.stdout.write(f'\r {OO}[Creat-fb] {OO}{self.loop}/{str(lim)} OK:{len(ok)} - CP:{len(cp)}{OO} '),
            sys.stdout.flush()
            if 'boy' in self.gender:
                name = boy.split(' ')
                sex = '2'
            elif 'girl' in self.gender:
                name = girl.split(' ')
                sex = '1'
            try:
                ses = requests.Session()
                buildses = user = "".join(random.SystemRandom().choice("qwertyuiopasdfghjklzxcvbnm0987654321") for i in range(26))
                create = ses.get(f"https://10minutemail.net/address.api.php?new=1&sessionid={buildses}&_={int(datetime.now().timestamp() * 1000)}").json()
                mail = {"mail": create["permalink"]["mail"], "session": create["session_id"]}
                email = mail['mail']
                session = mail['session']
            except KeyError:
                pass
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
            passw = name[0]+name[1]+str(random.randint(111,999))
            try:
                self.ses = requests.Session()
                a = self.ses.get('https://free.facebook.com/reg?_fb_noscript', headers=headers)
                loger = re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1)
                ref = BeautifulSoup(a.text, 'html.parser').find('form', {'action': True, "id":"mobile-reg-form", "method":"post"})
                bl = ['lsd', 'jazoest', 'cpp', 'reg_instance', 'submission_request']
                bz = ['reg_impression_id', 'ns']
                self.data = {}
                for v in ref('input'):
                    if v.get('name') in bl:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({'helper': ''})
                for v in ref('input'):
                    if v.get('name') in bz:
                        try:
                            self.data.update({v.get('name'):v.get('value')})
                        except:
                            pass
                self.data.update({
                    "zero_header_af_client": "",
                    "app_id": "103",
                    "logger_id": re.search('name="logger_id" value="(.*?)"', str(a.text)).group(1),
                    "field_names[0]": "firstname",
                    "firstname": name[0],
                    "lastname": name[1],
                    "field_names[1]": "birthday_wrapper",
                    "birthday_day": str(random.randint(1,28)),
                    "birthday_month": str(random.randint(1,12)),
                    "birthday_year": str(random.randint(1992,2004)),
                    "age_step_input": "",
                    "did_use_age": "",
                    "field_names[2]": "reg_email__",
                    "reg_email__": email,
                    "field_names[3]": "sex",
                    "sex": sex,
                    "preferred_pronoun": "",
                    "custom_gender": "",
                    "field_names[]": "reg_passwd__",
                    "reg_passwd__": passw,
                    "submit": "Sign Up",
                    "name_suggest_elig": "false",
                    "was_shown_name_suggestions": "false",
                    "did_use_suggested_name": "false",
                    "use_custom_gender": "",
                    "guid": "",
                    "pre_form_step": "",
                })
                gett = self.ses.post('https://free.facebook.com'+ref['action'], headers=headers1, data=self.data)
                getts = self.ses.get('https://mbasic.facebook.com/login/save-device/?login_source=account_creation&logger_id='+loger+'&app_id=103', headers=headers1)
                data1 = {}
                data2 = {}
                data3 = {}
                cok = self.ses.cookies.get_dict()
                if 'checkpoint' in getts.url:
                    cp.append(email+passw)
                    print ('\r\033[1;33m[CP] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                dbl = ['fb_dtsg', 'jazoest', 'flow', 'next', 'nux_source']
                for x in BeautifulSoup(getts.text, 'html.parser').find_all('form', {'method': 'post'}):
                    if '/login/device-based/update-nonce/' in str(x):
                        for v in x('input'):
                            if v.get('name') in dbl:
                                try:
                                    data1.update({v.get('name'):v.get('value')})
                                except:
                                    pass
                        data1.update({'submit': 'OK'})
                        po = self.ses.post('https://free.facebook.com'+x.get('action'), headers=headers1, data=data1)
                        for x in BeautifulSoup(po.text, 'html.parser').find_all('form', {'method': 'post'}):
                            if 'confirmation_event_location=cliff' in str(x):
                                for v in x('input'):
                                    if v.get('name') in dbl:
                                        try:
                                            data2.update({v.get('name'):v.get('value')})
                                        except:
                                            pass
                                code = inbox(session)
                                data2.update({'c': code, 'submit': 'Confirm'})
                                rex = self.ses.post('https://free.facebook.com'+x.get('action'), headers=headers1, data=data2)
                                if 'checkpoint' in rex.url:
                                    cok = self.ses.cookies.get_dict()
                                    cp.append(email+passw)
                                    print ('\r\033[1;33m[CP] '+cok['c_user']+' | '+passw+'\033[0;97m     ')
                                else:
                                    coki = (";").join([ "%s=%s" % (key, value) for key, value in self.ses.cookies.get_dict().items() ])
                                    cok = self.ses.cookies.get_dict()
                                    print ('\r\033[1;32m[OK] '+cok['c_user']+' | '+passw+' ')
                                    ok.append(email+passw)
            except requests.exceptions.ConnectionError:
                time.sleep(1)
                pass
            except Exception as e:
                pass
        print ('process has been completed')
        print (47*'-')
        print ('\033[1;32mTotal ids > Ok/' +str(len(ok)) + ' CP/' + str(len(cp)))
        print (47*'-')
        input('back')
        menu()
menu()
