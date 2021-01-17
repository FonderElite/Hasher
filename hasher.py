import colorama
import os
import time
import uuid
from colorama import Fore, Back, Style
import hashlib, bcrypt
import  sys
wi = Fore.WHITE
print(Fore.CYAN + '''
 █████   █████                   █████                        
░░███   ░░███                   ░░███                         
 ░███    ░███   ██████    █████  ░███████    ██████  ████████ 
 ░███████████  ░░░░░███  ███░░   ░███░░███  ███░░███░░███░░███
 ░███░░░░░███   ███████ ░░█████  ░███ ░███ ░███████  ░███ ░░░ 
 ░███    ░███  ███░░███  ░░░░███ ░███ ░███ ░███░░░   ░███     
 █████   █████░░████████ ██████  ████ █████░░██████  █████    
░░░░░   ░░░░░  ░░░░░░░░ ░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░     

''')
work = os.getcwd()
print("Current Directory:" + work)
time.sleep(2)
print(Fore.MAGENTA  + 'Made By FonderElite || Droid')
print(Fore.MAGENTA + "Visit My Github Page: https://github.com/FonderElite")
help = print(Fore.GREEN + wi + '''
=============================================
+|   Hashing Algorithm using Python        |+
=============================================
+|   M a d e    By    F o n d e r E l i t e|+
+|-----------------------------------------|+
+|        Visit My Websites:               |+
+|     http://singularity.rf.gd            |+
+|     http://droidtech.rf.gd              |+
+|     http://justice.rf.gd                |+
+|         Social Media                    |+
+|Github:  https://github.com/Fonderelite  |+
+|Twitter: https://twitter.com/elitefonder |+
 =======================================================
 Available Hashes:[SHA1,MD5,MD4,SHA224,SHA256,SHA384,SHA512,WHIRLPOOL,DSA-SHA,MDC2]
 =======================================================''')
print(Fore.GREEN + wi + " Available Salts:[SHA256.salt]")
print(Fore.MAGENTA + "Command For Salting > Ex. $user@ubuntu:" + Fore.YELLOW + "Salt")


def skull():
    print(Fore.RED + '''
                      .-"      "-.
                     /            |
                    |              |
                    |,  .-.  .-.  ,|
                    | )(__/  \__)( |
                    |/     /\     \|
          (@_       (_     ^^     _)
     _     ) \_______\__|IIIIII|__/__________________________
    (_)@8@8{}<________|-\IIIIII/-|___________________________>
           )_/        \          /
          (@           `--------` 
    ''')
    def thankyou():
        print(Fore.MAGENTA +'''
 |￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
Dont be a Script Kiddie.
|＿＿＿＿＿＿＿＿＿＿＿____________|
(\__/) ||
(•ㅅ•) ||
/ 　 づ
        ''')

#command = print(Fore.MAGENTA + "[+]Input a command: ")
tohash = input(Fore.RED + wi + "Input a string to hash/salt: ")
hashing = print(wi + "Choose  your preffered hashing type: ")
salting = "Available Salts:[SHA256]"
chosen = input("")
time.sleep(1)
#if command == "python3 hash.py -h":
    #print(help)
    #print("Try again.")
#elif command == "python3 hash.py":
    #print(help)
   # print("Try again.")
#elif command == "python3 hash.py -H":
 # print(hashes)

def sha1():
 time.sleep(2)
for i in range(1):
    setpass = bytes(tohash, 'utf-8')
hash_object = hashlib.sha1(setpass)
guess_pw = hash_object.hexdigest()
print(guess_pw)

def md5():

    time.sleep(2)
    for i in range(1):
        setpass2 = bytes(tohash, 'utf-8')
        hash_object2 = hashlib.md5(setpass2)
        guess_pw2 = hash_object2.hexdigest()
        print(guess_pw2)


def sha256():

    time.sleep(2)
    for i in range(1):
        setpass3 = bytes(tohash, 'utf-8')
        hash_object3 = hashlib.sha256(setpass3)
        guess_pw3 = hash_object3.hexdigest()
        print(guess_pw3)
def sha224():

    time.sleep(2)
    for i in range(1):
        setpass4 = bytes(tohash, 'utf-8')
        hash_object4 = hashlib.sha224(setpass4)
        guess_pw4 = hash_object4.hexdigest()
        print(guess_pw4)

def sha512():
            time.sleep(2)
            for i in range(1):
                setpass5 = bytes(tohash, 'utf-8')
                hash_object5 = hashlib.sha512(setpass5)
                guess_pw5 = hash_object5.hexdigest()
                print(guess_pw5)

def sha384():
    time.sleep(2)
    for i in range(1):
        setpass6 = bytes(tohash,'utf-8')
        hash_object6 = hashlib.sha384(setpass6)
        hash_object6.hexdigest()
        print(hash_object6)



#########################################################################
def saltone():
    for i in range(1):
     salt = uuid.uuid4().hex
     salted1 = hashlib.sha256(salt.encode() + tohash.encode()).hexdigest() + ':' + salt
     print(salted1)

def salting():
 nice = input("Choose your preffered salting method: ")
 if  nice == "SHA256.salt":
    print("")
    print("SHA-256.salt(Salted Hash Below)")
    saltone()
    print(Fore.MAGENTA + '''
   __       _
o-''))_____//   Dont Be a Script Kiddie 
"--__/ * * * )
c_c__/-c____/
    ''')
