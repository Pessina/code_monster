# Controlando o ESP/IoT através de comandos de voz

O objetivo deste projeto é controlar um módulo ESP (ou similares) através de comandos de voz.
Como protótipo do nosso conceito, focaremos na task simples de acender e apagar um led acoplado ao módulo.

## Natural Language Processing

Natural Language Processing (NLP) é o campo da computação que estuda o reconhecimento e processamento de linguagem natural.
Em outras palavras, dado um comando por voz, um algoritmo de NLP deve ser capaz de interpretar a inteção do usuário e realizar a ação correspondente.

Para o escopo do nosso projeto infelizmente não temos tempo o suficiente para estudar técnicas avançadas nem tempo o suficiente para implementar o nosso próprio serviço de NLP, dado a complexidade que esse tipo de infraestrutura exige.

Por esta razão **optamos por utilizar o serviço de NLP integrado à Google Assistente**

## Google Assistente

A Google Assistente é um serviço que, como o nome sugere, tem como objetivo oferecer funcionalidades que auxiliem o usuário em tarefas rotineiras.
Dentre estas tarefas está **o controle de dispositivos IoT**.

Com comandos como _"acender luz da sala"_ o usuário é capaz de controlar a iluminação de ambientes ou desligar e ligar a TV sem a necessidade de interação física com interruptores.

Felizmente este serviço **permite a integração com serviços de terceiros** sendo assim ideal para o nosso protótipo.

A questão então é **como fazer uso do sistema de NLP da Google Assistente para controlar o módulo ESP?**

Para isso faremos uso da plataforma IFTTT.

## Criando ações para a Google Assistente

### Breve introdução sobre o IFTTT

A plataforma IFTTT (if this than that) nos permite criar ações em respostas à triggers de diversos serviços através dos chamados **applets**.

Um applet é formado por um trigger e uma ação correspondente.

No nosso caso, o trigger será **Google Assistente ouvir a frase _turn light on_**, como podemos ver na imagem que segue:

![Alt text](images/ifttt_trigger.png)
