#pip install flet

import flet as ft

def main(web):
    titulo = ft.Text("Peer-to-ChatPy")
    
    def enviar_Mensagem_Tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        web.update()
        
    web.pubsub.subscribe(enviar_Mensagem_Tunel)
    
    titulo_Popup = ft.Text("Bem Vindo ao Peer-to-ChatPy")
    campo_Nome = ft.TextField(label="Escreva seu nome:")
    
    def enviar_Mensagem(evento):
        #prepara texto da mensagem do usuario
        texto = f"{campo_Nome.value}: {campo_Mensagem.value}"
        
        #envia mensagem no tunel
        web.pubsub.send_all(texto)
        
        #limpa comapo da mensagem
        campo_Mensagem.value = ""
        
        #atualiza tela
        web.update()
        
    campo_Mensagem = ft.TextField(label="Digite a sua mensagem:", on_submit=enviar_Mensagem)
    botao_Enviar = ft.ElevatedButton("Enviar", on_click=enviar_Mensagem)
    
    chat = ft.Column()
    
    linha_Mensagem = ft.Row([campo_Mensagem, botao_Enviar])
    
    def entrar_Chat(evento):
        web.remove(titulo)
        web.remove(botao_iniciar)
        popup.open = False
        
        web.add(chat)
        
        web.add(linha_Mensagem)
        
        texto_Entrou_Chat = f"{campo_Nome.value} entrou no Chat"
        
        web.pubsub.send_all(texto_Entrou_Chat)
        
        web.update()
    
    botao_Entrar_Chat = ft.ElevatedButton("Entrar Chat", on_click=entrar_Chat)
    
    popup = ft.AlertDialog(
            title=titulo_Popup, 
            content=campo_Nome, 
            actions=[botao_Entrar_Chat]
        )
    
    def abrir_Poupup(evento):
        web.dialog = popup
        popup.open = True
        web.update()
    
    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=abrir_Poupup)

    web.add(titulo)
    web.add(botao_iniciar)
    

ft.app(main, view=ft.WEB_BROWSER)
