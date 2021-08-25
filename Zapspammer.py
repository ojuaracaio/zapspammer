from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

### INÍCIO DA INTERFACE ###
root = Tk()
root.title('Zapspammer')
driver = webdriver.Firefox()

### FUNÇÕES DOS BOTÕES ###
def enviar_mensagens():
	alvo=entrada_alvo.get()
	alvo = alvo.split(',')
	vezes = int(entrada_vezes.get())
	msg= entrada_msg.get()

	for i in range(len(alvo)):

		busca = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
		busca.send_keys(alvo[i])
		busca.send_keys(Keys.ENTER)

		texto = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
		for i in range(vezes):
			texto.send_keys(msg)
			texto.send_keys(Keys.ENTER)


def abrir_zap():
	
	driver.get('https://web.whatsapp.com/')

### ENTRADAS ###
entrada_alvo = Entry(root)
entrada_msg = Entry(root)
entrada_vezes = Entry(root)

### BOTÕES ###
botao_zap = Button(root, text="abrir whatsapp", command=abrir_zap)
botao_enviar = Button(root, text="enviar mensagens", command=enviar_mensagens)

### ETIQUETAS ###
etiqueta_alvo = Label(root, text="Contato")
etiqueta_msg = Label(root, text="Mensagem")
etiqueta_vezes = Label(root, text="Nº de vezes")

### GRADE ###
etiqueta_alvo.grid(row=0, column=0)
etiqueta_msg.grid(row=1, column=0)
etiqueta_vezes.grid(row=2, column=0)

entrada_alvo.grid(row=0, column=1)
entrada_msg.grid(row=1, column=1)
entrada_vezes.grid(row=2, column=1)

botao_zap.grid(row=3, column=0)
botao_enviar.grid(row=3, column=1)



root.mainloop()
