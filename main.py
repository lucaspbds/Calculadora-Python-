from tkinter import *


widthButton = 5
heightButton = 2
bgBtNum = '#243757'
fgBtNum = 'white'
bgBtFuncao = '#3a5f6f'
fgBtFuncao = '#951f2b'
font = 'Arial 15 bold'


def exibir(event):
    global operacao
    operacao = operacao + event
    valorTexto.set(operacao)


def calcular():
    global operacao
    resultado = eval(operacao)
    valorTexto.set(resultado)


def limparVisor():
    global operacao
    operacao = ''
    valorTexto.set('0')


calculadora = Tk()
calculadora.title("Calculadora")
calculadora.geometry('286x470')

valorTexto = StringVar()
operacao = ''
valorTexto.set('0')

frame_visor = Frame(calculadora,
                    width=286,
                    height=100,
                    background='#171430')
frame_visor.grid(column=0, row=0)
frame_teclas = Frame(calculadora,
                     width=286,
                     height=500,
                     background='#171430')
frame_teclas.grid(column=0, row=1)

visor = Label(frame_visor,
              textvariable=valorTexto,
              font='Arial 17',
              background="#171430",
              foreground="white",
              width=21,
              height=5,
              anchor='se',
              bd=0,
              padx=7,
              relief=FLAT)
visor.grid(column=0, row=0)

limpar = Button(frame_teclas,
                font=font,
                text='C',
                bd=0,
                background=bgBtFuncao,
                foreground=fgBtFuncao,
                width=11,
                height=heightButton,
                relief=RAISED,
                overrelief=RIDGE,
                activebackground='#4d7e94',
                activeforeground=fgBtFuncao,
                command=limparVisor)
limpar.place(x=0, y=0)
divisao = Button(frame_teclas,
                 font=font,
                 text='/',
                 bd=0,
                 background=bgBtFuncao,
                 foreground=fgBtFuncao,
                 width=widthButton,
                 height=heightButton,
                 relief=RAISED,
                 overrelief=RIDGE,
                 activebackground='#4d7e94',
                 activeforeground=fgBtFuncao,
                 command=lambda: exibir('/'))
divisao.place(x=144, y=0)
mult = Button(frame_teclas,
              font=font,
              text='X',
              bd=0,
              background=bgBtFuncao,
              foreground=fgBtFuncao,
              width=widthButton,
              height=heightButton,
              relief=RAISED,
              overrelief=RIDGE,
              activebackground='#4d7e94',
              activeforeground=fgBtFuncao,
              command=lambda: exibir('*'))
mult.place(x=216, y=0)
sub = Button(frame_teclas,
             font=font,
             text='-',
             bd=0,
             background=bgBtFuncao,
             foreground=fgBtFuncao,
             width=widthButton,
             height=heightButton,
             relief=RAISED,
             overrelief=RIDGE,
             activebackground='#4d7e94',
             activeforeground=fgBtFuncao,
             command=lambda: exibir('-'))
sub.place(x=216, y=68)
adicao = Button(frame_teclas,
                font=font,
                text='+',
                bd=0,
                background=bgBtFuncao,
                foreground=fgBtFuncao,
                width=widthButton,
                height=heightButton,
                relief=RAISED,
                overrelief=RIDGE,
                activebackground='#4d7e94',
                activeforeground=fgBtFuncao,
                command=lambda: exibir('+'))
adicao.place(x=216, y=136)
resultado = Button(frame_teclas,
                   font='Arial 15 bold',
                   text='=',
                   bd=0,
                   background='#d4112d',
                   foreground='white',
                   width=widthButton,
                   height=5,
                   relief=RAISED,
                   overrelief=RIDGE,
                   activebackground='#de1d3d',
                   activeforeground="white",
                   command=lambda: calcular())
resultado.place(x=216, y=204)

bt_7 = Button(frame_teclas,
              font=font,
              text='7',
              bd=0,
              background=bgBtNum,
              foreground=fgBtNum,
              width=widthButton,
              height=heightButton,
              relief=RAISED,
              overrelief=RIDGE,
              activebackground='#344c75',
              activeforeground='white',
              command=lambda: exibir('7'))
