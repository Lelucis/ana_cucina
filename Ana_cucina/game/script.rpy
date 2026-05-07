# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Anna", color="#ff69b4")
define j = Character("Prefeito Jorge", color="#3f4ae9")
define s = Character("Dona Silvia", color="#ec7615")
define c = Character("Pescador Carlos", color="#2ceb82")
define p = Character("Padeiro Pedro", color="#cddd3b")
define l = Character("Leleco o Louco", color="#ee3050")


# Inicio do jogo

label start:

   play music "Curadora-Casa Rosa.mp3"

   scene fundocidadeana
   with fade

   "Anna esta se mudando para uma nova vila"
   "Foi uma longa viagem para chegar aqui"
   "Vale dos Pinheiros é uma vila pequena e muito acolhedora"

   scene fundoana
   with fade

   show anacucina
   
   "Ela é uma cozinheira muito boa, e está ansiosa para conhecer novas receitas"
   "Ela já aprendeu muitas receitas ao longo de sua vida"
   "Agora sua missão é aprender receitas deste novo lugar"

   hide anacucina

   show anamapa

   a "Logo que cheguei aqui, ganhei este mapa, aqui mostra toda a cidade"
   a "Escolhi algumas pessoas que achei interessante conhecer"
   a "E claro, saber se tem receitas para mim!"

   hide anamapa
   show anamapa2

   a "Humm..."
   a "Estou vendo aqui, vou visitar o Prefeito, a Dona Silvia,o Padeiro, o pescador e o Louco"

   hide anamapa2
   show anamapa3

   a "Então vamos lá?!"


   call screen telaprincipal

# Tela principal

screen telaprincipal():
   add "fundocidade"
   imagebutton:
      pos (139, 200)
      idle "prefeitobotao.png"
      hover im.MatrixColor("prefeitobotao.png", im.matrix.brightness(0.2))
      action [Hide("telaprincipal"), Jump("prefeito")]

   imagebutton:
      pos (139, 400)
      idle "botaosilvia.png"
      hover im.MatrixColor("botaosilvia.png", im.matrix.brightness(0.2))
      action [Hide("telaprincipal"), Jump("silvia")]

   imagebutton:
      pos (139, 600)
      idle "botaopescador.png"
      hover im.MatrixColor("botaopescador.png", im.matrix.brightness(0.2))
      action [Hide("telaprincipal"), Jump("pescador")]

   imagebutton:
      pos (1550, 242)
      idle "botaopadeiro.png"
      hover im.MatrixColor("botaopadeiro.png", im.matrix.brightness(0.2))
      action [Hide("telaprincipal"), Jump("padeiro")]

   imagebutton:
      pos (1550, 542)
      idle "botaolouco.png"
      hover im.MatrixColor("botaolouco.png", im.matrix.brightness(0.2))
      action [Hide("telaprincipal"), Jump("louco")]


   # Checks na tela principal
   frame:
      background Transform("images/fundomenu.png", yoffset=-35)
      xpos 786
      ypos 10
      xsize 400
      ysize 100   
      padding (30, 30)  
      vbox:
         spacing 15
         xalign 0.5
         yoffset 90

         if fimprefeito:
            text "✔ Prefeito" color "#00aa00" size 35
         else:
            text "○ Prefeito" color "#000000" size 35
 
         if fimsilvia:
            text "✔ Dona Silvia" color "#00aa00" size 35
         else:
            text "○ Dona Silvia" color "#000000" size 35
 
         if fimpescador:
            text "✔ Pescador" color "#00aa00" size 35
         else:
            text "○ Pescador" color "#000000" size 35
 
         if fimpadeiro:
            text "✔ Padeiro" color "#00aa00" size 35
         else:
            text "○ Padeiro" color "#000000" size 35
 
         if fimlouco:
            text "✔ Louco" color "#00aa00" size 35
         else:
            text "○ Louco" color "#000000" size 35

   
   if fimprefeito and fimsilvia and fimpescador and fimpadeiro and fimlouco:
      imagebutton:
         idle "botaofinal.png"
         hover im.MatrixColor("botaofinal.png", im.matrix.brightness(0.2))
         pos (837, 801)
         action [Hide("telaprincipal"), Jump("final_jogo")]

