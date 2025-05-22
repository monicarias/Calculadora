import tkinter as tk
from tkinter import messagebox
import pyttsx3  # 👈 Importamos el motor de voz

# 🚀 Función para saludar con voz al iniciar
def saludar_con_voz():
    engine = pyttsx3.init()
    engine.say("Hola Mónica, estás programando como una genia usando Tee-Kinter.")
    engine.runAndWait()

# 💡 Clase de la calculadora
class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            mensaje = (
                "Hola Mónica, soy tu asistente de inteligencia artificial. "
                "Detecté un intento de división entre cero. "
                "Ni siquiera las IA más avanzadas se atreven a hacerlo. 😉"
            )
            # Mostrar mensaje en voz
            engine = pyttsx3.init()
            engine.say(mensaje)
            engine.runAndWait()

            # (opcional) También mostrar en ventana
            messagebox.showinfo("Advertencia IA", mensaje)

            return "Error: división por cero"

# 🔢 Función que maneja los botones de operación
def operar(operacion):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        calc = Calculadora(num1, num2)

        if operacion == "sumar":
            resultado = calc.sumar()
        elif operacion == "restar":
            resultado = calc.restar()
        elif operacion == "multiplicar":
            resultado = calc.multiplicar()
        elif operacion == "dividir":
            resultado = calc.dividir()

        messagebox.showinfo("Resultado", f"El resultado es: {resultado}")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa números válidos.")

# 🖼️ Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora POO con Voz")
ventana.geometry("300x250")

# 🎤 Llamar al saludo de voz al iniciar
saludar_con_voz()

# 🧾 Campos de entrada
tk.Label(ventana, text="Número 1:").pack(pady=5)
entry1 = tk.Entry(ventana)
entry1.pack()

tk.Label(ventana, text="Número 2:").pack(pady=5)
entry2 = tk.Entry(ventana)
entry2.pack()

# 🔘 Botones de operación
tk.Button(ventana, text="Sumar", command=lambda: operar("sumar")).pack(pady=5)
tk.Button(ventana, text="Restar", command=lambda: operar("restar")).pack(pady=5)
tk.Button(ventana, text="Multiplicar", command=lambda: operar("multiplicar")).pack(pady=5)
tk.Button(ventana, text="Dividir", command=lambda: operar("dividir")).pack(pady=5)

# 🟢 Ejecutar ventana
ventana.mainloop()
