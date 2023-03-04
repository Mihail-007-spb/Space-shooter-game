"""Space shooter game.
The image and sound files are located in the repository by
name 'Image-and-sound-for-the-published-repositories'"""


"""Игра шутер: Космос.
Файлы изображения и звука находятся в repository по имени
 'Image-and-sound-for-the-published-repositories'"""


from tkinter import *
import random
import time
from PIL import ImageTk, Image
import winsound
import threading
from multiprocessing import Process
import time

def exzit_igra(event):
    paddle.started = False
    musika_exzit_p()
    print('Выход')
    tk.destroy()
    time.sleep(1)
    ball.hit_bottom = True


def prof_igra(event):
    global paddle, ball, c_iz, v_ball, v
    c_iz = 0
    list = [2.5, 3, 3.8]
    v = list[2]
    musika_new_m()
    canvas.delete('padle')
    canvas.delete('ball')
    create_paddle()
    create_ball()

    while not ball.hit_bottom:
        if paddle.started == True:
            canvas.itemconfig('level', state='hidden')
            canvas.itemconfig(pause_mon, state='normal')
            ball.draw()
            paddle.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
    else:
        canvas.itemconfig('level', state='normal')


def sred_igra(event):
    global paddle, ball, c_iz, v_ball, v
    c_iz = 0
    list = [2.5, 3, 3.5]
    v = list[1]
    musika_new_m()
    canvas.delete('padle')
    canvas.delete('ball')
    create_paddle()
    create_ball()

    while not ball.hit_bottom:
        if paddle.started == True:
            canvas.itemconfig('level', state='hidden')
            canvas.itemconfig(pause_mon, state='normal')
            ball.draw()
            paddle.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
    else:
        canvas.itemconfig('level', state='normal')


def legk_igra(event):
    global paddle, ball, c_iz, v_ball, v
    c_iz = 0
    list = [2.5, 3, 3.5]
    v = list[0]
    musika_new_m()
    canvas.delete('padle')
    canvas.delete('ball')
    create_paddle()
    create_ball()

    while not ball.hit_bottom:
        if paddle.started == True:
            canvas.itemconfig('level', state='hidden')
            canvas.itemconfig(pause_mon, state='normal')
            ball.draw()
            paddle.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
    else:
        canvas.itemconfig('level', state='normal')


def create_ball():
    global ball
    ball = Ball(canvas, paddle, score, 'red')


def create_paddle():
    global paddle
    paddle = Paddle(canvas, 'yellow', state='normal')
    paddle.started = True


def pause_igra(event):
    paddle.started = False
    canvas.itemconfig(pause_mon, state='hidden')
    canvas.itemconfig(pause, state='normal')
    print('Пауза')


def start_igra(event):
    paddle.started = True
    canvas.itemconfig(pause, state='hidden')


def musika_go_padle_m():
    p1 = Process(target=musika_go_padle)
    p1.daemon = True
    p1.start()


def musika_exzit_p():
    thr_p = threading.Thread(target=musika_exzit).start()


def musika_end_p():
    thr_e = threading.Thread(target=musika_end).start()


def musika_new_m():
    p = Process(target=musika_new)
    p.daemon = True
    p.start()


def musika_strelba_m():
    p = Process(target=musika_strelba)
    p.daemon = True
    p.start()


def musika_popadanie_m():
    w = Process(target=musika_popadanie)
    w.daemon = True
    w.start()


def musika_strelba():
    winsound.PlaySound(r"C:\FOTO  Python\zvuk-vistrela.wav",
                       winsound.SND_FILENAME)


def musika_popadanie():
    winsound.PlaySound(r"C:\\FOTO  Python\\vzriv-2.wav",
                       winsound.SND_FILENAME)


def musika_end():
    winsound.PlaySound(r"C:\\FOTO  Python\\razbivanie-stekla.wav",
                       winsound.SND_FILENAME)


def musika_new():
    winsound.PlaySound(r"C:\\FOTO  Python\\nachalo game.wav",
                       winsound.SND_FILENAME)


def musika_exzit():
    winsound.PlaySound(r"C:\\FOTO  Python\\exzit of game-01.wav",
                       winsound.SND_FILENAME)


def musika_go_padle():
    winsound.PlaySound(r"C:\\FOTO  Python\\go of padle-2.wav",
                       winsound.SND_FILENAME)


def new_game_00(event):
    canvas.itemconfig('level', state='normal')


z = 0


