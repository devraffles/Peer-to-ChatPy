# Peer-to-ChatPy

## Instalação

1. **Instale as dependências:**

   ```bash
   pip install flet
   ```

## Bibliotecas Utilizadas

O Blind Helper utiliza as seguintes bibliotecas:

* `flet`: Usada para poder usar o socket e também para o fron-end.

## Funções do Código

* **`web`: *Esse paremetro serve para pegar todas funcionalidades do framework Flet*.
  * **`web.add()`: *Função para adicionar* .
  * **`web.remove()`: *Função para remover* .
  * **`web.update()`: *Função para editar um elemento* .
  * **`web.dialog`: *Chamar o popup* .
  * **`web.pubsub.send_all`: *Envia mensagem no tunel de comunicação do socket* .
  * **`web.pubsub.subscribe`: *Posta mensagem no tunel de comunicação do socket* .
    
* **`ft.app()`: *Server para estar colocando todos os elemntos na página* .
  
* **`ft.AlertDialog`: *Popup do Flet* .
  
* **`ft.ElevatedButton`: *Botão do Flet* .
  
* **`ft.Text`: *Texto do Flet* .
  
* **`ft.TextField`: *Campo de Escrita do Flet* .
  
* **`ft.Column()`: *Organizar os elementos em coluna* .
  
* **`ft.Row`: *Organizar os elementos em linha* .

## Licença

GNU General Public License v3.0
