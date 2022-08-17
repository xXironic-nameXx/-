from libtorrent import *
from pygame import mixer
import time
import datetime
import os
import climage

p = print
r = input
m = "./music/"


def skip():
    if not mixer.music.get_busy():
        return 1


def back(a):
    if a == "вернуться" or a == "<=":
        menu()


def d_getter(g):
    d = []
    try:
        for f in os.listdir(g):
            if os.path.isfile(os.path.join(g, f)):
                d.append(f)
    finally:
        return sorted(d)


def song_cover(d, s):
    c = d[:d.find(".")]
    x = "ETC/"
    o = ".jpg"
    if c + o in os.listdir(m + x):
        p(climage.convert(m + x + c + o, is_unicode=1, is_truecolor=1, is_256color=0, is_16color=0, is_8color=0,
                          width=s), end="")


def cover(j, k, s):
    p(climage.convert(str(j) + "/art.jpg", is_truecolor=1, is_256color=0, is_16color=0, is_8color=0, is_unicode=1,
                      width=s) if "art.jpg" in k else "", end="")


def dimens():
    x = r("большая картика? (да/нет): ")
    back(x)
    return [50, 100][x == "да"]


def z(path=m):
    f_list = []
    d_list = []

    try:
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)):
                f_list.append(f)
            else:
                if os.path.isdir(os.path.join(path, f)):
                    d_list.append(f)
    finally:
        p("""
████─████─████─█──█─█──█────██─
█──█─█▄▄▄─█────█▄▄█─█─▄█────█─█
█──█─█────█────█──█─█▀─█──███──
█──█─████─████─█──█─█──█──███──
        """)
        f_list = sorted(f_list)
        song_cover(f_list[1], 30)
        for i, j in enumerate(f_list):
            if j != ".DS_Store":
                p(j, end=[", ", "\n"][len(f_list[:i]) % 3 != 0])
        if len(d_list) != 0:
            p("""
████──████─████──████──█──█─█────█────█████
█──█──█──█─█────█────█─████─█────█────█───█
█▀▀█──█──█─█▀▀█─█────█─█▐─█─█▀▀█─█──███─███
█──█─██──█─████──████──█──█─████─█──███─███
            """)
            a = d_list[0]
            cover((m + a), d_getter(m + a), 30)
            for i, j in enumerate(d_list):
                if j != "ETC":
                    p(j, end=[", ", "\n"][len(d_list[:i]) % 2 != 0])


def band(a):
    s = "ETC/bands/"
    p(climage.convert(m + s + a + ".jpg", is_truecolor=1, is_256color=0, is_16color=0, is_8color=0, is_unicode=1,
                      width=50), end="")
    x = open(m + s + a + ".txt").read()
    albums = eval(x[x.find("[") + 1:x.find("]")])
    p(x[x.find('"""') + 3:x.rfind('"""') - 2])
    p()
    p(albums)
    c = r("какой альбом слушаем?: ")
    back(c)
    z(m + c)
    g = m + c
    f_list = []
    p()
    try:
        for f in os.listdir(g):
            if os.path.isfile(os.path.join(g, f)):
                f_list.append(f)
    finally:
        if r("размешать (да/нет)") == "нет":
            f_list = sorted(f_list)
        else:
            f_list = f_list
        for i in f_list:
            p(i)
        time.sleep(3)
        cover(g, f_list, dimens())
        p("")
        x = r("сначала/ с какой-то песни (1 - сначало/ любая другая цифра): ")
        back(x)
        for i in f_list[int(x) - 1 * (".DS_Store" not in f_list):]:
            p(i + " ", end="")
            play(g, i)


def play(h, y):
    mixer.init()
    f = False in [i not in y for i in [".txt", ".m3u", ".jpg", ".png", ".DS_Store"]]
    while f == 0:
        mixer.music.load(str(h) + "/" + y)
        mixer.music.play()
        a = r("остановить/ следующий: ")
        back(a)
        if a == "остановить":
            mixer.music.pause()
            v = r("начать(начнёт сначала, никак подругому на данной момент)? (да): ")
            back(v)
            while v != "да":
                continue
            else:
                mixer.music.unpause()
                pause = 1
        else:
            mixer.music.unload()
            f = skip()
            pause = 0
        if pause != 1:
            f = skip()
    else:
        p("закончил играть")



def home():
    z()
    p()
    p("используйте 'вернуться' или '<=', чтобы выйти из проигрывателя")
    a = r("альбом/ песня/ группа: ")
    back(a)
    if a == "альбом":
        if r("песню/ целый альбом: ") == "песню":
            h = m + r("напишите названия альбома сюда: ")
            f_list = []

            try:
                for f in os.listdir(h):
                    if os.path.isfile(os.path.join(h, f)):
                        f_list.append(f)
            finally:
                cover(h, f_list, dimens())
                p()
            z(h)
            p()
            c = r("напишите название песни сюда: ")
            back(c)
            play(h, c)
            menu()
        else:
            c = r("напишите его названия сюда: ")
            g = m + c
            back(c)
            f_list = []
            p()
            try:
                for f in os.listdir(g):
                    if os.path.isfile(os.path.join(g, f)):
                        f_list.append(f)
            finally:
                if r("размешать (да/нет): ") == "нет":
                    f_list = sorted(f_list)
                else:
                    f_list = f_list
                for i in f_list:
                    p(i)
                time.sleep(3)
                cover(g, f_list, dimens())
                p("")
                x = r("сначала/ с какой-то песни (1 - сначало/ любая другая цифра): ")
                back(x)
                for i in f_list[int(x) - 1 * (".DS_Store" not in f_list):]:
                    p(i + " ", end="")
                    play(g, i)
            menu()
    elif a == "песня":
        d = r("напишите название песни сюда: ")
        back(d)
        song_cover(d, dimens())
        p("Играю: " + d, end=" ")
        play(m, d)
    else:
        f_list = []
        g = m + "ETC/bands"
        try:
            for f in os.listdir(g):
                if os.path.isfile(os.path.join(g, f)):
                    f_list.append(f)
        finally:
            f_list = sorted(f_list)
            for i in f_list:
                if ".txt" in i:
                    p(i[:i.find(".")])
        b = r("группа: ")
        back(b)
        band(b)
    menu()