bt_7.place(x=0, y=68)
bt_8 = Button(frame_teclas,
              font=font,
              text='8',
              bd=0,
              background=bgBtNum,
              foreground=fgBtNum,
              width=widthButton,
              height=heightButton,
              relief=RAISED,
              overrelief=RIDGE,
              activebackground='#344c75',
              activeforeground='white',
              command=lambda: exibir('8'))
bt_8.place(x=72, y=68)
bt_9 = Button(frame_teclas,
              font=font,
              text='9',
              bd=0,
              background=bgBtNum,
              foreground=fgBtNum,
              width=widthButton,
              height=heightButton,
              relief=RAISED,
              overrelief=RIDGE,
              activebackground='#344c75',
              activeforeground='white',
              command=lambda: exibir('9'))
bt_9.place(x=144, y=68)
bt_4 = Button(frame_teclas,
              font=font,
              text='4',
              bd=0,
              background=bgBtNum,
              foreground=fgBtNum,
              width=widthButton,
              height=heightButton,
              relief=RAISED,
              overrelief=RIDGE,
              activebackground='#344c75',
              activeforeground='white',
              command=lambda: exibir('4'))
bt_4.place(x=0, y=136)
bt_5 = Button(frame_teclas,
              font=font,
              text='5',
              bd=0,
              background=bgBtNum,
              foreground=fgBtNum,
              width=widthButton,
              height=heightButton,
              relief=RAISED,
              overrelief=RIDGE,
              activebackground='#344c75',
              activeforeground='white',
              command=lambda: exibir('5'))
bt_5.place(x=72, y=136)
bt_6 = Button(frame_teclas,
              font=font,
              text='6',
              bd=0,
              background=bgBtNum,
              foreground=fgBtNum,
              width=widthButton,
              height=heightButton,
              relief=RAISED,
              overrelief=RIDGE,
              activebackground='#344c75',
              activeforeground='white',
              command=lambda: exibir('6'))
bt_6.place(x=144, y=136)
bt_1 = Button(frame_teclas,
              font=font,
              text='1',
              bd=0,
              background=bgBtNum,
              foreground=fgBtNum,
              width=widthButton,
              height=heightButton,
              relief=RAISED,
              overrelief=RIDGE,
              activebackground='#344c75',
              activeforeground='white',
              command=lambda: exibir('1'))
bt_1.place(x=0, y=204)
bt_2 = Button(frame_teclas,
              font=font,
              text='2',
              bd=0,
              background=bgBtNum,
              foreground=fgBtNum,
              width=widthButton,
              height=heightButton,
              relief=RAISED,
              overrelief=RIDGE,
              activebackground='#344c75',
              activeforeground='white',
              command=lambda: exibir('2'))
bt_2.place(x=72, y=204)
bt_3 = Button(frame_teclas,
              font=font,
              text='3',
              bd=0,
              background=bgBtNum,
              foreground=fgBtNum,
              width=widthButton,
              height=heightButton,
              relief=RAISED,
              overrelief=RIDGE,
              activebackground='#344c75',
              activeforeground='white',
              command=lambda: exibir('3'))
bt_3.place(x=144, y=204)
bt_0 = Button(frame_teclas,
              font=font,
              text='0',
              bd=0,
              background=bgBtNum,
              foreground=fgBtNum,
              width=11,
              height=heightButton,
              relief=RAISED,
              overrelief=RIDGE,
              activebackground='#344c75',
              activeforeground='white',
              command=lambda: exibir('0'))
bt_0.place(x=0, y=272)
bt_ponto = Button(frame_teclas,
                  font=font,
                  text='.',
                  bd=0,
                  background=bgBtNum,
                  foreground=fgBtNum,
                  width=widthButton,
                  height=heightButton,
                  relief=RAISED,
                  overrelief=RIDGE,
                  activebackground='#344c75',
                  activeforeground='white',
                  command=lambda: exibir('.'))
bt_ponto.place(x=144, y=272)

calculadora.mainloop()
