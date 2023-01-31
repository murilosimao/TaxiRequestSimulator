<h1 align="center">TAXI app BackEnd simulator</h1>

<br>

## :dart: Sobre ##

A ideia é simular uma aplicativo de carona com mensageria, onde temos varios clientes e varios taxistas. Cada cliente tem seu gosto e cada taxista tem sua caracteristica.

## :sparkles: Features ##

:heavy_check_mark: RabbitMQ - Mensageria\
:heavy_check_mark: Docker - Utilizado para escalar

## :rocket: Tecnologias ##

The following tools were used in this project:

- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Pika](https://pika.readthedocs.io/en/stable/)


## :checkered_flag: Iniciando ##

```bash
# Rode o container
$ docker-compose up --scale producer=10 --scale consumer1=20
```

## :memo:  ##

Made with :heart: by <a href="https://github.com/murilosimao" target="_blank">MuriloSimão</a>

&#xa0;

<a href="#top">Ir para o ínicio</a>
