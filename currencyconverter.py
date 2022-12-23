import requests
from bs4 import BeautifulSoup


def url_2_soup(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    return soup


currency = {"USD": 0,
            "TL": 1,
            "EURO": 0,
            "JAPAN": 0,
            "ENGSTR": 0,
            "AUD": 0}


def convertCurrency(quantity, From, To):
    global currency

    if not (From == To):
        if From == "USD" or To == "USD" and not (From == To):
            site = url_2_soup("https://www.google.com/finance/quote/USD-TRY")
            usd_ = float(str(site).split("YMlKec fxKbKc\">")[1].split("</div>")[0])
            currency["USD"] = 1 / usd_
        if From == "EURO" or To == "EURO" and not (From == To):
            site = url_2_soup("https://www.google.com/finance/quote/EUR-TRY")
            euro_ = float(str(site).split("YMlKec fxKbKc\">")[1].split("</div>")[0])
            currency["EURO"] = 1 / euro_
        if From == "JAPAN" or To == "JAPAN" and not (From == To):
            site = url_2_soup("https://www.google.com/finance/quote/TRY-JPY")
            japan_ = float(str(site).split("YMlKec fxKbKc\">")[1].split("</div>")[0])
            currency["JAPAN"] = 1 / japan_
        if From == "ENGSTR" or To == "ENGSTR" and not (From == To):
            site = url_2_soup("https://www.google.com/finance/quote/GBP-TRY")
            sterlin_ = float(str(site).split("YMlKec fxKbKc\">")[1].split("</div>")[0])
            currency["ENGSTR"] = 1 / sterlin_
        if From == "AUD" or To == "AUD":
            site = url_2_soup("https://www.google.com/finance/quote/AUD-TRY")
            aud_ = float(str(site).split("YMlKec fxKbKc\">")[1].split("</div>")[0])
            currency["AUD"] = 1 / aud_
        return quantity / currency[From] * currency[To]
    else:
        return quantity


print(convertCurrency(100, "USD", "USD"))