label final_jogo:

   scene fundoanafinal
   with fade

   a "Consegui! Aprendi todas as receitas da vila!"
   a "Agora minha coleção está completa."

   "Ana foi para casa e fez todas as receitas que aprendeu"
   "Chamou seus vizinhos para comer e experimentar as receitas"

   scene fundotodosfim
   with fade

   "Assim passaram uma tarde agradável e uma amizade duradoura se iniciou."
   "Fim"

   return


# Transform

transform esquerda:
   xalign 0.1
   yalign 1.0

transform direita:
   xalign 0.9
   yalign 1.0

transform meio:
   yalign 1.0

# Arco prefeito

default teminfo = False
default faloucomprefeito = False
default fimprefeito = False

label prefeito:

   if faloucomprefeito == True:
      jump prefeito2 

   scene fundoprefeito
   show prefeito at direita

   j "Olá, sou o Prefeito Jorge, você é nova na vila?"

   show anacucina at esquerda

   a "Olá! Sim, cheguei a pouco tempo."
   j "Muito bom! E o que te trás aqui?"
   a "Bem... gostaria de saber se o senhor tem alguma receita especial para me ensinar."
   j "Pensando bem, tenho sim, um rocambole de carne magnifico"
   j "Mas antes..."

   $ faloucomprefeito = True

   jump prefeito2
   

label prefeito2:
   scene fundoprefeito
   show prefeito at direita
   show anacucina at esquerda

   if not teminfo:
      show prefeito
      j "Preciso de um favor"
      j "Err... a Dona Silvia faz aniversário em breve e gostaria de preentea-la"
      j "Mas não sei bem o que dar..."
      j "Poderia descobrir do que ela gosta?"
      call screen telaprincipal
   
   if teminfo == True:
      jump prefeito3

label prefeito3:
   scene fundoprefeito
   show prefeito at direita
   show anacucina at esquerda

   if fimprefeito == True:
      jump prefeito4

   j "Vejo que já conheceu a Dona Silvia. Uma pessoa ótima!"
   j "Então consegue me ajudar..."
   menu:
      j "Qual presente a Dona Silvia iria gostar?"
      "Uma joia":
         "Pensando bem ela não é do tipo que gosta de joias."
         jump prefeito3
      "Flores":
         "É isso, ótimo, Obrigado!"
         "Está aqui a receita que prometi!"
         $ fimprefeito = True
         jump prefeito4
      "Chapéu":
         "Pensando bem ela não costuma usar muitos chapéis."
         jump prefeito3


label prefeito4:
   scene fundoprefeito
   show prefeito at direita
   show anacucina at esquerda

   j "Agora você já tem minha receita de rocambole de carne."
   j "Até mais!"

   call screen telaprincipal

# Arco Silvia

default fimsilvia = False

label silvia:

   if fimsilvia == True:
      jump silvia2

   scene fundosilvia
   show donasilvia at direita
   
   s "Olá criança, vejo que é nova na vila."
   s "meu nome é Silvia!"

   show anacucina at esquerda

   a "Olá! cheguei esses dias na vila, muito bonita e aconchegante!"
   s "Muito bem querida, espero que se sinta em casa."
   a "Obrigada! hum..."
   a "Queria fazer um pedido... a senhora tem uma receita especial para me ensinar?"
   s "Deixe eu pensar..."
   s "Tenho uma receita de Torta de maçã muito boa!"
   s "Se você me ajudar com a horta eu terei tempo de te ensinar!"
   a "Ajudo sim! Mal vejo a hora de aprender."

   "As duas foram até o quintal..."

   $ fimsilvia = True

   call screen popupvideo

image videopopup = Movie(
   play="images/anasilviavid.webm", loop=True)

screen popupvideo():
   add "fundosilvia2"

   modal True

   frame:
      xalign 0.5
      yalign 0.5
      padding (20, 20)

      vbox:
         spacing 10

         add "videopopup"

         textbutton "Fechar":
            xalign 0.5
            action Hide ("popupvideo"), Jump("silvia2")
  

