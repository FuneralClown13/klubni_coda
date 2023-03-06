from tkinter import *
from tkinter import ttk
from main import main

count = 1


def clicked():
    global count
    if count <= 0:
        count = 1
    text = main(count)
    lbl_advice['text'] = text


def count_l():
    global count
    count -= 1

    if count == 1:
        btn_advice['text'] = f'Мне нужен {count} совет...'
        btn_r['state'] = 'active'
        btn_l['state'] = 'disabled'
    elif count > 1:
        btn_advice['text'] = f'Мне нужно {count} совета...'
        btn_r['state'] = 'active'



def count_r():
    global count
    count += 1

    if 5 > count > 1:
        btn_advice['text'] = f'Мне нужно {count} совета...'
        btn_r['state'] = 'active'
        btn_l['state'] = 'active'
    elif count == 5:
        btn_advice['text'] = f'Мне нужно {count} советов...'
        btn_r['state'] = 'disabled'


root = Tk()
btn_l = ttk.Button(root, text='←', command=count_l, state='disabled')
btn_l.grid(row=1, column=1, pady=5)
btn_r = ttk.Button(root, text='→', command=count_r, state='active')
btn_r.grid(row=1, column=3, pady=5)
btn_advice = Button(root, text='Мне нужен 1 совет...', command=clicked, state='active')
btn_advice.grid(row=1, column=2, pady=5)

lbl_advice = Label(root, text='', wraplength=350)
lbl_advice.grid(row=3, column=1, columnspan=3)
if __name__ == '__main__':
    [root.columnconfigure(index=c, weight=1) for c in range(3)]
    # wise advice
    root.title('WISE ADVICE')
    root.geometry('350x450')
    root.mainloop()
