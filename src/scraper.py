import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

SECOES = {
    "economia": "https://g1.globo.com/economia/",
    "politica": "https://g1.globo.com/politica/",
    "mundo": "https://g1.globo.com/mundo/",
    "tecnologia": "https://g1.globo.com/tecnologia/",
    "esportes": "https://ge.globo.com/",
}

def scrape_g1_by_section():
    all_data = []

    for tema, url in SECOES.items():
        print(f"🔎 Coletando notícias de {tema}...")
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")

            
            articles = soup.find_all("a", class_="feed-post-link") + \
                       soup.find_all("a", class_="feed-post-body-title") + \
                       soup.find_all("a", class_="tec--card__title__link")  

            for article in articles:
                title = article.get_text(strip=True)
                link = article.get("href")
                if link: 
                    all_data.append({"tema": tema, "titulo": title, "link": link})

        except Exception as e:
            print(f"⚠️ Erro ao coletar {tema}: {e}")

        sleep(1) 

    df = pd.DataFrame(all_data)
    df.to_csv("data/raw/g1_news_by_section.csv", index=False, encoding="utf-8")
    print(f"✅ {len(df)} notícias salvas em data/raw/g1_news_by_section.csv")
    return df

if __name__ == "__main__":
    scrape_g1_by_section()
