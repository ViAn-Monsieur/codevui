import tkinter as tk
from tkinter import Button, Label
import random
import time
import threading
import sys

def print_lyrics():
    lyrics = [
        ("Yêu thương sao cho vừa?", 0.05),
        ("Hay anh đang lo thừa?", 0.05),
        ("Cho anh mong như cơm bữa", 0.05),
        ("Em đừng xinh như thế nữa", 0.05),
        ("Loạn nhịp  cả tim lên rồi", 0.05),
        ("Đầu này toàn là em mà thôi", 0.05),
        ("Yeah-eh, ee-yeah-eh, ee-yeah", 0.05),
        ("Nỗi nhớ em cầu kỳ nên chẳng biết lý do là gì", 0.08),
        ("Hao tốn hơi nhiều GB nên cần dùng thêm USB", 0.05),
        ("Nỗi nhớ em cầu kỳ nên chẳng biết lý do là gì", 0.05),
        ("Hao tốn hơi nhiều GB nên cần D-O-M-I-C", 0.05)
    ]
    delay=[1.0, 1.0, 0.88, 0.5, 0.08, 0.08, 0.8, 1.0, 1.5, 1.0, 2.3]
    for i, (line, char_speed) in enumerate(lyrics):
        for Char in line:
            print(Char, end='')
            sys.stdout.flush()
            time.sleep(char_speed)
        time.sleep(delay[i])
        print('')

def print_ending():
    lyrics = [
        ("Tràn ngập bộ nhớ, nhớ, nhớ, nhớ em", 0.06),
        ("Cho anh cảm giác không sao quên được", 0.08),
        ("Tràn ngập bộ nhớ, nhớ, nhớ, nhớ em", 0.08),
        ("Nhưng anh mong có cảm giác này mãi", 0.08)
    ]
    delay=[1.5, 1.2, 1.0, 1.5]
    for i, (line, char_speed) in enumerate(lyrics):
        for Char in line:
            print(Char, end='')
            sys.stdout.flush()
            time.sleep(char_speed)
        print()
        time.sleep(delay[i])

messages = [
    ("I miss you!", ("Comic Sans MS", 18, "bold")),
    ("May khoi!", ("Comic Sans MS", 18, "bold")),
    ("Nho cai lon!", ("Comic Sans MS", 18, "bold"))
]

color = ["white"]

def create_windows(screen_width, screen_height):
    window = tk.Tk()
    window.geometry(f'250x70+{random.randint(0, screen_width-300)}+{random.randint(0, screen_height-200)}')
    window.title("Thông báo")

    message, font = random.choice(messages)
    fg_color = random.choice(color)
    label = tk.Label(window, text= message, font=font, fg=fg_color, bg="#F8C8F0")
    label.pack(expand=True, fill="both")
    window.after(3000, window.destroy)
    window.mainloop()

def create_multiple_window(num):
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    
    for _ in range(num):
        t = threading.Thread(target=create_windows, args=(screen_width, screen_height))
        t.start()
        time.sleep(0.04)

if __name__=="__main__":
    # root = tk.Tk()
    # root.geometry('300x300')
    # button = Button(root, text='Nhấp vào đi', command=root.destroy)
    # label = Label(root, text='Hello ngay tot lanh')
    # button.pack(pady=10)
    # root.mainloop()
    print_lyrics()
    k = threading.Thread(target=print_ending)
    k.start()
    create_multiple_window(150)
