import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import Mate

from tkinter import *
from tkinter.tix import *
from LinearCongruential import LinearCongruential
from MixedCongruential import MixedCongruential
from MiddleSquares import MiddleSquares
from MultiplicativeCongruential import MultiplicativeCongruential
#from MCLC import MCLC

"""
Useful Links:
https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter Most useful in my opinion
https://www.tutorialspoint.com/python/python_gui_programming.htm
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
https://www.youtube.com/watch?v=HjNHATw6XgY&list=PLQVvvaa0QuDclKx-QpC9wntnURXVJqLyk
"""

# You can also use a pandas dataframe for pokemon_info.
# you can convert the dataframe using df.to_numpy.tolist()
pokemon_info = [['Bulbasaur', 'Grass', '318'], ['Ivysaur', 'Grass', '405'], ['Venusaur', 'Grass', '525'], ['Charmander', 'Fire', '309'], ['Charmeleon', 'Fire', '405'], ['Charizard', 'Fire', '534'], ['Squirtle', 'Water', '314'], ['Wartortle', 'Water', '405'], ['Blastoise', 'Water', '530'], ['Caterpie', 'Bug', '195'], ['Metapod', 'Bug', '205'], ['Butterfree', 'Bug', '395'], ['Weedle', 'Bug', '195'], ['Kakuna', 'Bug', '205'], ['Beedrill', 'Bug', '395'], ['Pidgey', 'Normal', '251'], ['Pidgeotto', 'Normal', '349'], ['Pidgeot', 'Normal', '479'], ['Rattata', 'Normal', '253'], ['Raticate', 'Normal', '413'], ['Spearow', 'Normal', '262'], ['Fearow', 'Normal', '442'], ['Ekans', 'Poison', '288'], ['Arbok', 'Poison', '448'], ['Pikachu', 'Electric', '320'], ['Raichu', 'Electric', '485'], ['Sandshrew', 'Ground', '300'], ['Sandslash', 'Ground', '450'], ['Nidoran?', 'Poison', '275'], ['Nidorina', 'Poison', '365'], ['Nidoqueen', 'Poison', '505'], ['Nidoran?', 'Poison', '273'], ['Nidorino', 'Poison', '365'], ['Nidoking', 'Poison', '505'], ['Clefairy', 'Fairy', '323'], ['Clefable', 'Fairy', '483'], ['Vulpix', 'Fire', '299'], ['Ninetales', 'Fire', '505'], ['Jigglypuff', 'Normal', '270'], ['Wigglytuff', 'Normal', '435'], ['Zubat', 'Poison', '245'], ['Golbat', 'Poison', '455'], ['Oddish', 'Grass', '320'], ['Gloom', 'Grass', '395'], ['Vileplume', 'Grass', '490'], ['Paras', 'Bug', '285'], ['Parasect', 'Bug', '405'], ['Venonat', 'Bug', '305'], ['Venomoth', 'Bug', '450'], ['Diglett', 'Ground', '265'], ['Dugtrio', 'Ground', '425'], ['Meowth', 'Normal', '290'], ['Persian', 'Normal', '440'], ['Psyduck', 'Water', '320'], ['Golduck', 'Water', '500'], ['Mankey', 'Fighting', '305'], ['Primeape', 'Fighting', '455'], ['Growlithe', 'Fire', '350'], ['Arcanine', 'Fire', '555'], ['Poliwag', 'Water', '300'], ['Poliwhirl', 'Water', '385'], ['Poliwrath', 'Water', '510'], ['Abra', 'Psychic', '310'], ['Kadabra', 'Psychic', '400'], ['Alakazam', 'Psychic', '500'], ['Machop', 'Fighting', '305'], ['Machoke', 'Fighting', '405'], ['Machamp', 'Fighting', '505'], ['Bellsprout', 'Grass', '300'], ['Weepinbell', 'Grass', '390'], ['Victreebel', 'Grass', '490'], ['Tentacool', 'Water', '335'], ['Tentacruel', 'Water', '515'], ['Geodude', 'Rock', '300'], ['Graveler', 'Rock', '390'], ['Golem', 'Rock', '495'], ['Ponyta', 'Fire', '410'], ['Rapidash', 'Fire', '500'], ['Slowpoke', 'Water', '315'], ['Slowbro', 'Water', '490'], ['Magnemite', 'Electric', '325'], ['Magneton', 'Electric', '465'], ["Farfetch'd", 'Normal', '377'], ['Doduo', 'Normal', '310'], ['Dodrio', 'Normal', '470'], ['Seel', 'Water', '325'], ['Dewgong', 'Water', '475'], ['Grimer', 'Poison', '325'], ['Muk', 'Poison', '500'], ['Shellder', 'Water', '305'], ['Cloyster', 'Water', '525'], ['Gastly', 'Ghost', '310'], ['Haunter', 'Ghost', '405'], ['Gengar', 'Ghost', '500'], ['Onix', 'Rock', '385'], ['Drowzee', 'Psychic', '328'], ['Hypno', 'Psychic', '483'], ['Krabby', 'Water', '325'], ['Kingler', 'Water', '475'], ['Voltorb', 'Electric', '330'], ['Electrode', 'Electric', '490'], ['Exeggcute', 'Grass', '325'], ['Exeggutor', 'Grass', '530'], ['Cubone', 'Ground', '320'], ['Marowak', 'Ground', '425'], ['Hitmonlee', 'Fighting', '455'], ['Hitmonchan', 'Fighting', '455'], ['Lickitung', 'Normal', '385'], ['Koffing', 'Poison', '340'], ['Weezing', 'Poison', '490'], ['Rhyhorn', 'Ground', '345'], ['Rhydon', 'Ground', '485'], ['Chansey', 'Normal', '450'], ['Tangela', 'Grass', '435'], ['Kangaskhan', 'Normal', '490'], ['Horsea', 'Water', '295'], ['Seadra', 'Water', '440'], ['Goldeen', 'Water', '320'], ['Seaking', 'Water', '450'], ['Staryu', 'Water', '340'], ['Starmie', 'Water', '520'], ['Scyther', 'Bug', '500'], ['Jynx', 'Ice', '455'], ['Electabuzz', 'Electric', '490'], ['Magmar', 'Fire', '495'], ['Pinsir', 'Bug', '500'], ['Tauros', 'Normal', '490'], ['Magikarp', 'Water', '200'], ['Gyarados', 'Water', '540'], ['Lapras', 'Water', '535'], ['Ditto', 'Normal', '288'], ['Eevee', 'Normal', '325'], ['Vaporeon', 'Water', '525'], ['Jolteon', 'Electric', '525'], ['Flareon', 'Fire', '525'], ['Porygon', 'Normal', '395'], ['Omanyte', 'Rock', '355'], ['Omastar', 'Rock', '495'], ['Kabuto', 'Rock', '355'], ['Kabutops', 'Rock', '495'], ['Aerodactyl', 'Rock', '515'], ['Snorlax', 'Normal', '540'], ['Articuno', 'Ice', '580'], ['Zapdos', 'Electric', '580'], ['Moltres', 'Fire', '580'], ['Dratini', 'Dragon', '300'], ['Dragonair', 'Dragon', '420'], ['Dragonite', 'Dragon', '600'], ['Mewtwo', 'Psychic', '680'], ['Mew', 'Psychic', '600']]