label silvia2:
   scene fundosilvia
   show donasilvia at direita

   $ teminfo = True

   s "Obrigada pela ajuda!"
   s "Agora que você tem a minha receita, aproveite!"

   call screen telaprincipal

# Arco pescador

default fimpescador = False
default tentativapesca = 0

label pescador:

   if fimpescador == True:
      jump pescador3

   scene fundopescador
   show pescador at direita
   
   c "Olá moça! Veio comprar peixe fresco?"
   c "Desculpe mas acabaram todos!"
   c "Estava saindo agora para ir pescar mais..."

   show anacucina at esquerda

   a "Olá! Bem.. na verdade vim perguntar se tem alguma receita para me ensinar."
   c "Ah tenho sim! Um peixe assado maravilhoso..."
   c "Vamos venha comigo até o lago, vamos pegar um peixe bem bonito para eu te ensinar como se faz!"

   $ fimpescador = True

   jump pesca

label pesca:

   scene fundopescador2
   $ tentativa_pesca = 0

   "Clique no anzol para tentar pescar."

   call screen telapesca

   jump depoisdapesca


screen telapesca():

   imagemap:
      ground "images/fundopescador2.png"
      hotspot (1249, 950, 104, 96):
         action Jump("tentarpescar")


label tentarpescar:

   $ tentativa_pesca += 1

   if tentativa_pesca == 1:
      call screen popup_pesca("pesca1.png")
      "Que droga! é uma bota velha."
      call screen telapesca

   elif tentativa_pesca == 2:
      call screen popup_pesca("pesca2.png")
      "Humm esse peixe é muito pequeno."
      call screen telapesca

   elif tentativa_pesca == 3:
      call screen popup_pesca("pesca3.png")
      "Sim, este é ótimo! Vamos ficar com ele."
      jump depoisdapesca

screen popup_pesca(imagem):
   modal True

   frame:
      xalign 0.5
      yalign 0.5
      padding (20, 20)

      vbox:
         spacing 15

         add imagem

         textbutton "Continuar":
            xalign 0.5
            action Return()

label depoisdapesca:
   scene fundopescador
   show pescador2 at direita
   show anacucina at esquerda

   c "Viu? é assim que se faz o assado!"
   a "Ficou maravilhoso! Obrigada."

   $ fimpescador = True

   call screen telaprincipal

label pescador3:
   scene fundopescador
   show pescador at direita
   show anacucina at esquerda

   c "Aproveitando a receita que ensinei?"
   c "Até mais!"

   call screen telaprincipal

# Arco Padeiro

default fimpadeiro = False

label padeiro:

   if fimpadeiro == True:
      jump finalpadeiro

   scene fundopadeiro
   show padeiro at direita

   $ fimpadeiro = True

   p "Olá moça! Gostaria de levar alguns biscoitos? Acabaram de sair do forno!"
   a "Oi! Estão com um cheiro ótimo."
   a "Na verdade vim aqui perguntar se tem alguma receita que possa me ensinar."
   p "Gosta de pão? Posso ensinar como fazer um bem macio e saboroso."
   a "Eu amo pão, como faz?"
   p "Venha vou ensinar e você mesma faz..."

   $ acertos = 0
   $ itens_colocados = {
      "item1": False,
      "item2": False,
      "item3": False,
      "item4": False
   }
   call screen puzzle4

   return

default acertos = 0
default itens_colocados = {
   "item1": False,
   "item2": False,
   "item3": False,
   "item4": False
}

init python:
   def verificar_drop(drags, drop):
      if drop is None:
         return

      drag = drags[0]
      item = drag.drag_name

      if drop.drag_name == "cumbuca" and item in store.itens_colocados:
         if not store.itens_colocados[item]:
            store.itens_colocados[item] = True
            store.acertos += 1
            drag.draggable = False
            drag.snap(900, 420)
            renpy.restart_interaction()

