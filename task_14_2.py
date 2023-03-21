from tkinter import *
import random
import time

print('''
#2. Экран «Конец игры»
Сейчас по окончании игры экран застывает. Пользователю будет гораздо 
удобнее, если при касании мячиком нижнего края холста на экране появится 
сообщение «Конец игры». В этом вам поможет функция create_
text. Стоит обратить внимание и на функцию itemconfig с аргументом state, 
в котором можно передавать такие значения, как normal
и hidden (см. раздел «Для чего еще нужен идентификатор» на стр. 186). 
В качестве дополнительного задания попробуйте выдержать перед показом 
сообщения небольшую паузу
''')

my_width = 500
my_height = 400
oval_size = (10, 10, 25, 25)


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.canvas.bind_all('<Button-1>', self.lets_play)
        self.id = canvas.create_oval(oval_size[0], oval_size[1], oval_size[2], oval_size[3], fill=color)
        self.canvas.move(self.id, my_width / 2, my_height / 6)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        random.shuffle(starts)
        self.y = starts[0]
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.play = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def lets_play(self, evt):
        self.play = True

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, my_width / 3, my_height - 15)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2


tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=my_width, height=my_height, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')

while 1:
    if ball.hit_bottom == False:
        paddle.draw()
        if ball.play == True:
            ball.draw()
    else:
        canvas.itemconfig(ball.id, state='hidden')
        time.sleep(0.5)
        ball.canvas.create_text(my_width / 2, my_height / 2, text='Game Over')
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)