frame_styles = {"relief": "groove",
                "bd": 3, "bg": "#BEB2A7",
                "fg": "#073bb3", "font": ("Arial", 9, "bold")}

frame_styles_1 = {"relief": "groove",
                "bd": 3, "bg": "#e6faf9",
                "fg": "#073bb3", "font": ("Arial", 9, "bold")}

frame_styles_2 = {"relief": "groove",
                "bd": 3, "bg": "#faf7e5",
                "fg": "#073bb3", "font": ("Arial", 9, "bold")}

frame_styles_3 = {"relief": "groove",
                "bd": 3, "bg": "#e5fae9",
                "fg": "#073bb3", "font": ("Arial", 9, "bold")}

frame_styles_4 = {"relief": "groove",
                "bd": 3, "bg": "#e8e5fa",
                "fg": "#073bb3", "font": ("Arial", 9, "bold")}

frame_styles_5 = {"relief": "groove",
                "bd": 3, "bg": "#fae5e5",
                "fg": "#073bb3", "font": ("Arial", 9, "bold")}

def check_user_input_number(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
        return True
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("Input is a float  number. Number = ", val)
            return True
        except ValueError:
            print("No.. "+str(input)+"is not a number. It's a string")
            return False

def createTable(table, datset):

    for i in range(0, len(table['columns']) + 1):
        if i == 0:
            table.column("#0", width=0, stretch=NO)
            table.heading("#0", text="", anchor="w")
        elif i > 0:
            table.column(str(table["columns"][i - 1]), anchor="w", width=120)
            table.heading(str(table["columns"][i - 1]), text=str(table["columns"][i - 1]), anchor="w")

    for i in range(0, len(datset)):
        row = []
        for j in range(0, len(datset[0])):
            row.append(datset[i][j])

        table.insert(parent='', index='end', iid=str(i), text='',
                        values=(row))
                        #values=(str(datset[i][0]), str(datset[i][1]), str(datset[i][2]), str(datset[i][3])))

    table.pack()

class MyApp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        main_frame = tk.Frame(self, bg="#84CEEB", height=600, width=1024)
        main_frame.pack_propagate(0)
        main_frame.pack(fill="both", expand="true")
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        #self.resizable(0, 0) #prevents the app from being resized
        self.geometry("1200x600") #fixes the applications size
        self.frames = {}
        pages = (PageCL, PageMxC, PageMS, PageMult, PageMCLC)
        for F in pages:
            frame = F(main_frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(PageCL)
        menubar = MenuBar(self)
        tk.Tk.config(self, menu=menubar)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def Quit_application(self):
        self.destroy()

class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        menu_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu1", menu=menu_file)
        menu_file.add_command(label="Congruencial Lineal", command=lambda: parent.show_frame(PageCL))
        menu_file.add_command(label="Congruencial Mixto", command=lambda: parent.show_frame(PageMxC))
        menu_file.add_command(label="Centros Cuadrados", command=lambda: parent.show_frame(PageMS))
        menu_file.add_command(label="Multiplicativo Congruencial", command=lambda: parent.show_frame(PageMult))

        menu_file.add_command(label="Congruencial Lineal Combinado", command=lambda: parent.show_frame(PageMCLC))

        menu_file.add_separator()
        menu_file.add_command(label="Cerrar Aplicación", command=lambda: parent.Quit_application())


class GUI(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.main_frame = tk.Frame(self, bg="#BEB2A7", height=600, width=1024)
        # self.main_frame.pack_propagate(0)
        self.main_frame.pack(fill="both", expand="true")
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)


class PageCL(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        self.main_frame.configure(bg= frame_styles_1.get("bg"))

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Congruencial Lineal")
        label1.pack(side="top")
        label1.config(bg=frame_styles_1.get("bg"))

        frame1 = tk.LabelFrame(self, frame_styles_1, text="Input")
        frame1.place(rely=0.09, relx=0.02, height=500, width=200)

        #initial_seed, a, c, m, num_randoms

        initial_seed_label = tk.Label(frame1, text="Semilla :")
        initial_seed_label.pack(anchor="w")
        initial_seed_label.config(bg= frame_styles_1.get("bg"))

        initial_seed_input = tk.Entry(frame1)
        initial_seed_input.insert(0, 4)
        initial_seed_input.pack(anchor="w")

        a_label = tk.Label(frame1, text="a :")
        a_label.pack(anchor="w")
        a_label.config(bg=frame_styles_1.get("bg"))

        a_input = tk.Entry(frame1, width=20)
        a_input.insert(0, 5)
        a_input.pack(anchor="w")

        c_label = tk.Label(frame1, text="c :")
        c_label.pack(anchor="w")
        c_label.config(bg= frame_styles_1.get("bg"))

        c_input = tk.Entry(frame1, width=20)
        c_input.insert(0, 7)
        c_input.pack(anchor="w")

        m_label = tk.Label(frame1, text="m :")
        m_label.pack(anchor="w")
        m_label.config(bg= frame_styles_1.get("bg"))

        m_input = tk.Entry(frame1, width=20)
        m_input.insert(0, 8)
        m_input.pack(anchor="w")

        num_randoms_label = tk.Label(frame1, text="No. Randoms :")
        num_randoms_label.pack(anchor="w")
        num_randoms_label.config(bg= frame_styles_1.get("bg"))

        num_randoms_input = tk.Entry(frame1, width=20)
        num_randoms_input.insert(0, 7)
        num_randoms_input.pack(anchor="w")

        button1 = tk.Button(frame1, text="GENERACION"   , width=20,command=lambda: generateRand(frame2))
        button1.pack(anchor="w")

        chi_button = tk.Button(frame1, text="Chi cuadrada"  , width=20, command=lambda: chi_clac(frame2))
        chi_button.pack(anchor="w")

        kol_button = tk.Button(frame1, text="Kolmogrov"     , width=20, command=lambda: kol_clac(frame2))
        kol_button.pack(anchor="w")

        res_button = tk.Button(frame1, text="Resultados"    , width=20, command=lambda: OpenResultsWindows())
        res_button.pack(anchor="w")

        frame2 = tk.LabelFrame(self, frame_styles_1, text="Tablas")
        frame2.place(rely=0.09, relx=0.2, height=500, width=900)

        def kol_clac(frame):
            initial_seed = str(initial_seed_input.get())
            a = str(a_input.get())
            c = str(c_input.get())
            m = str(m_input.get())
            num_randoms = str(num_randoms_input.get())

            initial_seed_input.delete(0, "end")
            a_input.delete(0, "end")
            c_input.delete(0, "end")
            m_input.delete(0, "end")
            num_randoms_input.delete(0, "end")

            initial_seed_input.insert(0, 4)
            a_input.insert(0, 5)
            c_input.insert(0, 7)
            m_input.insert(0, 8)
            num_randoms_input.insert(0, 7)

            for widget in frame2.winfo_children():
                widget.destroy()

            print("Input Test")
            inputtestArr= [check_user_input_number(initial_seed),
                        check_user_input_number(a),
                        check_user_input_number(c),
                        check_user_input_number(m),
                        check_user_input_number(num_randoms)]

            print(inputtestArr)

            inputtest= True
            for input in inputtestArr:
                if input == False:
                    inputtest= False

            if not inputtest:
                print("Se aborta el calculo por inputs erroneos")
                ans_label = tk.Label(frame, text="Inputs erroneos")
                ans_label.pack()
                ans_label.config(bg="#f5d1cc")
            else:
                LC= LinearCongruential(eval(initial_seed), eval(a), eval(c), eval(m), eval(num_randoms))
                LCres= LC.getResultsList()

                kol_label = tk.Label(frame, text="Kolmogrov :")
                kol_label.pack()

                kol_frame = Frame(frame)
                kol_frame.pack()
                kol_table = ttk.Treeview(kol_frame)
                kol_table['columns'] = ('i', 'Ri', '1/N', 'I/N - Ri', 'Ri-(i-1)/N')

                column = 3
                rand = [row[column] for row in LCres]
                LCkolAns = Mate.kolmogrov(rand)

                createTable(kol_table, LCkolAns[1])

                if LCkolAns[0] == True:
                    ans_label = tk.Label(frame, text="SE ACEPTA")
                    ans_label.pack()
                    ans_label.config(bg="#ccf5d0")
                elif LCkolAns[0] == False:
                    ans_label = tk.Label(frame, text="SE RECHAZA")
                    ans_label.pack()
                    ans_label.config(bg="#f5d1cc")

        def chi_clac(frame):
            initial_seed = str(initial_seed_input.get())
            a = str(a_input.get())
            c = str(c_input.get())
            m = str(m_input.get())
            num_randoms = str(num_randoms_input.get())

            for widget in frame2.winfo_children():
                widget.destroy()

            LC= LinearCongruential(eval(initial_seed), eval(a), eval(c), eval(m), eval(num_randoms))
            LCres= LC.getResultsList()

            chi_label = tk.Label(frame, text="Chi cuadrada :")
            chi_label.pack()

            Chi_frame = Frame(frame)
            Chi_frame.pack()
            Chi_table = ttk.Treeview(Chi_frame)
            Chi_table['columns'] = ('k', 'Class-', 'Class+', 'Foi', 'Prob', 'Fei', 'Fo-Fe')

            column = 3
            rand = [row[column] for row in LCres]
            LCchiSqrtAns  = Mate.chi(rand)

            createTable(Chi_table, LCchiSqrtAns[1])

            if LCchiSqrtAns[0] == True:
                ans_label = tk.Label(frame, text="SE ACEPTA")
                ans_label.pack()
                ans_label.config(bg="#ccf5d0")
            elif LCchiSqrtAns[0] == False:
                ans_label = tk.Label(frame, text="SE RECHAZA")
                ans_label.pack()
                ans_label.config(bg="#f5d1cc")

        def generateRand(frame):
            initial_seed = str(initial_seed_input.get())
            a = str(a_input.get())
            c = str(c_input.get())
            m = str(m_input.get())
            num_randoms = str(num_randoms_input.get())

            for widget in frame2.winfo_children():
                widget.destroy()

            print("initial_seed: "+ str(initial_seed))
            print("a: " + str(a))
            print("c: " + str(c))
            print("m: " + str(m))
            print("num_randoms: " + str(num_randoms))
            print("___________________________ ")

            label1 = tk.Label(frame, text="Numeros Random :")
            label1.pack()

            LC= LinearCongruential(eval(initial_seed), eval(a), eval(c), eval(m), eval(num_randoms))
            LCres= LC.getResultsList()
            print(LCres)

            LC_frame = Frame(frame)
            LC_frame.pack()
            LC_table = ttk.Treeview(LC_frame)
            # i, semilla, No. aleatorio, random_i
            # 4, 5, 7, 8, 7
            LC_table['columns'] = ('i', 'semilla', 'aleat', 'rand')

            #print("###################################")
            #print(LC_table["columns"])
            #print(LC_table["columns"][1])

            createTable(LC_table, LCres)

        class OpenResultsWindows(tk.Tk):

            def __init__(self, *args, **kwargs):
                tk.Tk.__init__(self, *args, **kwargs)

                main_frame = tk.Frame(self, width=1000,height=700)
                main_frame.pack_propagate(0)
                main_frame.pack(fill="both", expand="true")
                #main_frame.grid_rowconfigure(0, weight=1)
                #main_frame.grid_columnconfigure(0, weight=1)
                self.title("Resultados juntos")
                self.geometry("1000x800")
                #self.resizable(0, 0)

                canvas = Canvas(main_frame, bg='#FFFFFF', width=1000, height=700, scrollregion=(0, 0, 500, 500))

                vbar = Scrollbar(canvas, orient=VERTICAL)
                vbar.pack(side=RIGHT, fill=Y)
                vbar.config(command=canvas.yview)

                canvas.config(width=1000, height=700)
                canvas.config(yscrollcommand=vbar.set)
                canvas.pack(side=LEFT, expand=True, fill=BOTH)

                vbar.config(command=canvas.yview)

                generateRand(canvas)

                chi_clac(canvas)

                kol_clac(canvas)






class PageMxC(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        self.main_frame.configure(bg= frame_styles_2.get("bg"))

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Congruencial Mixto")
        label1.pack(side="top")
        label1.config(bg=frame_styles_2.get("bg"))

        frame1 = tk.LabelFrame(self, frame_styles_2, text="Input")
        frame1.place(rely=0.09, relx=0.02, height=500, width=200)

        #initial_seed, a, c, m, num_randoms

        initial_seed_label = tk.Label(frame1, text="Semilla :")
        initial_seed_label.pack(anchor="w")
        initial_seed_label.config(bg= frame_styles_2.get("bg"))

        initial_seed_input = tk.Entry(frame1)
        initial_seed_input.pack(anchor="w")

        a_label = tk.Label(frame1, text="a :")
        a_label.pack(anchor="w")
        a_label.config(bg=frame_styles_2.get("bg"))

        a_input = tk.Entry(frame1, width=20)
        a_input.pack(anchor="w")

        c_label = tk.Label(frame1, text="c :")
        c_label.pack(anchor="w")
        c_label.config(bg= frame_styles_2.get("bg"))

        c_input = tk.Entry(frame1, width=20)
        c_input.pack(anchor="w")

        m_label = tk.Label(frame1, text="m :")
        m_label.pack(anchor="w")
        m_label.config(bg= frame_styles_2.get("bg"))

        m_input = tk.Entry(frame1, width=20)
        m_input.pack(anchor="w")

        num_randoms_label = tk.Label(frame1, text="No. Randoms :")
        num_randoms_label.pack(anchor="w")
        num_randoms_label.config(bg= frame_styles_2.get("bg"))

        num_randoms_input = tk.Entry(frame1, width=20)
        num_randoms_input.pack(anchor="w")

        mxc_button = tk.Button(frame1, text="GENERACION"  , width=20, command=lambda: mxc_calc(frame2))
        mxc_button.pack(anchor="w")

        chi_button = tk.Button(frame1, text="Chi cuadrada"  , width=20, command=lambda: chi_clac(frame2))
        chi_button.pack(anchor="w")

        kol_button = tk.Button(frame1, text="Kolmogrov"     , width=20, command=lambda: kol_clac(frame2))
        kol_button.pack(anchor="w")

        res_button = tk.Button(frame1, text="Resultados"    , width=20, command=lambda: OpenResultsWindows())
        res_button.pack(anchor="w")

        frame2 = tk.LabelFrame(self, frame_styles_2, text="Tablas")
        frame2.place(rely=0.09, relx=0.2, height=500, width=900)

        def mxc_calc(frame):
            initial_seed = str(initial_seed_input.get())
            a = str(a_input.get())
            c = str(c_input.get())
            m = str(m_input.get())
            num_randoms = str(num_randoms_input.get())

            for widget in frame.winfo_children():
                widget.destroy()

            print("initial_seed: "+ str(initial_seed))
            print("a: " + str(a))
            print("c: " + str(c))
            print("m: " + str(m))
            print("num_randoms: " + str(num_randoms))
            print("___________________________ ")

            label1 = tk.Label(frame, text="Numeros Random :")
            label1.pack()

            MxC= MixedCongruential(eval(initial_seed), eval(a), eval(c), eval(m), eval(num_randoms))
            MxCres= MxC.getResultsList()
            print(MxCres)

            MxC_frame = Frame(frame)
            MxC_frame.pack()
            MxC_table = ttk.Treeview(MxC_frame)
            MxC_table['columns'] = ('i', 'Semilla', "No. Aleatorio", "Ri")

            if not MxCres:
                ans_label = tk.Label(frame, text="No se cumplieron las características del Teorema HULL-DOBELL")
                ans_label.pack()
                ans_label.config(bg="#f5d1cc")
            else:
                createTable(MxC_table, MxCres)

        def kol_clac(frame):
            initial_seed = str(initial_seed_input.get())
            a = str(a_input.get())
            c = str(c_input.get())
            m = str(m_input.get())
            num_randoms = str(num_randoms_input.get())

            for widget in frame2.winfo_children():
                widget.destroy()

            MxC= LinearCongruential(eval(initial_seed), eval(a), eval(c), eval(m), eval(num_randoms))
            MxCres= MxC.getResultsList()

            kol_label = tk.Label(frame, text="Kolmogrov :")
            kol_label.pack()

            kol_frame = Frame(frame)
            kol_frame.pack()

            kol_table = ttk.Treeview(kol_frame)
            kol_table['columns'] = ('i', 'Ri', '1/N', 'I/N - Ri', 'Ri-(i-1)/N')

            column = 3
            rand = [row[column] for row in MxCres]
            MxCkolAns = Mate.kolmogrov(rand)

            createTable(kol_table, MxCkolAns[1])

            if MxCkolAns[0] == True:
                ans_label = tk.Label(frame, text="SE ACEPTA")
                ans_label.pack()
                ans_label.config(bg="#ccf5d0")
            elif MxCkolAns[0] == False:
                ans_label = tk.Label(frame, text="SE RECHAZA")
                ans_label.pack()
                ans_label.config(bg="#f5d1cc")

        def chi_clac(frame):
            initial_seed = str(initial_seed_input.get())
            a = str(a_input.get())
            c = str(c_input.get())
            m = str(m_input.get())
            num_randoms = str(num_randoms_input.get())

            for widget in frame2.winfo_children():
                widget.destroy()

            LC= LinearCongruential(eval(initial_seed), eval(a), eval(c), eval(m), eval(num_randoms))
            LCres= LC.getResultsList()

            chi_label = tk.Label(frame, text="Chi cuadrada :")
            chi_label.pack()

            Chi_frame = Frame(frame)
            Chi_frame.pack()
            Chi_table = ttk.Treeview(Chi_frame)
            Chi_table['columns'] = ('k', 'Class-', 'Class+', 'Foi', 'Prob', 'Fei', 'Fo-Fe')

            column = 3
            rand = [row[column] for row in LCres]
            LCchiSqrtAns  = Mate.chi(rand)

            createTable(Chi_table, LCchiSqrtAns[1])

            if LCchiSqrtAns[0] == True:
                ans_label = tk.Label(frame, text="SE ACEPTA")
                ans_label.pack()
                ans_label.config(bg="#ccf5d0")
            elif LCchiSqrtAns[0] == False:
                ans_label = tk.Label(frame, text="SE RECHAZA")
                ans_label.pack()
                ans_label.config(bg="#f5d1cc")

        class OpenResultsWindows(tk.Tk):

            def __init__(self, *args, **kwargs):
                tk.Tk.__init__(self, *args, **kwargs)

                main_frame = tk.Frame(self)
                main_frame.pack_propagate(0)
                main_frame.pack(fill="both", expand="true")
                main_frame.grid_rowconfigure(0, weight=1)
                main_frame.grid_columnconfigure(0, weight=1)
                self.title("resultados jutnos")
                self.geometry("1000x800")
                #self.resizable(0, 0)

                mxc_calc(main_frame)

                chi_clac(main_frame)

                kol_clac(main_frame)



class PageMS(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        self.main_frame.configure(bg= frame_styles_3.get("bg"))

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Centros Cuadrados")
        label1.pack(side="top")
        label1.config(bg=frame_styles_3.get("bg"))

        frame1 = tk.LabelFrame(self, frame_styles_3, text="Input")
        frame1.place(rely=0.09, relx=0.02, height=500, width=200)

        #initial_seed, a, c, m, num_randoms

        initial_seed_label = tk.Label(frame1, text="Semilla :")
        initial_seed_label.pack(anchor="w")
        initial_seed_label.config(bg= frame_styles_3.get("bg"))

        initial_seed_input = tk.Entry(frame1)
        initial_seed_input.pack(anchor="w")

        num_randoms_label = tk.Label(frame1, text="No. Randoms :")
        num_randoms_label.pack(anchor="w")
        num_randoms_label.config(bg= frame_styles_3.get("bg"))

        num_randoms_input = tk.Entry(frame1, width=20)
        num_randoms_input.pack(anchor="w")

        chi_button = tk.Button(frame1, text="GENERACION", width=20, command=lambda: ms_calc(frame2))
        chi_button.pack(anchor="w")

        frame2 = tk.LabelFrame(self, frame_styles_3, text="Tablas")
        frame2.place(rely=0.09, relx=0.2, height=500, width=900)

        def ms_calc(frame):
            initial_seed = str(initial_seed_input.get())
            num_randoms = str(num_randoms_input.get())

            for widget in frame.winfo_children():
                widget.destroy()

            print("initial_seed: "+ str(initial_seed))
            print("num_randoms: " + str(num_randoms))
            print("___________________________ ")


            MS= MiddleSquares(eval(initial_seed),eval(num_randoms))
            MSres= MS.getResultsList()
            print(MSres)

            MS_frame = Frame(frame)
            MS_frame.pack()
            MS_table = ttk.Treeview(MS_frame)
            MS_table['columns'] = ('i', 'Semilla', "Generador", "No. Aleatorio", "Ri")

            if not MSres:
                ans_label = tk.Label(frame, text="No se cumplieron las características del Teorema HULL-DOBELL")
                ans_label.pack()
                ans_label.config(bg="#f5d1cc")
            else:
                createTable(MS_table, MSres)

class PageMult(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        self.main_frame.configure(bg=frame_styles_4.get("bg"))

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Multiplicativo Congruencial")
        label1.pack(side="top")
        label1.config(bg=frame_styles_4.get("bg"))

        frame1 = tk.LabelFrame(self, frame_styles_4, text="Input")
        frame1.place(rely=0.09, relx=0.02, height=500, width=200)

        # initial_seed, a, c, m, num_randoms

        initial_seed_label = tk.Label(frame1, text="Semilla :")
        initial_seed_label.pack(anchor="w")
        initial_seed_label.config(bg=frame_styles_4.get("bg"))

        initial_seed_input = tk.Entry(frame1)
        initial_seed_input.pack(anchor="w")

        a_label = tk.Label(frame1, text="a :")
        a_label.pack(anchor="w")
        a_label.config(bg=frame_styles_4.get("bg"))

        a_input = tk.Entry(frame1, width=20)
        a_input.pack(anchor="w")

        m_label = tk.Label(frame1, text="m :")
        m_label.pack(anchor="w")
        m_label.config(bg=frame_styles_4.get("bg"))

        m_input = tk.Entry(frame1, width=20)
        m_input.pack(anchor="w")

        num_randoms_label = tk.Label(frame1, text="No. Randoms :")
        num_randoms_label.pack(anchor="w")
        num_randoms_label.config(bg=frame_styles_4.get("bg"))

        num_randoms_input = tk.Entry(frame1, width=20)
        num_randoms_input.pack(anchor="w")

        multc_button = tk.Button(frame1, text="GENERACION", width=20, command=lambda: mult_calc(frame2))
        multc_button.pack(anchor="w")

        chi_button = tk.Button(frame1, text="Chi cuadrada"  , width=20, command=lambda: chi_clac(frame2))
        chi_button.pack(anchor="w")

        kol_button = tk.Button(frame1, text="Kolmogrov"     , width=20, command=lambda: kol_clac(frame2))
        kol_button.pack(anchor="w")

        res_button = tk.Button(frame1, text="Resultados"    , width=20, command=lambda: OpenResultsWindows())
        res_button.pack(anchor="w")

        frame2 = tk.LabelFrame(self, frame_styles_4, text="Tablas")
        frame2.place(rely=0.09, relx=0.2, height=500, width=900)

        def mult_calc(frame):
            initial_seed = str(initial_seed_input.get())
            a = str(a_input.get())
            m = str(m_input.get())
            num_randoms = str(num_randoms_input.get())

            for widget in frame2.winfo_children():
                widget.destroy()

            print("initial_seed: " + str(initial_seed))
            print("a: " + str(a))
            print("m: " + str(m))
            print("num_randoms: " + str(num_randoms))
            print("___________________________ ")

            label1 = tk.Label(frame, text="Random :")
            label1.pack()

            MultC = MultiplicativeCongruential(eval(initial_seed), eval(a), eval(m), eval(num_randoms))
            MultCres = MultC.getResultsList()
            print(MultCres)

            MultC_frame = Frame(frame)
            MultC_frame.pack()
            MultC_table = ttk.Treeview(MultC_frame)
            MultC_table['columns'] = ('i', 'semilla', "Random", "Ri")

            if not MultCres:
                ans_label = tk.Label(frame, text="No se cumplieron las características")
                ans_label.pack()
                ans_label.config(bg="#f5d1cc")
            else:
                createTable(MultC_table, MultCres)

        def kol_clac(frame):
            initial_seed = str(initial_seed_input.get())
            a = str(a_input.get())
            m = str(m_input.get())
            num_randoms = str(num_randoms_input.get())

            for widget in frame2.winfo_children():
                widget.destroy()

            MultC = MultiplicativeCongruential(eval(initial_seed), eval(a), eval(m), eval(num_randoms))
            MultCres = MultC.getResultsList()
            print(MultCres)

            kol_label = tk.Label(frame, text="Kolmogrov :")
            kol_label.pack()

            kol_frame = Frame(frame)
            kol_frame.pack()

            kol_table = ttk.Treeview(kol_frame)
            kol_table['columns'] = ('i', 'Ri', '1/N', 'I/N - Ri', 'Ri-(i-1)/N')

            column = 3
            rand = [row[column] for row in MultCres]
            MultkolAns = Mate.kolmogrov(rand)

            createTable(kol_table, MultkolAns[1])

            if MultkolAns[0] == True:
                ans_label = tk.Label(frame, text="SE ACEPTA")
                ans_label.pack()
                ans_label.config(bg="#ccf5d0")
            elif MultkolAns[0] == False:
                ans_label = tk.Label(frame, text="SE RECHAZA")
                ans_label.pack()
                ans_label.config(bg="#f5d1cc")

        def chi_clac(frame):
            initial_seed = str(initial_seed_input.get())
            a = str(a_input.get())
            m = str(m_input.get())
            num_randoms = str(num_randoms_input.get())

            for widget in frame2.winfo_children():
                widget.destroy()

            MultC = MultiplicativeCongruential(eval(initial_seed), eval(a), eval(m), eval(num_randoms))
            MultCres = MultC.getResultsList()
            print(MultCres)

            chi_label = tk.Label(frame, text="Chi cuadrada :")
            chi_label.pack()

            Chi_frame = Frame(frame)
            Chi_frame.pack()
            Chi_table = ttk.Treeview(Chi_frame)
            Chi_table['columns'] = ('k', 'Class-', 'Class+', 'Foi', 'Prob', 'Fei', 'Fo-Fe')

            column = 3
            rand = [row[column] for row in MultCres]
            MultCchiSqrtAns = Mate.chi(rand)

            createTable(Chi_table, MultCchiSqrtAns[1])

            if MultCchiSqrtAns[0] == True:
                ans_label = tk.Label(frame, text="SE ACEPTA")
                ans_label.pack()
                ans_label.config(bg="#ccf5d0")
            elif MultCchiSqrtAns[0] == False:
                ans_label = tk.Label(frame, text="SE RECHAZA")
                ans_label.pack()
                ans_label.config(bg="#f5d1cc")

        class OpenResultsWindows(tk.Tk):

            def __init__(self, *args, **kwargs):
                tk.Tk.__init__(self, *args, **kwargs)

                main_frame = tk.Frame(self)
                main_frame.pack_propagate(0)
                main_frame.pack(fill="both", expand="true")
                main_frame.grid_rowconfigure(0, weight=1)
                main_frame.grid_columnconfigure(0, weight=1)
                self.title("resultados jutnos")
                self.geometry("1000x800")
                #self.resizable(0, 0)

                mult_calc(main_frame)

                chi_clac(main_frame)

                kol_clac(main_frame)

class PageMCLC(GUI):
    def __init__(self, parent, controller):
        GUI.__init__(self, parent)

        self.main_frame.configure(bg=frame_styles_5.get("bg"))

        label1 = tk.Label(self.main_frame, font=("Verdana", 20), text="Metodo Congruencial Lineal Combinado")
        label1.pack(side="top")
        label1.config(bg=frame_styles_5.get("bg"))

        frame1 = tk.LabelFrame(self, frame_styles_5, text="Input")
        frame1.place(rely=0.09, relx=0.02, height=500, width=200)

        # initial_seed, a, c, m, num_randoms

        initial_seed_label = tk.Label(frame1, text="Semilla :")
        initial_seed_label.pack(anchor="w")
        initial_seed_label.config(bg=frame_styles_5.get("bg"))

        initial_seed_input = tk.Entry(frame1)
        initial_seed_input.pack(anchor="w")

        a_label = tk.Label(frame1, text="a :")
        a_label.pack(anchor="w")
        a_label.config(bg=frame_styles_5.get("bg"))

        a_input = tk.Entry(frame1, width=20)
        a_input.pack(anchor="w")

        m_label = tk.Label(frame1, text="m :")
        m_label.pack(anchor="w")
        m_label.config(bg=frame_styles_5.get("bg"))

        m_input = tk.Entry(frame1, width=20)
        m_input.pack(anchor="w")

        num_randoms_label = tk.Label(frame1, text="No. Randoms :")
        num_randoms_label.pack(anchor="w")
        num_randoms_label.config(bg=frame_styles_5.get("bg"))

        num_randoms_input = tk.Entry(frame1, width=20)
        num_randoms_input.pack(anchor="w")

        multc_button = tk.Button(frame1, text="GENERACION", width=20, command=lambda: mclc_calc(frame2))
        multc_button.pack(anchor="w")

        frame2 = tk.LabelFrame(self, frame_styles_5, text="Tablas")
        frame2.place(rely=0.09, relx=0.2, height=500, width=900)

        def mclc_calc(frame):
            initial_seed = str(initial_seed_input.get())
            a = str(a_input.get())
            m = str(m_input.get())
            num_randoms = str(num_randoms_input.get())

            for widget in frame2.winfo_children():
                widget.destroy()

            print("initial_seed: " + str(initial_seed))
            print("a: " + str(a))
            print("m: " + str(m))
            print("num_randoms: " + str(num_randoms))
            print("___________________________ ")

            label1 = tk.Label(frame, text="Random :")
            label1.pack()

            MultC = MultiplicativeCongruential(eval(initial_seed), eval(a), eval(m), eval(num_randoms))
            MultCres = MultC.getResultsList()
            print(MultCres)

            MultC_frame = Frame(frame)
            MultC_frame.pack()
            MultC_table = ttk.Treeview(MultC_frame)
            MultC_table['columns'] = ('i', 'semilla', "Random")

            if not MultCres:
                ans_label = tk.Label(frame, text="No se cumplieron las características")
                ans_label.pack()
                ans_label.config(bg="#f5d1cc")
            else:
                createTable(MultC_table, MultCres)



root = MyApp()
root.mainloop()