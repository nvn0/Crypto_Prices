import cbpro
import colorama
from colorama import Back, Fore, Style
import platform
import os
import time
import requests
#import sys
from plyer import notification



colorama.init(autoreset=True)


clear_command = "cls" if platform.system() == "Windows" else "clear"

os.system(clear_command)

try:
    public_client = cbpro.PublicClient()

    result = public_client.get_products()
except:
    print(Fore.RED + "Error! - Looks like you are not connected to the internet...")
    exit()


# for row in result:
#     print(row)



def Crypto_prices():

    localtime = time.localtime()
    time_now = time.strftime("%H:%M:%S", localtime)
    print("\nHour:",time_now)

    BTC_price = public_client.get_product_ticker('BTC-EUR')
    print(Fore.YELLOW + "\nBTC:", BTC_price['price'], "€")

    ETH_price = public_client.get_product_ticker('ETH-EUR')
    print(Fore.BLUE + "ETH:", ETH_price['price'], "€")

    ADA_price = public_client.get_product_ticker('ADA-EUR')
    print(Fore.CYAN + "ADA:", ADA_price['price'], "€")

    # EGLD_price = public_client.get_product_ticker('EGLD-EUR')
    # print (Fore.BLUE + "EGLD:",EGLD_price['price'], "€")

    XMR_price = requests.get("https://api.kraken.com/0/public/Ticker?pair=XMREUR").json()['result']['XXMRZEUR']['c'][0]
    print(Fore.YELLOW + "XMR:", str(XMR_price)[:6], "€")

    SOL_price = public_client.get_product_ticker('SOL-EUR')
    print(Fore.GREEN + "SOL:", SOL_price['price'], "€")

    AVAX_price = public_client.get_product_ticker('AVAX-EUR')
    print(Fore.RED + "AVAX:", AVAX_price['price'], "€")

    BCH_price = public_client.get_product_ticker('BCH-EUR')
    print(Fore.GREEN + "BCH:", BCH_price['price'], "€")

    LTC_price = public_client.get_product_ticker('LTC-EUR')
    print(Fore.LIGHTWHITE_EX + "LTC:", LTC_price['price'], "€")

    opc2 = ""
    while opc2 != "exit":

        opc2 = input("\n>_: ")

        if opc2 == "exit":
            print("A sair...")
        elif opc2 == "refresh" or opc2 == "r":
            Crypto_prices()
        elif opc2 == "000":  # Secret command
            exit()



def list(): # option 2


    for row in result:
        print(row['id'])




    opc3 = ""
    while opc3 != "exit":

        opc3 = input("\n>_: ")

        if opc3 == "exit":
            print("A sair...")
        elif opc3 == "000":  # Secret command
            exit()






def search_asset(): # option 3

    try:
        asstc = input("Digit the name of the crypto asset(Ex: btc): ")
        asstf = input("Digit the name of the fiat asset(Ex: usd): ")
        #X_price = public_client.get_currencies()

        asst = '-'.join([asstc, asstf])


        X_price = public_client.get_product_ticker(asst)

        asst2 = ''.join([asstc, asstf]).upper()


        Z_price = requests.get(f"https://api.kraken.com/0/public/Ticker?pair={asst2}").json()['result']


    except:

        print(Fore.RED + "\nERROR! - INVALID OPTION!")
        search_asset()
    else:
        print("Coinbase:\n", X_price)
        print("Kraken:\n", Z_price)


    # for x in X_price:
    #     print(x)
    #print("BCH:", X_price['price'], "€")

    opc4 = ""
    while opc4 != "exit":

        opc4 = input("\n>_: ")

        if opc4 == "exit":
            print("A sair...")
        elif opc4 == "a" or "r":
            search_asset()
        elif opc4 == "000":  # Secret command
            exit()



def last_trades(): # option 4

    try:
        y = input("Digit the pair of the asset(Ex: BTC-EUR): ")
        num_trades = int(input("Number of trades that you want to see? "))

        lasttrades = public_client.get_product_trades(y)

    except:
        print(Fore.RED + "\nERROR! - INVALID OPTION!")
        last_trades()
    else:

        try:
            print(f"\nThe last {num_trades} trades")
            for s in range(num_trades):
                print(next(lasttrades))
        except:
            print(Fore.RED + "\nERROR! - INVALID OPTION!")
            last_trades()
        else:
            pass





    opc4 = ""
    while opc4 != "exit":

        opc4 = input("\n>_: ")

        if opc4 == "exit":
            print("A sair...")
        elif opc4 == "000":  # Secret command
            #sys.exit()
            exit()



def price_notify(coin, t2):

    while True:
        time.sleep(t2)
        c_price = public_client.get_product_ticker(f'{coin}')

        notification.notify(
            title=f"{coin}:",
            message=f"{c_price['price']} €",
            app_icon="",
            timeout=10,
        )






opc = ""
while opc != "exit":
    os.system(clear_command)


    print("\n===================================================")
    print("                     Crypto Prices")
    print("===================================================")
    print("  [1] - Show Crypto Prices")
    print("  [2] - List of assets")
    print("  [3] - Search an asset")
    print("  [4] - Last trades")
    print("  [5] - Notify prices")
    print("  [exit]")
    print("===================================================")


    opc = input("Choose an option: ")

    if opc == "1":
        os.system(clear_command)
        print("\nCrypto Prices:")
        Crypto_prices()
    elif opc == "000": # Secret command
        os.system(clear_command)
        exit()
    elif opc == "2":
        os.system(clear_command)
        print("List of Cryptos")
        list()
    elif opc == "3":
        os.system(clear_command)
        print("Search an asset")
        search_asset()
    elif opc == "4":
        os.system(clear_command)
        print("Last trades")
        last_trades()
    elif opc == "5":
        os.system(clear_command)
        print("Set a notification")
        coin = input("What coin you want to be notify about?(Ex: BTC-EUR)")
        t = int(input("Insert the time interval for the reminder (minutes): "))
        t2 = t * 60
        price_notify(coin, t2)
    elif opc == "exit":
        print("\nA sair...")
    else:
        print(Fore.RED + "\nERROR! - INVALID OPTION!")










