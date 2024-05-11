import tkinter as tk

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecha)
        else:
            # Valor duplicado, no hacemos nada
            pass

    def inorden(self):
        return self._inorden_recursivo(self.raiz)

    def _inorden_recursivo(self, nodo):
        if nodo is not None:
            return self._inorden_recursivo(nodo.izquierda) + [nodo.valor] + self._inorden_recursivo(nodo.derecha)
        else:
            return []

    def preorden(self):
        return self._preorden_recursivo(self.raiz)

    def _preorden_recursivo(self, nodo):
        if nodo is not None:
            return [nodo.valor] + self._preorden_recursivo(nodo.izquierda) + self._preorden_recursivo(nodo.derecha)
        else:
            return []

    def postorden(self):
        return self._postorden_recursivo(self.raiz)

    def _postorden_recursivo(self, nodo):
        if nodo is not None:
            return self._postorden_recursivo(nodo.izquierda) + self._postorden_recursivo(nodo.derecha) + [nodo.valor]
        else:
            return []

class Aplicacion:
    def __init__(self, master):
        self.master = master
        self.master.title("Recorridos de Árboles Binarios")
        self.master.geometry("400x300")

        self.arbol = ArbolBinario()

        self.label = tk.Label(master, text="Inserta un valor:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.insertar_button = tk.Button(master, text="Insertar", command=self.insertar_valor)
        self.insertar_button.pack()

        self.inorden_button = tk.Button(master, text="Recorrido Inorden", command=self.recorrido_inorden)
        self.inorden_button.pack()

        self.preorden_button = tk.Button(master, text="Recorrido Preorden", command=self.recorrido_preorden)
        self.preorden_button.pack()

        self.postorden_button = tk.Button(master, text="Recorrido Postorden", command=self.recorrido_postorden)
        self.postorden_button.pack()

        self.texto = tk.Text(master, wrap="word")
        self.texto.pack(fill="both", expand=True)

    def insertar_valor(self):
        valor = int(self.entry.get())
        self.arbol.insertar(valor)
        self.actualizar_texto()

    def recorrido_inorden(self):
        recorrido = self.arbol.inorden()
        self.mostrar_recorrido("Recorrido Inorden", recorrido)

    def recorrido_preorden(self):
        recorrido = self.arbol.preorden()
        self.mostrar_recorrido("Recorrido Preorden", recorrido)

    def recorrido_postorden(self):
        recorrido = self.arbol.postorden()
        self.mostrar_recorrido("Recorrido Postorden", recorrido)

    def mostrar_recorrido(self, nombre, recorrido):
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, f"{nombre}:\n")
        self.texto.insert(tk.END, str(recorrido) + "\n\n")

    def actualizar_texto(self):
        self.texto.delete("1.0", tk.END)
        self.texto.insert(tk.END, "Árbol Binario:\n")
        self.texto.insert(tk.END, self.obtener_arbol_string(self.arbol.raiz))

    def obtener_arbol_string(self, nodo, nivel=0):
        resultado = ""
        if nodo is not None:
            resultado += self.obtener_arbol_string(nodo.derecha, nivel + 1)
            resultado += " " * 4 * nivel + f"->{nodo.valor}\n"
            resultado += self.obtener_arbol_string(nodo.izquierda, nivel + 1)
        return resultado

def main():
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()

if __name__ == "__main__":
    main()