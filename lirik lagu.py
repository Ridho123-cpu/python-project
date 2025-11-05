import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(Lyric, delay, speed):
    time.sleep(delay)
    animate_text(Lyric, speed)

def sing_song():
    lyrics = [
        ("\nI think I've seen this film before", 0.09),
        ("And I didn't like the ending", 0.08),
        ("I'm not your problem anymore", 0.09),
        ("So who am I offending now", 0.07),
        ("You were my crown", 0.08),
        ("Now I'm exile seeing you out", 0.09),
        ("I think I've seen this film before", 0.08),
        ("So I'm leaving out the side door", 0.08),
    ]

    delays = [0.3, 4.7, 7.1, 11.7, 13.8, 14.7, 20.4, 24.0]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()