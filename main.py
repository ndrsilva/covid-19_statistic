from tkinter import *
from tkinter import ttk

#######/ importando lib's /#########
from PIL import Image
import requests
import string
import json
import datetime

####################/ cores /#####################
cor_00 = '#000000'  # black
cor_01 = '#cc1d4e'  # red
cor_02 = '#feffff'  # white
cor_03 = '#0074eb'  # blue
cor_04 = '#435e5a'  #
cor_05 = '#59b356'  # green
cor_06 = '#d9d9d9'  # grey

####################/ cirar a janela principal do aplicativo /#####################
janela = Tk()
janela.resizable(width=False, height=False)
janela.geometry('890x360')
janela.title('')
janela.configure(bg=cor_06)

####################/ criando frames /#####################
app_nome_frame = Frame(janela, width=840, height=50, bg=cor_02, relief="flat")
app_nome_frame.grid(row=0, column=0, columnspan=3, sticky=NSEW)

mostrar_frame_infectados = Frame(janela, width=220, height=100, bg=cor_02, relief="flat")
mostrar_frame_infectados.grid(row=1, column=0, sticky=NW, pady=5, padx=10)

mostrar_frame_recuperados = Frame(janela, width=220, height=100, bg=cor_02, relief="flat")
mostrar_frame_recuperados.grid(row=1, column=1, sticky=NW, pady=5, padx=0)

mostrar_frame_mortes = Frame(janela, width=220, height=100, bg=cor_02, relief="flat")
mostrar_frame_mortes.grid(row=1, column=2, sticky=NW, pady=5, padx=0)

selecione_frame = Frame(janela, width=840, height=50, bg=cor_06, relief="flat")
selecione_frame.grid(row=2, column=0, columnspan=3, sticky=N, pady=10)

####################/ cirando labels para app_nome_frame /#####################
img = Image.open("covid-019.jpeg")
img = img.resize((80, 50))
img = img.save("covid-19.png")
imagem = PhotoImage(file="covid-19.png")


app_imagem = Label(app_nome_frame, image=imagem, width=350,
                   anchor=NE, pady=20, relief="flat", bg=cor_02)
app_imagem.grid(row=0, column=0, pady=5)

app_nome = Label(app_nome_frame, text=f"COVID-19 / Global", width=27, height=1, pady=20, relief="flat",
                 anchor=NW, font="Helvetica 25 bold", bg=cor_02, fg=cor_00)
app_nome.grid(row=0, column=1, pady=5)



####################/ chamando a API /#####################
response = requests.get('https://covid19.mathdro.id/api')
info = response
info = json.loads(info.text)

infectados = info["confirmed"]["value"]
recuperados = info["recovered"]["value"]
mortes = info["deaths"]["value"]
dia = info["lastUpdate"]
dia = datetime.datetime.strptime(dia, "%Y-%m-%dT%H:%M:%S.000Z")
dia = dia.strftime("%c")


####################/ criando labels para mostrar_frame_infectados /#####################
label_infectados = Label(mostrar_frame_infectados, text="Infectados", width=20, height=1, pady=7,
                         padx=0, relief="flat", anchor=NW, font="Courier 15 bold", bg=cor_02, fg=cor_00)
label_infectados.grid(row=0, column=0, pady=1, padx=13)

mostrar_infectados = Label(mostrar_frame_infectados, text=infectados, width=12, height=1, pady=7,
                           padx=0, relief="flat", anchor=NW, font="Courier 25 bold", bg=cor_02, fg=cor_00)
mostrar_infectados.grid(row=1, column=0, pady=1)

mostrar_info_data = Label(mostrar_frame_infectados, text=dia, width=25, height=1, pady=7,
                          padx=0, relief="flat", anchor=NW, font="Courier 11 bold", bg=cor_02, fg=cor_00)
mostrar_info_data.grid(row=2, column=0, pady=1)

mostrar_info_casos_ativos = Label(mostrar_frame_infectados, text="Total de casos ativos de Covid-19", width=35,
                                  height=1, pady=7,
                                  padx=7, relief="flat", anchor=NW, font="Courier 8 bold", bg=cor_02, fg=cor_00)
mostrar_info_casos_ativos.grid(row=3, column=0, pady=1)

rodape_azul = Label(mostrar_frame_infectados, text="", width=19, height=1, pady=1,
                    padx=1, relief="flat", anchor=NW, font="Courier 1 bold", bg=cor_03, fg=cor_00)
rodape_azul.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

####################/ criando labels para mostrar_frame_recuperados /#####################
label_recuperados = Label(mostrar_frame_recuperados, text="Recuperados", width=20, height=1, pady=7,
                          padx=0, relief="flat", anchor=NW, font="Courier 15 bold", bg=cor_02, fg=cor_00)
label_recuperados.grid(row=0, column=0, pady=1, padx=13)

