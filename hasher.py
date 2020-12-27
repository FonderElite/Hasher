import colorama
import os
import time
from colorama import Fore, Back, Style
import hashlib, bcrypt

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
time.sleep(2)
print(Fore.YELLOW + 'Made By FonderElite || Droid')
print("Visit My Github Page: https://github.com/FonderElite")
help = print(Fore.GREEN + '''
=============================================
+|   Hashing Algorithm using Python        |+
=============================================
+|   M a d e    By    F o n d e r E l i t e|+
+|-----------------------------------------|+
+|        Visit My Websites:               |+
+|http://singularity.rf.gd                 |+
+|http://droidtech.rf.gd                   |+
+|http://justice.rf.gd                     |+
+|         Social Media                    |+
+|Github: https://github.com/Fonderelite   |+
+|Twitter: https://twitter.com/elitefonder |+
 ===========================================
 Available Hashes:[SHA1,MD5,SHA224,SHA256]
''')

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
        print(Fore.GREEN +'''
 |￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣|
Dont be a Script Kiddie.
|＿＿＿＿＿＿＿＿＿＿＿____________|
(\__/) ||
(•ㅅ•) ||
/ 　 づ
        ''')


#command = print(Fore.MAGENTA + "[+]Input a command: ")
starting = Fore.YELLOW + "Starting to Hash in SHA-1"
tohash = input("Input a string to hash:")
print("Choose a your preffered hashing type:")
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


else:
    print(Fore.RED + '''
 ██████████ ███████████   ███████████      ███████    ███████████   ███
░░███░░░░░█░░███░░░░░███ ░░███░░░░░███   ███░░░░░███ ░░███░░░░░███ ░███
 ░███  █ ░  ░███    ░███  ░███    ░███  ███     ░░███ ░███    ░███ ░███
 ░██████    ░██████████   ░██████████  ░███      ░███ ░██████████  ░███
 ░███░░█    ░███░░░░░███  ░███░░░░░███ ░███      ░███ ░███░░░░░███ ░███
 ░███ ░   █ ░███    ░███  ░███    ░███ ░░███     ███  ░███    ░███ ░░░ 
 ██████████ █████   █████ █████   █████ ░░░███████░   █████   █████ ███
░░░░░░░░░░ ░░░░░   ░░░░░ ░░░░░   ░░░░░    ░░░░░░░    ░░░░░   ░░░░░ ░░░  ''')
