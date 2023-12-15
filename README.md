# SEND-USER-TO-POSTGRES

Modelo de API em Cloud [Run](https://cloud.google.com/run?hl=pt-BR) para enviar dados de um modelo de usuário para um banco [PostgreSQL](https://www.postgresql.org/).


## Linguagem
Essa aplicação utiliza como linguagem o [Python 3.9](https://www.python.org/).


### Configuração prévia
Inicialmente, será necessário um banco PostgreSQL em funcionamento que aceite conexões externas. Para instalar e configurar o banco, leia a [documentação](https://www.postgresql.org/docs/current/tutorial-install.html).


Com o banco funcionando, altere a linha 11 do Dockerfile, colocando as informações necessárias para conectar com o banco, de acordo com a configuração feita por você.


### Build e Run do Container

Para buildar uma imagem Docker e em seguida subir um Container, execute os seguintes comandos:


1. docker build -t sendtopostgres .
2. docker run -d --name sendtopostgres -p 80:80 sendtopostgres


Com isso, você terá uma imagem Docker em funcionamento:


<p align="center">
<img src="https://uploaddeimagens.com.br/images/004/691/366/original/containerfuncionando.png">
</p>


E ao acessar o endpoint "/docs", verá a seguinte página:


<p align="center">
<img src="https://uploaddeimagens.com.br/images/004/691/368/original/printdoswagger.png">
</p>
