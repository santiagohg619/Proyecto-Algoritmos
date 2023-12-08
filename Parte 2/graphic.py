import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from chatTaller1 import allOps, graphMatriz, generar_muestras


class DataEntryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ingreso de Datos")
        self.root.geometry("400x300")

        self.welcome_label = tk.Label(self.root, text="Bienvenido", font=("Arial", 18))
        self.welcome_label.pack(pady=10)

        self.file_button = tk.Button(self.root, text="Subir Archivo CSV", command=self.upload_csv)
        self.file_button.pack(pady=10)

        self.manual_button = tk.Button(self.root, text="Ingresar Manualmente", command=self.manual_entry)
        self.manual_button.pack(pady=10)

        self.creator_label = tk.Label(self.root, text="Creado por: Manu y Santiago", font=("Arial", 10))
        self.creator_label.pack(side=tk.BOTTOM)

    def upload_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            # Aquí puedes agregar la lógica para manejar el archivo CSV
            # messagebox.showinfo("Información", "Archivo CSV seleccionado: " + file_path)

            channels_data = {}
            contador=1
            numMuestras=0
            try:
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    for i in range(len(lines)):
                        print("linea actual", lines[i])
                        if not(i==len(lines)-1):
                            channel_data = lines[i][:-1].split(',')
                        else:
                            channel_data = lines[i].split(',')
                        for element in channel_data:
                            if element=='' or element not in ("0","1"):
                                print("Error por el elemento", element)
                        channels_data[chr(64+contador)]= channel_data
                        print(chr(64+contador),"\nchannel_data",channel_data)
                        contador+=1
                print()
                print(channels_data)
                #return channels_data
                numMuestras=len(channels_data[list(channels_data.keys())[0]])
                generar_muestras(len(channels_data.keys()))
                self.operar(channels_data,numMuestras)
            except FileNotFoundError:
                print("Archivo no encontrado.")
                return []


    def manual_entry(self):
        manual_window = tk.Toplevel(self.root)

        muestras = tk.simpledialog.askinteger("Ingreso Manual", "Ingrese el numero de Muestras")
        canales = tk.simpledialog.askinteger("Ingreso Manual", "Ingrese el numero de canales")

        if muestras is not None and canales is not None:
            entry_width = 5  # Ancho de los campos Entry

            for i in range(muestras):
                label = tk.Label(manual_window, text=f"{i + 1}", font=("Arial", 12))
                label.grid(row=0, column=i + 1, padx=5, pady=5)

            for j in range(canales):
                label = tk.Label(manual_window, text=f"Canal {chr(65 + j)}:", font=("Arial", 12))
                label.grid(row=j + 1, column=0, padx=5, pady=5)

            for i in range(muestras):
                for j in range(canales):
                    entry = tk.Entry(manual_window, width=entry_width)
                    entry.grid(row=j + 1, column=i + 1, padx=5, pady=5)

            save_button = tk.Button(manual_window, text="Guardar Datos", command=lambda: self.save_data(manual_window, muestras, canales))
            save_button.grid(row=canales + 1, column=muestras + 1, padx=5, pady=10)

            if muestras > 10:  # Agregar barra de desplazamiento si la cantidad de muestras es mayor que 10
                scrollbar = tk.Scrollbar(manual_window)
                scrollbar.grid(row=1, column=muestras + 2, columnspan=canales, sticky='NS')
                for i in range(canales + 1):
                    manual_window.grid_rowconfigure(i, weight=1)
                for j in range(muestras + 1):
                    manual_window.grid_columnconfigure(j, weight=1)
                for i in range(muestras):
                    for j in range(canales):
                        entry = manual_window.grid_slaves(row=j + 1, column=i + 1)[0]
                        entry.config(xscrollcommand=scrollbar.set)
                        entry.grid(row=j + 1, column=i + 1, sticky='ew')
                        scrollbar.config(command=entry.xview)

    def save_data(self, window, muestras, canales):
        data = {}
        for i in range(canales):
            row = []
            for j in range(muestras):
                entry = window.grid_slaves(row=i + 1, column=j + 1)[0]
                value = entry.get()
                if value == '' or value not in ('0', '1'):
                    messagebox.showerror("Error", f"Los datos en la muestra {j + 1}, canal {chr(65 + i)} deben ser 0 o 1 y no pueden estar vacíos.")
                    return
                row.append(value)
            data[chr(65 + i)]=row

        print("Datos ingresados:", data)
        generar_muestras(canales)
        self.operar(data,muestras)
        window.destroy()

    def show_table(self, data, title):
        # Crear una nueva ventana
        new_window = tk.Toplevel(self.root)
        new_window.title(title)

        # Crear un marco para la tabla en la nueva ventana
        frame = tk.Frame(new_window)
        frame.grid(row=0, column=0)

        #Obtencion de eiquetas
        filas=list(data.keys())
        columnas= data[list(data.keys())[0]]
        print("\n Los datos para", title)
        print(data)
        print("las columnas son",columnas)
        print("las filas son", filas)



        for i, col in enumerate(columnas):
            tk.Label(frame, text=col, borderwidth=1, relief="solid", width=10).grid(row=0, column=i+1)

        for i, fila in enumerate(filas):
            tk.Label(frame, text=fila, borderwidth=1, relief="solid", width=10).grid(row=i+1, column=0)



        # Llenar la tabla con valores del diccionario
        for i, outer_key in enumerate(data.keys()):
            for j, inner_key in enumerate(data[outer_key].keys()):
                tk.Label(frame, text=str(data[outer_key][inner_key]), borderwidth=1, relief="solid", width=10).grid(row=i+1, column=j+1)


    def operar(self, channels_data, numMuestras):

        matrizEstadoCanalF, matrizEstadoEstadoF, matrizEstadoCanalP, matrizEstadoEstadoP = allOps(channels_data,numMuestras)

        #Punto 1
        # Calcular la matriz de probabilidades basada en los estados generados aleatoriamente
        # matrizEstadoCanalF, indexEstados = calcular_matriz_EstadoCanalF(sampleData,num_muestras)
        graphMatriz(matrizEstadoCanalF,"+")
        self.show_table(matrizEstadoCanalF,"matrizEstadoCanalF")


        #Punto 2
        # matrizEstadoEstadoF = generar_matriz_EstadoEstadoF(indexEstados)
        graphMatriz(matrizEstadoEstadoF,"+")
        self.show_table(matrizEstadoEstadoF, "matrizEstadoEstadoF")
        
        #Punto 3
        # Calcular la matriz de probabilidades previas basada en los estados generados aleatoriamente Punto 3
        # matrizEstadoCanalP = calcular_matriz_EstadoCanalP(sampleData,num_muestras,indexEstados)
        graphMatriz(matrizEstadoCanalP,"-")
        self.show_table(matrizEstadoCanalP, "matrizEstadoCanalP")


        # punto 4
        # matrizEstadoEstadoP = generar_matriz_EstadoEstadoP(indexEstados)
        graphMatriz(matrizEstadoEstadoP,"-")
        self.show_table(matrizEstadoEstadoP, "matrizEstadoEstadoP")



def main():
    root = tk.Tk()
    app = DataEntryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