##########################################################################

 else:
    print("Thank you for using my Tool!")

def md4():
    hash_object7 = hashlib.new('md4')
    hash_object7.update(bytes(tohash,'utf-8'))
    hashed7 = hash_object7.hexdigest()
    print(hashed7)

def whirlpool():
    for i in range(1):
        hash_object8 = hashlib.new('whirlpool')
        hash_object8.update(bytes(tohash, 'utf-8'))
        hashed8 = hash_object8.hexdigest()
        print(hashed8)
def dsasha():
    hash_object9 = hashlib.new('whirlpool')
    hash_object9.update(bytes(tohash, 'utf-8'))
    hashed9 = hash_object9.hexdigest()
    print(hashed9)
def mdc2():
    hash_object10 = hashlib.new('MDC2')
    hash_object10.update(bytes(tohash, 'utf-8'))
    hashed10 = hash_object10.hexdigest()
    print(hashed10)
if chosen == "SHA1":
    print("SHA-1(Hashed Text Below)")
    sha1()
    print(Fore.MAGENTA + '''
     |￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
    Dont be a Script Kiddie.
    |＿＿＿＿＿＿＿＿＿＿＿____________|
    (\__/) ||
    (•ㅅ•) ||
    / 　 づ
            ''')

elif chosen == "MD5":
    print("MD5(Hashed Text Below)")
    md5()
    print(Fore.MAGENTA + '''
     |￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
    Dont be a Script Kiddie.
    |＿＿＿＿＿＿＿＿＿＿＿____________|
    (\__/) ||
    (•ㅅ•) ||
    / 　 づ
            ''')
elif chosen == "SHA256":
    print("SHA-256(Hashed Text Below)")
    sha256()
    print(Fore.MAGENTA + '''
     |￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
    Dont be a Script Kiddie.
    |＿＿＿＿＿＿＿＿＿＿＿____________|
    (\__/) ||
    (•ㅅ•) ||
    / 　 づ
            ''')
elif chosen == "SHA224":
    print("SHA-224(Hashed Text Below)")
    sha224()
    print(Fore.MAGENTA + '''
     |￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
       Dont be a Script Kiddie.
    |＿＿＿＿＿＿＿＿＿＿＿____________|
    (\__/) ||
    (•ㅅ•) ||
    / 　 づ
            ''')
elif chosen == "SHA512":
    print('SHA-512(Hashed Text Below)')
    sha512()
    print(Fore.MAGENTA + '''
      |￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
        Dont be a Script Kiddie.
     |＿＿＿＿＿＿＿＿＿＿＿____________|
     (\__/) ||
     (•ㅅ•) ||
     / 　 づ
             ''')

elif chosen == "SHA384":
    print('SHA-384(Hashed Text Below)')
    sha384()
    print(Fore.MAGENTA + '''
      |￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
        Dont be a Script Kiddie.
     |＿＿＿＿＿＿＿＿＿＿＿____________|
     (\__/) ||
     (•ㅅ•) ||
     / 　 づ
    ''')
elif chosen == "MD4":
    print('MD4(Hashes Text Below)')
    md4()
    print(Fore.MAGENTA + '''
          |￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
            Dont be a Script Kiddie.
         |＿＿＿＿＿＿＿＿＿＿＿____________|
         (\__/) ||
         (•ㅅ•) ||
         / 　 づ
        ''')
elif chosen == "WHIRLPOOL":
    print('WHIRLPOOL(Hashes Text Below)')
    whirlpool()
    print(Fore.MAGENTA + '''
              |￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
                Dont be a Script Kiddie.
             |＿＿＿＿＿＿＿＿＿＿＿____________|
             (\__/) ||
             (•ㅅ•) ||
             / 　 づ
            ''')
elif chosen == "DSASHA":
    print('DSA-SHA(Hashes Text Below)')
    dsasha()
    print(Fore.MAGENTA + '''
                  |￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
                    Dont be a Script Kiddie.
                 |＿＿＿＿＿＿＿＿＿＿＿____________|
                 (\__/) ||
                 (•ㅅ•) ||
                 / 　 づ
                ''')
elif chosen == "MDC2":
    print('MDC2(Hashes Text Below)')
    mdc2()
    print(Fore.MAGENTA + '''
                     |￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
                       Dont be a Script Kiddie.
                    |＿＿＿＿＿＿＿＿＿＿＿____________|
                    (\__/) ||
                    (•ㅅ•) ||
                    / 　 づ
                   ''')
elif salting() == "SHA256.salt":
    print("SHA-256.salt(Hashed Text Below)")
    print(Fore.MAGENTA + '''
   __       _
o-''))_____//   Dont Be a Script Kiddie 
"--__/ * * * )
c_c__/-c____/
   ''')

else:
    print(Fore.RED + '''
╦╗┬─┐┬ ┬  ┌─┐┌─┐┌─┐┬┌┐┌ 
 ║ ├┬┘└┬┘  ├─┤│ ┬├─┤││││ 
 ╩ ┴└─ ┴   ┴ ┴└─┘┴ ┴┴┘└┘o ''')