class Ball:
    global paddle, score, ball

    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10, 10, 70, 70, fill=color,
                                          width=3, tag="ball" )
        start_2 = [30, 200, 400, 600, 700]
        random.shuffle(start_2)
        self.starting_point_x_ball = start_2[0]
        self.canvas.move(self.id, self.starting_point_x_ball, 50)
        global v_ball
        v_ball = self.y = 2
        # шарик узнаёт свою высоту и ширину
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        # свойство, которое отвечает за то, достиг шарик дна или нет.
        # Пока не достиг, значение будет False
        self.hit_bottom = False
    # обрабатываем касание платформы, для этого получаем 4 координаты шарика
    # в переменной pos (левая верхняя и правая нижняя точки)
    global t, a, a1, z
    t = time.localtime()
    a = time.time()
    a1 = int(a)

    """ДВИЖЕНИЕ ПЛАТФОРМЫ"""
    def hit_paddle(self, pos):
        global z, c_iz, a1, b1, f
        b = time.time()
        b1 = int(b)
        c_iz = (b1 - a1)
        # получаем кординаты платформы через объект paddle (платформа)
        paddle_pos = self.canvas.coords(self.paddle.id)
        # если координаты касания совпадают с координатами платформы
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] and \
                pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                z = z + 1
                musika_popadanie_m()
                print('Это время=' + str(c_iz))
                print('Это z=' + str(z))
                canvas.delete('padle')
                canvas.delete('ball')
                create_paddle()
                create_ball()
                canvas.delete("score")
                canvas.create_text(80, 30, text="Счет: {}".format(z),
                                   font="Times 20",
                                   fill="white", tag="score")
                # возвращаем метку о том, что мы успешно коснулись
                return True


        return False

    """ДВИЖЕНИЕ ШАРИКА"""
    def draw(self):
        global z, v_ball, v, list
        # передвигаем шарик на заданный вектор x и y
        self.canvas.move(self.id, 0, v_ball)
        # запоминаем новые координаты шарика
        pos = self.canvas.coords(self.id)
        # если шарик падает сверху
        list = [2.5, 3, 3.5]

        """КАСАНИЕ ШАРИКОМ НИЗА"""
        if pos[3] >= 670:
            paddle.started = False
            musika_end_p()
            canvas.delete("score")
            z = 0
            canvas.itemconfig('level', state='normal')

        #"""ПОПАДАНИЕ В ЦЕЛЬ"""
        elif self.hit_paddle(pos) == True:
            print('касание')
            v_ball = v
            #self.y = 2
            print("Ускорение шарика =", v_ball)


class Paddle:
    # конструктор
    def __init__(self, canvas, color, state):
        self.state = state
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 30, 40, fill=color, width=2,
                                          tag="padle")
        # задаём список возможных стартовых положений платформы
        start_1 = [330, 300, 350]
        # перемешиваем их
        random.shuffle(start_1)
        # выбираем первое из перемешанных
        self.starting_point_x = start_1[0]
        # перемещаем платформу в стартовое положение
        self.canvas.move(self.id, self.starting_point_x, 560)
        # пока платформа никуда не движется, поэтому изменений по оси х нет
        self.x = 0
        self.y = 0
        # платформа узнаёт свою ширину
        self.canvas_width = self.canvas.winfo_width()
        #self.canvas_height = self.canvas.winfo_height()
        # задаём обработчик нажатий
        # если нажата стрелка вправо — выполняется метод turn_right()
        self.canvas.bind('<KeyPress-Right>', self.turn_right)
        # если стрелка влево — turn_left()
        self.canvas.bind('<KeyPress-Left>', self.turn_left)
        self.canvas.bind('<w>', self.turn_up)
        # пока платформа не двигается, поэтому ждём
        self.started = False
        # как только игрок нажмёт Enter — всё стартует
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)

    # движемся вправо
    def turn_right(self, event):
        # будем смещаться правее на 2 пикселя по оси х
        self.x = 4
        musika_go_padle_m()


    # движемся влево
    def turn_left(self, event):
        # будем смещаться левее на 2 пикселя по оси х
        self.x = -4
        musika_go_padle_m()

    """ВЫСТРЕЛ"""
    def turn_up(self, event):
        musika_strelba_m()
        self.y = -20
        self.x = 0

    # игра начинается
    def start_game(self, event):
        # меняем значение переменной, которая отвечает
        # за старт движения платформы
        self.started = True

    # метод, который отвечает за движение платформы
    def draw(self):
        # сдвигаем нашу платформу на заданное количество пикселей
        self.canvas.move(self.id, self.x, self.y)
        # получаем координаты холста
        pos = self.canvas.coords(self.id)
        # если мы упёрлись в левую границу
        if pos[0] <= 0:
            # останавливаемся
            self.x = 0
        # если упёрлись в правую границу
        elif pos[2] >= self.canvas_width:
            # останавливаемся
            self.x = 0

        #"""ВОЗВРАТ СНАРЯДА"""
        elif pos[3] >= 590:
            self.y = 0

        #отскок снаряда сверху
        elif pos[3] <= 0:
            self.y = 300


