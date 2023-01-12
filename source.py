"""
This program was made by ss.spooky.ss#0003
This is a PUBLIC program, if you bought this product you got scammed

Follow me on TikTok @.3ekk

THIS PROGRAM WAS MADE FOR WINDOWS AND TESTED ON WINDOWS 11
"""

import os, time, threading
import cloudscraper
from colorama import Fore

print(Fore.MAGENTA + "This program was made by ss.spooky.ss#0003\nThis is a PUBLIC program, if you bought this program, sadly you got scammed\nFollow me on TikTok @.3ekk")
time.sleep(7)

try:
    requests = cloudscraper.create_scraper(
        browser={
            'browser': 'firefox',
            'platform': 'windows',
            'mobile': False
        }
    )
    # Set the window title, only works in windows
    os.system("title NGL Raider - Developed by ss.spooky.ss#0003")
    # Send NGL question function
    def Send(name, content, cooldown, pro, dev):  # Paramaters
        uuid = requests.get(
            "https://www.uuidgenerator.net/api/version4"
        )  # Request a UUID4 generator to simulate a deviceId
        url = "https://ngl.link/api/submit"  # API Link
        data = {
            "username": name,  # Username that the person wants to raid
            "question": content,  # MSG Content
            "deviceId": uuid.text,  # Generated UUID4
            "gameSlug": "",  # Some aditional param
            "referrer": "",  # Some aditional param
        }
        def error(r):  # Function to show info about the request
            if dev:  # Dev info
                print(
                    Fore.YELLOW + "[DEV] Website status code: " + str(r.status_code)
                )  # Status code
                print(Fore.YELLOW + "[DEV] Website text: " + r.text)  # Website Text
                print(Fore.YELLOW + "[DEV] Request data: " + str(data))  # Request data
            if r.status_code == 200:  # If the request worked then
                print(
                    Fore.GREEN + "[+] Question send!"
                )  # Print that the question was send
            else:  # Else (if error)
                print(
                    Fore.RED + "[-] Error when trying to send the request!"
                )  # Print error
        if pro == False:  # If no proxies
            
            # Default proc
            
            if dev:
                print(Fore.YELLOW + "[DEV] Sending request to https://ngl.link/api/submit")
            r = requests.post(url, data=data)  # Then normal post
            if dev:
                print(Fore.YELLOW + "[DEV] Request sent!")
            error(r)
            
        else:  # Else
            
            # Proxy Proc
            
            # Gets the proxy path using os.path.join
            HTTPPath = os.path.join(os.getcwd(), "proxies\httpProxy.txt")
            HTTPSPath = os.path.join(os.getcwd(), "proxies\httpsProxy.txt")
            # Opens the HTTP proxy path
            with open(HTTPPath, "r") as f:
                for v in f.readlines():  # Read all the lines in a for loop
                    if dev:
                        print(Fore.YELLOW + "[DEV] Finded HTTP proxy: " + v)
                    requests.proxies = {"http": v}
                    if dev:
                        print(
                            Fore.YELLOW
                            + "[DEV] Sending request to https://ngl.link/api/submit"
                        )
                        print(Fore.YELLOW + "[DEV] Request proxy: " + v)
                        print(Fore.YELLOW + "[DEV] Request data: " + str(data))
                    r = requests.post(url, data=data)  # Post with proxies
                    print(Fore.YELLOW + "[DEV] Request sent!")
                    error(r)
            # Opens the HTTPS proxy path
            with open(HTTPSPath, "r") as f:
                for v in f.readlines():  # Read all the lines in a for loop
                    if dev:
                        print(Fore.YELLOW + "[DEV] Finded HTTPS proxy: " + v)
                    requests.proxies = {"https": v}
                    if dev:
                        print(
                            Fore.YELLOW
                            + "[DEV] Sending request to https://ngl.link/api/submit"
                        )
                        print(Fore.YELLOW + "[DEV] Request proxy: " + v)
                        print(Fore.YELLOW + "[DEV] Request data: " + str(data))
                    r = requests.post(url, data=data)  # Post with proxies 
                    if dev:
                        print(Fore.YELLOW + "[DEV] Request sent!")
                    error(r)  # Function to debug error
        time.sleep(cooldown / 1000)  # Cooldown
        Send(name, content, cooldown, pro, dev)  # Repeat the same function
    # Process
    def process():
        os.system("cls")  # Cls to clear cmd
        
        # Username
        
        user = input(
            Fore.CYAN + "Enter the user username that you want to raid (eg: @instagram): @"
        )  # Asks for the username
        print(Fore.YELLOW + "Checking if the user exists...")
        r = requests.get(
            "https://ngl.link/" + user.lower()
        )  # Request to know if the user really exists
        if r.status_code == 200:  # If the request worked, then it does exist
            print(Fore.GREEN + "The username does exist!")
        else:  # Else (if dont worked)
            print(
                Fore.RED + "Error: The username does not exist or Rate Limit!"
            )  # Then the username doesnt exist or just a rate limit
            time.sleep(2)  # Time sleep to the person sees the error
            process()  # Restart the process
        os.system("cls")  # Cls to clear cmd
        
        # Message
        
        msg = input(
            Fore.CYAN + "Enter the message that you want to send (max: 300 chars): "
        )  # Asks for the massage content
        if len(msg) > 300:  # If the messa lenght is over 300 chars
            print(Fore.RED + "Input error!")  # Then print error
            time.sleep(2)  # Time sleep to the person sees the error
            process()  # Restart the process
        os.system("cls")  # Cls to clear cmd
        
        # Default config
        
        defcon = input(Fore.CYAN + 'Do you want to use the default config? Highly recommended if you dont know a lot about programming (y/n): ')
        if defcon == "y":  # If the person accepts the overclock
            os.system("cls")  # Cls to clear cmd
            Send(user, msg, 2000, False, False)
        elif defcon == "n":  # If the person doesnt accept the overclock
            pass  # Then pass
        else:  # If the person dont put (y/n) then
            print(Fore.RED + "Input error!")  # Print input error
            time.sleep(2)  # Time sleep to the person sees the error
            process()  # Restart the process   
        os.system("cls")  # Cls to clear cmd
        
        # Threads
        
        overclock = input(
            Fore.CYAN + "(May error) Do you want to use threads (y/n): "
        )  # Asks if the person wants to use threads
        prothreading = False  # Threads bool variable
        threadss = 0  # How many threads
        if overclock == "y":  # If the person accepts the overclock
            prothreading = True  # Threads bool variable = true
            try:
                num = int(
                    input(Fore.CYAN + "How many threads do you want to use: ")
                )  # Ask how many threads the person wants to use
                threadss = num  # Set the threads num
            except:
                print(
                    Fore.RED + "Input error!"
                )  # If the person puts something that is not a number, it will result in a input error
                time.sleep(2)  # Time sleep to the person sees the error
                process()  # Restart the process
        elif overclock == "n":  # If the person doesnt accept the overclock
            pass  # Then pass
        else:  # If the person dont put (y/n) then
            print(Fore.RED + "Input error!")  # Print input error
            time.sleep(2)  # Time sleep to the person sees the error
            process()  # Restart the process
        os.system("cls")  # Cls to clear cmd
        
        # Cooldown
        
        cd = 0  # Cooldown time
        try:
            num = int(
                input(
                    Fore.CYAN + "Enter cooldown in MILISECONDS (recommend to use 1000): "
                )
            )  # Asks the cooldown
            cd = num  # Set the cooldown variable
        except:
            print(
                Fore.RED + "Input error!"
            )  # If the person puts something that is not a number, it will result in a input error
            time.sleep(2)  # Time sleep to the person sees the error
            process()  # Restart the process
        os.system("cls")  # Cls to clear cmd
        
        # Proxies
        
        prq = input(
            Fore.CYAN + "Do you want to use proxies (y/n): "
        )  # Ask if the person wants to use proxies
        proxy = False
        if prq == "y":  # If the person accept using proxies
            proxy = True
        elif prq == "n":  # If the person doesnt accept the proxies
            pass  # Then pass
        else:  # If the person dont put (y/n) then
            print(Fore.RED + "Input error!")  # Show input error
            time.sleep(2)  # Time sleep to the person sees the error
            process()  # Restart the process
        os.system("cls")  # Cls to clear cmd
        
        # Developer Mode
        
        dm = input(
            Fore.CYAN + "Do you want to use developer mode (y/n): "
        )  # Ask if the person wants to use proxies
        dev = False
        if dm == "y":  # If the person accept using developer mode
            dev = True
        elif dm == "n":  # If the person doesnt accept the developer mode
            pass  # Then pass
        else:  # If the person dont put (y/n) then
            print(Fore.RED + "Input error!")  # Show input error
            time.sleep(2)  # Time sleep to the person sees the error
            process()  # Restart the process
        os.system("cls")  # Cls to clear cmd
        
        # Last question
        
        areus = input(
            Fore.RED + "Are you sure that you want to do the NGL raid? (y/n): "
        )  # Asks if the person wants to do the NGL Raid (just a warning xd)
        if areus == "y":  # If the person says yes
            os.system("cls")  # Cls to clear cmd
            # Execute threading
            if prothreading:  # If the person accepted threading
                for i in range(threadss):  # Will execute the threads
                    pro = threading.Thread(
                        target=Send, name="Sender", args=[user, msg, cd, proxy, dev]
                    )  # Setup the send function with args
                    pro.start()  # Start the thread
                    time.sleep(1)  # Cooldown to look better
            else:  # If the person recused threading
                Send(user, msg, cd, proxy, dev)  # Send normal function
        elif areus == "n":  # If the person dont want to raid then it will just exit
            exit()  # Exit cool function
        else:  # If the person didnt put (y/n) then
            print("Input error!")  # Print input error
            process()  # Restart process
    process()  # Start the process
except Exception as ex:  # If ANY python error happens in the script, it will show a fatal error
    print(Fore.RED + "FATAL ERROR " + str(ex))
    time.sleep(4)  # Cooldown to the person see the error
    exit()  # Will exit the application