screen puzzle4():
   add "mesa.png"

   text "Arraste os itens para dentro da cumbuca." xpos 50 ypos 20
   text "Acertos: [acertos]/4" xpos 50 ypos 50

   draggroup:

      drag:
         drag_name "cumbuca"
         child Fixed(
            Frame(Solid("#ffffff00"), 300, 300),
            "alvo.png")
         xpos 800
         ypos 300
         draggable False
         droppable True

      drag:
         drag_name "item1"
         child "ovo.png"
         xpos 100 ypos 500
         draggable True
         droppable False
         dragged verificar_drop

      drag:
         drag_name "item2"
         child "leite.png"
         xpos 250 ypos 500
         draggable True
         droppable False
         dragged verificar_drop

      drag:
         drag_name "item3"
         child "fermento.png"
         xpos 400 ypos 500
         draggable True
         droppable False
         dragged verificar_drop

      drag:
         drag_name "item4"
         child "farinha.png"
         xpos 550 ypos 500
         draggable True
         droppable False
         dragged verificar_drop

   if acertos == 4:
      timer 0.5 action Jump("puzzle_sucesso")

label puzzle_sucesso:

   scene fundopadeiro
   show anacucina at esquerda
   show padeiro2 at direita

   p "Olha que beleza de pão! Parabéns, você fez certinho."
   a "Adorei a receita, obrigada!"

   jump finalpadeiro

label finalpadeiro:
   scene fundopadeiro
   show anacucina at esquerda
   show padeiro at direita

   p "Aproveite a nova receita!"

   call screen telaprincipal


# Arco Louco

default fimlouco = False

label louco:
   if fimlouco == True:
      jump finallouco

   scene fundopraca
   show louco2 at direita

   l "Olá olá linda mocinha, o que te tras até essa praça sozinha?"

   show anacucina at esquerda

   a "olá! Vim te perguntar se tem alguma receita que eu possa aprender"
   l "Uma receita eu posso ensinar, se você aprender a cantar!"
   a "Cantar? como assim?"
   l "Vamos lá?!"

   $ fimlouco = True

   jump puzzle_genius


default sequencia_genius = ["vermelho", "azul", "verde", "amarelo"]
default clique_atual = 0

label puzzle_genius:
   hide louco2
   hide anacucina
   show louco3 at direita

   $ clique_atual = 0

   "Vermelho arde como o coração que insiste"
   "Azul acalma o céu onde a alma existe"
   "Verde brota em esperança tranquila e viva"
   "Amarelo sorri, luz que nunca se esquiva"
   
   call screen tela_genius
   return

init python:

   def verificar_genius(cor):
      global clique_atual
      if cor == sequencia_genius[clique_atual]:
         clique_atual += 1
         if clique_atual >= len(sequencia_genius):
            renpy.hide_screen("tela_genius")
            renpy.jump("passou_genius")
      else:
         clique_atual = 0
         renpy.notify("Errou! Tente de novo.")

screen tela_genius():

   add "fundopraca2.png"

   # Indicador de progresso
   hbox:
      xpos 500
      ypos 100
      spacing 15

      for i in range(len(sequencia_genius)):

         if i < clique_atual:
            text "✔" size 50 color "#048d04"

         else:
            text "○" size 50 color "#0c0c0c"

   imagebutton:
      idle "botaovermelho.png"
      hover im.MatrixColor("botaovermelho.png", im.matrix.brightness(0.2))
      xpos 300
      ypos 300
      action Function(verificar_genius, "vermelho")

   imagebutton:
      idle "botaoazul.png"
      hover im.MatrixColor("botaoazul.png", im.matrix.brightness(0.2))
      xpos 600
      ypos 300
      action Function(verificar_genius, "azul")

   imagebutton:
      idle "botaoverde.png"
      hover im.MatrixColor("botaoverde.png", im.matrix.brightness(0.2))
      xpos 300
      ypos 600
      action Function(verificar_genius, "verde")

   imagebutton:
      idle "botaoamarelo.png"
      hover im.MatrixColor("botaoamarelo.png", im.matrix.brightness(0.2))
      xpos 600
      ypos 600
      action Function(verificar_genius, "amarelo")

label passou_genius:

   scene fundopraca
   show louco2 at direita
   show anacucina at esquerda

   l "A receita é salada de repolho!"
   l "Espero que tenha bastante molho! "
   a "Haamm Obrigada!!"

   jump finallouco

label finallouco:
   scene fundopraca
   show louco2 at direita

   l "A receita você você aprendeu, volte sempre entendeu?"

   call screen telaprincipal