mostrar_recuperados = Label(mostrar_frame_recuperados, text=recuperados, width=12, height=1, pady=7,
                            padx=0, relief="flat", anchor=NW, font="Courier 25 bold", bg=cor_02, fg=cor_00)
mostrar_recuperados.grid(row=1, column=0, pady=1)

mostrar_info_data = Label(mostrar_frame_recuperados, text=dia, width=25, height=1, pady=7,
                          padx=0, relief="flat", anchor=NW, font="Courier 11 bold", bg=cor_02, fg=cor_00)
mostrar_info_data.grid(row=2, column=0, pady=1)

mostrar_info_casos_ativos = Label(mostrar_frame_recuperados, text="Total de casos recup. de Covid-19", width=35,
                                  height=1, pady=7,
                                  padx=7, relief="flat", anchor=NW, font="Courier 8 bold", bg=cor_02, fg=cor_00)
mostrar_info_casos_ativos.grid(row=3, column=0, pady=1)

rodape_verde = Label(mostrar_frame_recuperados, text="", width=19, height=1, pady=1,
                     padx=1, relief="flat", anchor=NW, font="Courier 1 bold", bg=cor_05, fg=cor_00)
rodape_verde.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

####################/ criando labels para mostrar_frame_mortes /#####################
label_mortes = Label(mostrar_frame_mortes, text="Mortes", width=20, height=1, pady=7,
                     padx=0, relief="flat", anchor=NW, font="Courier 15 bold", bg=cor_02, fg=cor_00)
label_mortes.grid(row=0, column=0, pady=1, padx=13)

mostrar_mortes = Label(mostrar_frame_mortes, text=mortes, width=12, height=1, pady=7,
                       padx=0, relief="flat", anchor=NW, font="Courier 25 bold", bg=cor_02, fg=cor_00)
mostrar_mortes.grid(row=1, column=0, pady=1)

mostrar_info_data = Label(mostrar_frame_mortes, text=dia, width=25, height=1, pady=7,
                          padx=0, relief="flat", anchor=NW, font="Courier 11 bold", bg=cor_02, fg=cor_00)
mostrar_info_data.grid(row=2, column=0, pady=1)

mostrar_info_casos_ativos = Label(mostrar_frame_mortes, text="Total de casos de mortes de Covid-19", width=35, height=1,
                                  pady=7,
                                  padx=7, relief="flat", anchor=NW, font="Courier 8 bold", bg=cor_02, fg=cor_00)
mostrar_info_casos_ativos.grid(row=3, column=0, pady=1)

rodape_vermelho = Label(mostrar_frame_mortes, text="", width=19, height=1, pady=1,
                        padx=1, relief="flat", anchor=NW, font="Courier 1 bold", bg=cor_01, fg=cor_00)
rodape_vermelho.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

####################/ criando caixa de seleção /#####################
label_pais = Label(selecione_frame, text="Selecione o país", width=13, height=1, pady=7, padx=0,
                   relief="flat", anchor=NW, font="Ivy 12 bold", bg=cor_06, fg=cor_00)
label_pais.grid(row=0, column=0, pady=1, padx=13)

pais = ["Global", "Angola", "Brazil", "India", "Portugal", "USA", "France", "Spain"]

combo = ttk.Combobox(selecione_frame, width=15, font="Ivy 8 bold")
combo["values"] = pais
combo.grid(row=0, column=1, pady=13, padx=13)

####################/ selecionando país na API /#####################


def pais_selecionado(eventObject):

    if combo.get() == "Global":
        response = requests.get('https://covid19.mathdro.id/api')
        info = response
        info = json.loads(info.text)

        infectados = info["confirmed"]["value"]
        recuperados = info["recovered"]["value"]
        mortes = info["deaths"]["value"]
        dia = info["lastUpdate"]
        dia = datetime.datetime.strptime(dia, "%Y-%m-%dT%H:%M:%S.000Z")
        dia = dia.strftime("%c")

        mostrar_infectados.configure(text=infectados)
        mostrar_recuperados.configure(text=recuperados)
        mostrar_mortes.configure(text=mortes)
        mostrar_info_data.configure(text=dia)
        app_nome.configure(text=f"COVID-19 / Global")

    else:

        select_pais = combo.get()
        response = requests.get(f'https://covid19.mathdro.id/api/countries/{select_pais}')
        info = response
        info = json.loads(info.text)

        infectados = info["confirmed"]["value"]
        recuperados = info["recovered"]["value"]
        mortes = info["deaths"]["value"]
        dia = info["lastUpdate"]
        dia = datetime.datetime.strptime(dia, "%Y-%m-%dT%H:%M:%S.000Z")
        dia = dia.strftime("%c")

        mostrar_infectados.configure(text=infectados)
        mostrar_recuperados.configure(text=recuperados)
        mostrar_mortes.configure(text=mortes)
        mostrar_info_data.configure(text=dia)
        app_nome.configure(text=f"COVID-19 / {select_pais}")


combo.bind("<<ComboboxSelected>>", pais_selecionado)


janela.mainloop()