def torrent():
    p("""
────────────────────────
█████───███─███────█████
──█─────█─█─█─█──────█──
──█─────███─███▐▀─▌▐─█──
──█─█▀█─█───█──▐▀─██─█──
──█─███─█───█──▐█─▌▐─█──
────────────────────────
    """)

    ses = session()
    c = r("магнитик: ")
    back(c)
    handle = add_magnet_uri(ses, c, {"save_path": m, "storage_mode": storage_mode_t(2)})
    ses.start_dht()

    p(datetime.datetime.now())

    p("скачиваю метадату...")
    while not handle.has_metadata():
        time.sleep(1)
    p("метадату у нас!")

    p("Поехали", handle.name())
    state_str = ["жду", "проверяю", "скачиваю метадату", "торрентю", "закончил"]
    s = handle.status()
    p('(down: %.1f kb/s up: %.1f kB/s дорогие сидеры: %d) %s ' % (
        s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
    if r("стримить торрент(если высокая скорость)? да/нет: ") == "нет":
        while handle.status().state != torrent_status.seeding:
            p('%.2f%% скачено (down: %.1f kb/s up: %.1f kB/s дорогие сидеры: %d) %s ' % (
                s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
            time.sleep(5)
        p(handle.name(), "закончил!")
        p(datetime.datetime.now())
        p("переименуйте картинку альбома на art.jpg")
        time.sleep(5)
        menu()
    else:
        menu()


def menu():
    if r("торрент/ дом: ") == "дом":
        home()
    else:
        torrent()


p("""
▄▄▄▄▄────▄▄▄───────██████──────▄───▄──▄▄▄▄▄
██──█───█───█─────█▒▒▒▒▒▒█─────█───█──█──██
██─█────█───█────█▒▒▒▒▒▒▒▒█────█████──█████
██████──█───█───█▒▒▒▒▒▒▒▒▒▒█───█───█──█──██
██───█──█───█──█▒▒▒▒▒▒▒▒▒▒▒▒█──█───█──█──██
███████████████████████████████████████████
█▒▒▒▒▒▒▒▒▒▒▒▒█───────────────█▒▒▒▒▒▒▒▒▒▒▒▒█
─█▒▒▒▒▒▒▒▒▒▒█─────────────────█▒▒▒▒▒▒▒▒▒▒█─
──█▒▒▒▒▒▒▒▒█───────────────────█▒▒▒▒▒▒▒▒█──
───█▒▒▒▒▒▒█─────────────────────█▒▒▒▒▒▒█───
────██████───────────────────────██████────

                Н а ч а т ь ?
            да / нет / инструкция
""")
n = r()
if n == "да":
    menu()
elif n == "инструкция":
    p("""
    █▀▀█──█▀█──────█████───
    █▄█▀──█─█─────█▒▒▒▒▒█──
    █▀▀█──█─█────█▒▒▒▒▒▒▒█─
    █▄▄█──███───█▒▒▒▒▒▒▒▒▒█
    ░░░░░░░░░░░█░░░░░░░░░░░
    █▒▒▒▒▒▒▒▒▒█──▐▌─█─████─
    ─█▒▒▒▒▒▒▒█───▐███─█──█─
    ──█▒▒▒▒▒█────▐▌─█─█▀▀█─
    ───█████─────▐▌─█─█──█─
    Волна - это музыкальный
    проигрыватель с функци-
    оналом торрента. 
    Это инструкция по этой 
    терминальной программе.

    1) Вводить нужно опции 
    нужно чётко, как напи-
    сано 

    2) постройте папки сле-
    дующим образом:

    |волна
        |music
            ETC*
            {ваши альбомы}
            {ваши песни}

    * ETC всегда
    должен стоят на 1ом 
    месте, альбомы и песни
    могут быть вразброс

    3) Используем обычные 
    формаиты: .mp3, .FLAC,
    .wav, и.т.д

    4) Картинки песен дол-
    жды быть, как название.
    Картинки ставьте в пап-
    ку "ETC":

    *если в название песни
    имеются точки, уберите 
    их

    пр файл: звезда.jpg

    пр* : вол.на => волна

    5) Картинки альбомов
    должны быть в папке
    альбома и назваться
    "art.jpg"

    пр: /music/чёрный аль-
    бом/art.jpg

    6) Чтобы вернутся из лю-
    бого откуда-либов меню
    напишите "вернуться" или
    "<="

    """)
    if r("я прочитал(да/нет) ") == "да":
        menu()
else:
    exit()
