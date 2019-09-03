import os
import pickle
from time import sleep
from email_sender import Email
from extract import Extraction
from oggetto import Item


def main():
    oggetto = Extraction("https://www.amazon.it/Demiawaking-Falsamaglia-Connettore-Sgancio-velocit%C3%A0/dp/B07PDKYWVL?pf_rd_p=c11f42df-e88f-4740-b4d0-b23235d9f226&pd_rd_wg=ZLtAS&pf_rd_r=21DAXM421P637F1MFV50&ref_=pd_gw_cr_cartx&pd_rd_w=vjKUv&pd_rd_r=2910a484-0c05-4431-9fa8-1dc1a543f0f6")

    print(oggetto.return_dict())
    #IF pickle exist then restore it
    if os.path.exists("item_attuale.pickle"):
        pickle_off = open("item_attuale.pickle", "rb")
        tmp_item = pickle.load(pickle_off)
        # if the item's title of the pickle restored is equal the title of the item passed in "oggetto"
        # use the picke object otherwise use the object "oggetto" passed
        if tmp_item.titolo == Item(oggetto.return_dict()).titolo:
            item_iniziale = tmp_item
        else:
            item_iniziale = Item(oggetto.return_dict())
    #IF doesn't exist use the object "oggetto" passed
    else:
        item_iniziale = Item(oggetto.return_dict())
    #email where to send
    mia_email = Email("email where to send")

    while True:
        item_attuale = Item(oggetto.return_dict())
        #if the item has a "prezzo scontato" use that as main price for comparation
        #otherwise use the "normal price"
        if item_iniziale.prezzo_scontato is not None:
            prezzo1 = item_iniziale.prezzo_scontato
        else:
            prezzo1 = item_iniziale.prezzo
        if item_attuale.prezzo_scontato is not None:
            prezzo2 = item_attuale.prezzo_scontato
        else:
            prezzo2 = item_attuale.prezzo

        if item_iniziale.prezzo < item_attuale.prezzo:
            messaggio = """\
                    il prezzo è passato da {} a {}""".format(prezzo1, prezzo2)
            mia_email.send(subject=item_attuale.titolo, messaggio=messaggio)
            break
        else:
            messaggio = """\
                    il prezzo è passato da {} a {}""".format(prezzo1, prezzo2)
            print(messaggio)
            #dump the picke  with the actual price
            pickling_on = open("item_attuale.pickle", "wb")
            pickle.dump(item_attuale, pickling_on)
            pickling_on.close()
        sleep(300)

if __name__ == "__main__":
    main()
