import logging
import urllib
from bs4 import BeautifulSoup


class Extraction:
    def __init__(self, url):
        self.url = url
        self.soup = self.validate_url()
        self._titolo = self.extract_titolo()
        self._prezzo = self.extract_prezzo()
        self._prezzo_scontato = self.extract_prezzo_scontato()

    def validate_url(self):
        try:
            html = urllib.request.urlopen(self.url)

            return BeautifulSoup(html, "html.parser")
        except urllib.error.HTTPError:
            logging.error("Url non trovato: HTTP Error 404")
            exit()

    def extract_titolo(self):
        title = self.soup.find(id="productTitle")
        if title is not None:
            return str(title.get_text()).strip()
        else:
            logging.error(" Titolo Non Trovato, assicurati sia un link di un prodotto amazon valido!")
            exit()
    def extract_prezzo(self):
        prezzo = self.soup.find(id="priceblock_ourprice")
        if prezzo is not None:
            return float(str(prezzo.get_text().replace("€", "").replace(",", ".").replace("EUR", "")).strip())
        else:
            logging.error(" Prezzo Non trovato, assicurati sia un link di un prodotto amazon valido!")
            exit()
    def extract_prezzo_scontato(self):
        prezzo_scontato = self.soup.find(id="priceblock_dealprice")
        if prezzo_scontato is not None:
            return float(str(prezzo_scontato.get_text().replace("€", "").replace(",", ".")).strip())
        else:
            return None

    def return_dict(self):
        return  {"titolo" : self._titolo, "prezzo" : self._prezzo, 
                 "prezzo_scontato" : self._prezzo_scontato}
    def __repr__(self):
        return f"Il prezzo dell' oggetto: {self._titolo} è {self._prezzo}"
