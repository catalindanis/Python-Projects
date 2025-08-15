import requests
from bs4 import BeautifulSoup
import openpyxl
import time

# Configurare
CAEN_CODE = "4520"
JUDET = "cluj"
MAX_PAGINI = 3
OUTPUT_FILE = "firme_cluj_auto_complet.xlsx"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# Funcție de extras date din pagina principală
def extrage_firme_de_pe_pagina(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    firme = []

    for tr in soup.select("table tbody tr"):
        cols = tr.find_all("td")
        if len(cols) >= 2:
            nume = cols[0].text.strip()
            link = cols[0].find("a")["href"] if cols[0].find("a") else ""
            localitate = cols[1].text.strip()
            firme.append({
                "nume": nume,
                "localitate": localitate,
                "link": link
            })

    return firme

# Funcție de extras date din pagina firmei
def extrage_detalii_firma(url_firma):
    email = telefon = site = descriere = ""

    if not url_firma.startswith("https://"):
        url_firma = "https://www.listafirme.ro" + url_firma

    try:
        response = requests.get(url_firma, headers=HEADERS)
        soup = BeautifulSoup(response.content, "html.parser")

        contact_div = soup.find("div", class_="col-md-6")

        if contact_div:
            text = contact_div.get_text(separator="\n")
            if "Email:" in text:
                email = text.split("Email:")[1].split("\n")[0].strip()
            if "Telefon:" in text:
                telefon = text.split("Telefon:")[1].split("\n")[0].strip()
            if "Web:" in text:
                site = text.split("Web:")[1].split("\n")[0].strip()

        descriere_tag = soup.find("div", class_="panel-body")
        if descriere_tag:
            descriere = descriere_tag.get_text(separator="\n").strip().split("\n")[0]

    except Exception as e:
        print(f"⚠️ Eroare la {url_firma}: {e}")

    return email, telefon, site, descriere

# Scrape + salvare Excel
def ruleaza_scraping():
    toate_firmele = []

    for pagina in range(1, MAX_PAGINI + 1):
        url = f"https://www.listafirme.ro/cauta/cod-caen/{CAEN_CODE}/judet/{JUDET}/pagina{pagina}.htm"
        print(f"🔎 Pagina {pagina}...")
        firme = extrage_firme_de_pe_pagina(url)
        if not firme:
            break

        for firma in firme:
            print(f"➡️ {firma['nume']} ({firma['localitate']})")
            email, telefon, site, descriere = extrage_detalii_firma(firma["link"])
            firma.update({
                "email": email,
                "telefon": telefon,
                "site": site,
                "descriere": descriere
            })
            toate_firmele.append(firma)
            time.sleep(1)  # pauză între firme

        time.sleep(2)  # pauză între pagini

    # Salvare Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Firme Cluj Auto"

    ws.append(["Nume", "Oraș", "Email", "Telefon", "Site", "Descriere", "Link firmă", "Răspuns"])

    for firma in toate_firmele:
        ws.append([
            firma["nume"],
            firma["localitate"],
            firma["email"],
            firma["telefon"],
            firma["site"],
            firma["descriere"],
            "https://www.listafirme.ro" + firma["link"],
            ""
        ])

    wb.save(OUTPUT_FILE)
    print(f"\n✅ Fișier generat: {OUTPUT_FILE}")

# MAIN
if __name__ == "__main__":
    ruleaza_scraping()
