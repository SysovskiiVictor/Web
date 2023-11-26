import time
import webbrowser


def Open(urls, interval):
    for url in urls:
        webbrowser.open(url, new=2)
        time.sleep(interval)


def main():
    interval = int(input('Введите интервал показа страниц в секундах: ').strip())
    urls = ['https://www.gismeteo.ru/weather-sankt-peterburg-4079/', 'https://ya.ru/', 'https://www.google.com/?hl=ru']
    Open(urls, interval)

    while True:
        new_url = input("Введите новый URL-адрес или 0, чтобы завершить программу: ").strip()
        if new_url == '0':
            break
        Open([new_url], interval)


if __name__ == "__main__":
    main()

