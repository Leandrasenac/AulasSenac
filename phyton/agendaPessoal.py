import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import json
import os

# Função para carregar compromissos de um arquivo JSON
def carregar_compromissos():
    if os.path.exists('compromissos.json'):
        with open('compromissos.json', 'r') as file:
            return json.load(file)
    return []

# Função para salvar compromissos no arquivo JSON
def salvar_compromissos():
    with open('compromissos.json', 'w') as file:
        json.dump(compromissos, file)

# Função para adicionar compromisso
def salvar_compromisso():
    compromisso = entry_compromisso.get()
    data = cal.get_date()
    
    if compromisso == "":
        messagebox.showwarning("Aviso", "Por favor, insira a descrição do compromisso.")
        return
    
    compromisso_dict = {"data": data, "descricao": compromisso}
    compromissos.append(compromisso_dict)
    
    # Atualiza a lista na interface
    lista_compromissos.insert(tk.END, f"{data} - {compromisso}")
    
    # Limpa os campos de entrada
    entry_compromisso.delete(0, tk.END)
    
    # Salva no arquivo JSON
    salvar_compromissos()

# Função para remover compromisso
def remover_compromisso():
    try:
        # Remove o compromisso selecionado
        indice = lista_compromissos.curselection()[0]
        compromisso_removido = lista_compromissos.get(indice)
        
        # Remove o compromisso da lista interna
        data_removida = compromisso_removido.split(" - ")[0]
        compromissos[:] = [comp for comp in compromissos if comp['data'] != data_removida]
        
        lista_compromissos.delete(indice)
        
        # Salva a lista atualizada no arquivo JSON
        salvar_compromissos()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione um compromisso para remover.")

# Configuração da janela principal
root = tk.Tk()
root.title("Agenda Pessoal")

# Carregar compromissos previamente salvos
compromissos = carregar_compromissos()

# Descrição do compromisso
label_compromisso = tk.Label(root, text="Descrição do Compromisso:")
label_compromisso.pack(pady=5)

entry_compromisso = tk.Entry(root, width=40)
entry_compromisso.pack(pady=5)

# Calendário para selecionar a data
cal_label = tk.Label(root, text="Selecione a Data:")
cal_label.pack(pady=5)

cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
cal.pack(pady=10)

# Lista de compromissos
lista_label = tk.Label(root, text="Compromissos:")
lista_label.pack(pady=5)

lista_compromissos = tk.Listbox(root, height=10, width=50)
lista_compromissos.pack(pady=5)

# Adicionando compromissos existentes à lista
for comp in compromissos:
    lista_compromissos.insert(tk.END, f"{comp['data']} - {comp['descricao']}")

# Botões
botao_salvar = tk.Button(root, text="Salvar", width=20, command=salvar_compromisso)
botao_salvar.pack(pady=5)

botao_remover = tk.Button(root, text="Remover", width=20, command=remover_compromisso)
botao_remover.pack(pady=5)

# Iniciar a interface
root.mainloop()