#  Описываем класс Score, который отвечает за отображение счетов
class Score:
    global score  # конструктор

    def __init__(self, canvas, color):
        # в самом начале счёт равен нулю
        self.score = 0
        # будем использовать наш холст
        self.canvas = canvas
        # создаём надпись, которая показывает текущий счёт,
        # делаем его нужно цвета и запоминаем внутреннее имя этой надписи
        self.id = canvas.create_text(750, 25, text=self.score,
                                     font=('Times', 30), fill=color,
                                     stat='hidden')

    # обрабатываем касание платформы
    def hit(self):
        # увеличиваем счёт на единицу
        self.score += 1
        # пишем новое значение счёта
        self.canvas.itemconfig(self.id, text=self.score)

if __name__ == '__main__':
    tk = Tk()
    tk.geometry('+400+50')
    s = ' '
    # делаем заголовок окна — Games с помощью свойства объекта title
    tk.title(s * 80 + '''ИГРА "КОСМИЧЕСКИЙ ШУТЕР"''')
    tk.iconbitmap(default=r"C:\\FOTO  Python\\predator26.ico")
# запрещаем менять размеры окна, для этого используем свойство resizable
    tk.resizable(0, 0)
# чтобы другие окна не могли его заслонить
    tk.wm_attributes('-topmost', 1)
    canvas = Canvas(tk, width=800, height=600, highlightthickness=0, bg="#252c58")
    canvas.grid()

    foto1 = ImageTk.PhotoImage(file=r"C:\\FOTO  Python\\planeta-kosmos.jpg")
    canvas.create_image(0, 0, image=foto1, anchor=NW)

    canvas.grid()
    canvas.focus_set()
    tk.update()

    start1 = canvas.create_text(400, 100,
                      text = ''' Выберите сложность игры:
                       
                 Легкий ''',
                               font='Times 20', fill='white',
                                state='normal', tag="level")

    start2 = canvas.create_text(400, 200,
                               text='''Средний ''',
                               font='Times 20', fill='white',
                                state='normal', tag="level")

    start3 = canvas.create_text(400, 270,
                               text=''' Продвинутый''',
                               font='Times 20', fill='white',
                                state='normal', tag="level")

    upravl = canvas.create_text(400, 400,
                                text='''        КЛАВИШИ УПРАВЛЕНИЯ:
        <w> (англ. раскладка) - огонь
        <-- движение влево
        --> движение вправо''',
                                font='Times 20', fill='white',
                                state='normal', tag="level")

    exzit = canvas.create_text(400, 500,
                                text=''' Выход''',
                                font='Times 40', fill='red',
                                state='normal', tag="level")

    pause_mon = canvas.create_text(400, 20,
                      text = "Для ПАУЗЫ нажмите ПРОБЕЛ",
                               font='Times 12', fill='white', state='hidden')
    st = ' '
    pause = canvas.create_text(400, 300,
                      text = st*8+"ПАУЗА!!!\n для продолжения\n"
                                  " нажмите клавишу <q>\n"
                                  "(английская раскладка)",
                               font='Times 30', fill='white', state='hidden')

    canvas.bind('<space>', pause_igra)
    canvas.bind('<q>', start_igra)

    canvas.tag_bind(start1, '<1>', legk_igra)
    canvas.tag_bind(start2, '<1>', sred_igra)
    canvas.tag_bind(start3, '<1>', prof_igra)
    canvas.tag_bind(exzit, '<1>', exzit_igra)

    score = Score(canvas, '#c9c9c9')
    paddle = Paddle(canvas, 'yellow', state='normal')
    ball = Ball(canvas, paddle, score, 'red')

    list = [2.5, 3, 3.5]
    v = list[0]

    while not ball.hit_bottom:
        if paddle.started == True:
            canvas.itemconfig(pause_mon, state='normal')
            ball.draw()
            paddle.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
    else:
        canvas.itemconfig('level', state='normal')