import requests as rq
import pandas as pd
import numpy as np

file = './file.csv'


def analyze_urls(urls):
    url_lengths = urls['url'].apply(len).values
    avg_length = np.mean(url_lengths)
    max_length = np.max(url_lengths)
    min_length = np.min(url_lengths)
    print(f"Средняя длина URL: {avg_length:.2f}")
    print(f"Максимальная длина URL: {max_length}")
    print(f"Минимальная длина URL: {min_length}")


def request_with_delays(urls):
    for i, row in urls.iterrows():
        print(f"Обработка URL: {row['url']}")
        output = rq.get(row['url'])
        if output.status_code == 200:
            with open(f"{row['name']}.html", 'w', encoding='utf-8') as f:
                f.write(output.text)
        else:
            print(f"Ошибка для URL {row['url']}: статус {output.status_code}")


def normalize_url_lengths(urls):
    url_lengths = urls['url'].apply(len).values
    normalized_lengths = (url_lengths - np.min(url_lengths)) / (np.max(url_lengths) - np.min(url_lengths))
    urls['normalized_length'] = normalized_lengths
    print("Нормализованные длины URL добавлены в DataFrame.")
    print(urls)

urls = pd.read_csv(file, delimiter=',', quotechar='"', on_bad_lines='skip')
analyze_urls(urls)
normalize_url_lengths(urls)
request_with_delays(urls)
