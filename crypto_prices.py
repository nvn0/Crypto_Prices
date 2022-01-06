import cbpro
import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)


public_client = cbpro.PublicClient()
#
# result = public_client.get_products()

# for row in result:
#     print(row)



def Crypto_prices():

    BTC_price = public_client.get_product_ticker('BTC-EUR')
    print (Fore.YELLOW + "BTC:", BTC_price['price'], "€")

    ETH_price = public_client.get_product_ticker('ETH-EUR')
    print (Fore.BLUE + "ETH:", ETH_price['price'], "€")

    ADA_price = public_client.get_product_ticker('ADA-EUR')
    print (Fore.CYAN + "ADA:", ADA_price['price'], "€")

    # EGLD_price = public_client.get_product_ticker('EGLD-EUR')
    # print (Fore.BLUE + "EGLD:",EGLD_price['price'], "€")

    SOL_price = public_client.get_product_ticker('SOL-EUR')
    print (Fore.GREEN + "SOL:", SOL_price['price'], "€")

    AVAX_price = public_client.get_product_ticker('AVAX-EUR')
    print (Fore.RED + "AVAX:", AVAX_price['price'], "€")




opc = ""
while opc != "exit":


    print("\n==============================")
    print("        Crypto Prices")
    print("==============================")
    print("[1] - Show Crypto Prices")
    print("[exit] - Show Crypto Prices")
    print("==============================")


    opc = input("Choose an option: ")

    if opc == "1":
        print("\nCrypto Prices:")
        Crypto_prices()
    elif opc == "000": # Secret command
        break
    elif opc == "2":
        print("2")
    else:
        print(Fore.RED + "\nERROR! - INVALID OPTION!")










