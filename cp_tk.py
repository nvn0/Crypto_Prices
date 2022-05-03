from tkinter import *
import time
import cbpro
import requests





try:
    public_client = cbpro.PublicClient()

    result = public_client.get_products()
except:
    print("Error! - Looks like you are not connected to the internet...")
    exit()


def Crypto_prices():

    localtime = time.localtime()
    time_now = time.strftime("%H:%M:%S", localtime)


    BTC_price = public_client.get_product_ticker('BTC-EUR')

    ETH_price = public_client.get_product_ticker('ETH-EUR')

    ADA_price = public_client.get_product_ticker('ADA-EUR')

    # EGLD_price = public_client.get_product_ticker('EGLD-EUR')

    XMR_price = requests.get("https://api.kraken.com/0/public/Ticker?pair=XMREUR").json()['result']['XXMRZEUR']['c'][0]

    SOL_price = public_client.get_product_ticker('SOL-EUR')

    AVAX_price = public_client.get_product_ticker('AVAX-EUR')

    BCH_price = public_client.get_product_ticker('BCH-EUR')

    LTC_price = public_client.get_product_ticker('LTC-EUR')


    texto = f'''
    Hour: {time_now}
    \nBTC: {BTC_price['price']} €
    ETH: {ETH_price['price']} €
    XMR: {str(XMR_price)[:6]} €
    ADA: {ADA_price['price']} €







'''

    texto_dinamico["text"] = texto




def last_trades(): # option 4

    try:
        y = input("Digit the pair of the asset(Ex: BTC-EUR): ")
        num_trades = int(input("Number of trades that you want to see? "))

        lasttrades = public_client.get_product_trades(y)

    except:
        print("\nERROR! - INVALID OPTION!")
        last_trades()
    else:

        try:
            print(f"\nThe last {num_trades} trades")
            for s in range(num_trades):
                print(next(lasttrades))
        except:
            print("\nERROR! - INVALID OPTION!")
            last_trades()
        else:
            pass





def hello():
    msg = "Hello, this is a Tkinter test"
    #print(msg)
    txt = text_entry.get()
    #print("Hello", txt)
    texto_dinamico["text"] = msg
    texto_dinamico2["text"] = "Hello", txt



# janela:
janela = Tk()
janela.title("Teste Tkinter")
janela.geometry("400x300")
#janela.configure(background="black")


# Apresentar texto:
texto_orientaçao = Label(janela, text="Teste de texto")
texto_orientaçao.grid(column=6, row=0, padx=10, pady=10) # defenir posição


# Entrada de texto
# text_entry = Entry(janela)
# text_entry.grid(column=0, row=2, padx=10, pady=10)




# Botão(com funções):
botao = Button(janela, text="Show", command=Crypto_prices)
botao.grid(column=6, row=3, padx=10, pady=10)



# Apresentar texto após carregar no botão
texto_dinamico = Label(janela, text="")
texto_dinamico.grid(column=0, row=4, padx=10, pady=10)


texto_dinamico2 = Label(janela, text="")
texto_dinamico2.grid(column=8, row=4, padx=10, pady=10)





# Deixar no final(de modo a manter a janela aberta):
janela.mainloop()
