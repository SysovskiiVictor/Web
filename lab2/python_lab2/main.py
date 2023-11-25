import time
import webbrowser


def get_user_input(prompt):
    return input(prompt).strip()


def open_urls_with_interval(urls, interval):
    for url in urls:
        webbrowser.open(url, new=2)
        time.sleep(interval)


def main():
    # Интервал между открытием страниц (введенный пользователем)
    interval = int(get_user_input('Введите интервал показа страниц в секундах: '))

    # Список URL-адресов web-страниц
    urls = ['https://mail.google.com', 'https://www.youtube.com', 'https://translate.google.com']

    # Открытие URL с заданным интервалом
    open_urls_with_interval(urls, interval)

    # Добавление новых URL-адресов
    while True:
        new_url = get_user_input("Введите новый URL-адрес (или 'q' для завершения): ")
        if new_url == 'q':
            break
        urls.append(new_url)
        open_urls_with_interval([new_url], interval)


if __name__ == "__main__":
    main()

