import tkinter as tk
from tkinter import messagebox

# Função para calcular o IMC
def calcular_imc():
    try:
        altura = float(entry_altura.get()) / 100  # converter altura para metros
        peso = float(entry_peso.get())
        imc = peso / (altura ** 2)
        resultado = f"O IMC do paciente é {imc:.2f}"
        
        # Classificação do IMC
        if imc < 18.5:
            resultado += " - Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            resultado += " - Peso normal"
        elif 25 <= imc < 29.9:
            resultado += " - Sobrepeso"
        else:
            resultado += " - Obesidade"
        
        messagebox.showinfo("Resultado do IMC", resultado)
    except ValueError:
        messagebox.showwarning("Erro", "Por favor, insira valores válidos para altura e peso.")

# Criar janela principal
root = tk.Tk()
root.title("Cálculo de IMC do Paciente")

# Rótulos e entradas
tk.Label(root, text="Nome do Paciente:").grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Endereço Completo:").grid(row=1, column=0, padx=10, pady=5)
entry_endereco = tk.Entry(root)
entry_endereco.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Altura (CM):").grid(row=2, column=0, padx=10, pady=5)
entry_altura = tk.Entry(root)
entry_altura.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Peso (Kg):").grid(row=3, column=0, padx=10, pady=5)
entry_peso = tk.Entry(root)
entry_peso.grid(row=3, column=1, padx=10, pady=5)

# Botão de calcular
btn_calcular = tk.Button(root, text="Calcular IMC", command=calcular_imc)
btn_calcular.grid(row=4, column=0, columnspan=2, pady=10)

# Executar a interface
root.mainloop()
