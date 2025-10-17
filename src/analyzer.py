import pandas as pd
from collections import Counter
import re

def analyze_by_theme(filepath="data/raw/g1_news_by_section.csv"):
    df = pd.read_csv(filepath)
    results = []

    for tema, group in df.groupby("tema"):
        all_titles = " ".join(group["titulo"].tolist()).lower()
        words = re.findall(r'\b[a-zà-ú]{4,}\b', all_titles)
        counter = Counter(words)
        common = counter.most_common(10)
        for word, freq in common:
            results.append({"tema": tema, "palavra": word, "frequencia": freq})

    result_df = pd.DataFrame(results)
    result_df.to_csv("data/processed/frequency_by_theme.csv", index=False)
    print("Frequência de palavras por tema salva em data/processed/frequency_by_theme.csv")
    return result_df

if __name__ == "__main__":
    print(analyze_by_theme())
