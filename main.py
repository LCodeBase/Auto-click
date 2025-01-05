import pyautogui
import time
import threading
import keyboard
import tkinter as tk
from tkinter import ttk, messagebox
import json

# Configuração para máxima velocidade do pyautogui
pyautogui.PAUSE = 0

# Variáveis globais
atividade_ativa = False
tecla_ou_botao = None
velocidade = 10
contador_cliques = 0
posicao_click = None

# Função que clica repetidamente a tecla ou botão do mouse
def clicando():
    global atividade_ativa, tecla_ou_botao, velocidade, contador_cliques, posicao_click
    while atividade_ativa:
        if posicao_click:
            pyautogui.click(posicao_click)
        elif tecla_ou_botao == "mouse1":
            pyautogui.click(button='left')
        elif tecla_ou_botao == "mouse2":
            pyautogui.click(button='right')
        else:
            pyautogui.press(tecla_ou_botao)
        contador_cliques += 1
        contador_label.config(text=f"Cliques Realizados: {contador_cliques}")
        time.sleep(0.001)

# Função para iniciar a automação
def iniciar_automacao():
    global atividade_ativa
    if not tecla_ou_botao and not posicao_click:
        messagebox.showerror("Erro", "Configure uma tecla/botão ou posição válida.")
        return
    atividade_ativa = True
    threading.Thread(target=clicando, daemon=True).start()

# Função para parar a automação
def parar_automacao():
    global atividade_ativa
    atividade_ativa = False

# Função chamada ao pressionar F1
def toggle_atividade():
    global atividade_ativa
    if atividade_ativa:
        parar_automacao()
        status_label.config(text="Automação Desativada", foreground="red")
    else:
        iniciar_automacao()
        status_label.config(text="Automação Ativada", foreground="green")

# Função para configurar a tecla e a velocidade
def configurar():
    global tecla_ou_botao, velocidade, posicao_click
    tecla_ou_botao = tecla_entry.get()
    try:
        velocidade = float(velocidade_entry.get())
        if velocidade <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erro", "Velocidade deve ser um número maior que 0.")
        return
    if tecla_ou_botao.lower() == "posicao":
        posicao_click = pyautogui.position()
        tecla_ou_botao = None
        messagebox.showinfo("Posição Capturada", f"Coordenadas: {posicao_click}")
    else:
        posicao_click = None
    status_label.config(text="Configurações salvas. Pressione F1 para iniciar.", foreground="blue")
    toggle_button.config(state=tk.NORMAL)

# Função para salvar configurações em arquivo JSON
def salvar_configuracoes():
    configuracoes = {
        "tecla_ou_botao": tecla_ou_botao,
        "velocidade": velocidade,
        "posicao_click": posicao_click
    }
    with open("configuracoes.json", "w") as arquivo:
        json.dump(configuracoes, arquivo)
    messagebox.showinfo("Salvo", "Configurações salvas com sucesso!")

# Função para carregar configurações de arquivo JSON
def carregar_configuracoes():
    global tecla_ou_botao, velocidade, posicao_click
    try:
        with open("configuracoes.json", "r") as arquivo:
            configuracoes = json.load(arquivo)
            tecla_ou_botao = configuracoes.get("tecla_ou_botao")
            velocidade = configuracoes.get("velocidade", 10)
            posicao_click = tuple(configuracoes.get("posicao_click", []))
            status_label.config(text="Configurações carregadas. Pressione F1 para iniciar.", foreground="blue")
            toggle_button.config(state=tk.NORMAL)
    except FileNotFoundError:
        messagebox.showwarning("Aviso", "Nenhum arquivo de configuração encontrado.")

# Interface Gráfica com Tkinter
root = tk.Tk()
root.title("Automação de Teclas e Mouse")
root.geometry("400x400")

# Labels e inputs para configuração
frame_config = ttk.LabelFrame(root, text="Configurações")
frame_config.pack(padx=10, pady=10, fill="both", expand=True)

tecla_label = ttk.Label(frame_config, text="Digite a tecla ou 'mouse1'/'mouse2' ou 'posicao':")
tecla_label.pack(pady=5)

tecla_entry = ttk.Entry(frame_config)
tecla_entry.pack(pady=5)

velocidade_label = ttk.Label(frame_config, text="Digite a velocidade (ignorado se otimizado):")
velocidade_label.pack(pady=5)

velocidade_entry = ttk.Entry(frame_config)
velocidade_entry.pack(pady=5)

config_button = ttk.Button(frame_config, text="Salvar Configurações", command=configurar)
config_button.pack(pady=5)

save_button = ttk.Button(frame_config, text="Salvar Configurações no Arquivo", command=salvar_configuracoes)
save_button.pack(pady=5)

load_button = ttk.Button(frame_config, text="Carregar Configurações do Arquivo", command=carregar_configuracoes)
load_button.pack(pady=5)

# Status do programa
status_label = ttk.Label(root, text="Aguardando configurações...", foreground="blue")
status_label.pack(pady=10)

contador_label = ttk.Label(root, text="Cliques Realizados: 0", foreground="black")
contador_label.pack(pady=5)

toggle_button = ttk.Button(root, text="Ativar/Desativar Automação (F1)", state=tk.DISABLED, command=toggle_atividade)
toggle_button.pack(pady=10)

# Função para detectar teclas de atalho
def iniciar_atalho_tecla():
    keyboard.add_hotkey('F1', toggle_atividade)

# Inicia o atalho de tecla em uma thread separada
threading.Thread(target=iniciar_atalho_tecla, daemon=True).start()

# Inicia a interface gráfica
root.mainloop()
