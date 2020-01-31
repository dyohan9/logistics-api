# Sistema de Entrega de Mercadorias - Grupo BR

[![Python Version](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/)


Para começar, agradeço muito a oportunidade que me foi dado para fazer esse teste, foi uma experiência muito boa e bastante desafiador, de cara quando comecei a ler o teste, comecei a perceber que o problema poderia ser resolvido com GRAFO, logo comecei a pesquisar para tentar encontrar a melhor solução para essa abordagem, foi quando lembrei do algoritmo <b>Dijkstra</b>, foi ai que comecei a pesquisar soluções que pudessem me auxiliar nesse processo, encontrei várias soluções, porém nenhuma servia para o meu problema, foi quando acabei encontrando uma que foi desenvolvido pelo usuário <b>vglinden</b>, a partir disso comecei a desenvolver o backend, como atualmente trabalho, somente tive tempo disponível na parte da noite, mesmo assim entrego esse projeto com testes e documentação.

Eu queria poder colocar o <b>Travis-CI</b> e o <b>Coveralls</b>, porém como o repositório é privado, os serviços são gratuitos somente para open-source.

Disponibilizei a documentação do backend com <b>Swagger</b> e também um arquivo dump do <b>Postman</b>.


## Documentação Endpoint
| # | Endpoint/Arquivo |
|--|--|
| Swagger | [*Produção*](http://localhost/) ou [*Desenvolvimento*](http://localhost:8000/)
| Postman | [*Clique Aqui*](https://github.com/dyohan9/TestGrupoBR/blob/master/Sistema.postman_collection.json)


## Desenvolvimento

Use o comando ```make``` para ```check_environment```, ```install_requirements```, ```lint```, ```test```, ```migrate```, ```start```, ```migrations``` and ```collectstatic```.

| Command | Description |
|--|--|
| make help | Mostrar todos os comandos disponíveis
| make check_environment | Verifique se todas as dependências foram instaladas
| make install_requirements | Instalar dependências pip
| make lint | Verificar e mostrar avisos e erros
| make test | Execute testes de unidade e mostre o relatório de cobertura
| make migrate | Atualizar schema e aplicar migrações no banco de dados
| make start | Iniciar servidor de desenvolvimento
| make migrations | Criar arquivos de migração
| make collectstatic | Gerar os arquivos estáticos em ```STATIC_ROOT```


## Produção

### Requisitos:
| # | Versão |
|--|--|
| Docker | >=18.x.x
| Docker-Compose | >=1.20.x

#### Docker
Para gerar a construção da imagem, utilize o seguinte comando:
```docker-compose build```
Após a geração da imagem, você pode executar o comando 
```docker-compose up -d```
dessa forma você vai rodar toda stack do projeto, banco de dados PostgreSQL, Celery, Redis e o próprio projeto.

Lembre-se de deixar <b>disponível a porta 80</b> em sua máquina para executar o projeto.


## Variáveis de Ambiente

Você pode definir variáveis de ambiente no seu sistema operacional, gravar no arquivo ```.env``` ou passar pela configuração do Docker.

| Variável | Tipo | Padrão | Descrição |
|--|--|--|--|
| SECRET_KEY | ```string```|  ```None``` | Uma chave secreta para uma instalação específica do Django. Isso é usado para fornecer assinatura criptográfica e deve ser definido como um valor único e imprevisível.
| DEBUG | ```boolean``` | ```False``` | Um booleano que ativa / desativa o modo de depuração.
| ALLOWED_HOSTS | ```string``` | ```*``` | Uma lista de strings representando os nomes de host/domínio que este site do Django pode servir.
| DEFAULT_DATABASE | ```string``` | ```sqlite:///db.sqlite3``` | Leia a documentação [dj-database-url](https://github.com/kennethreitz/dj-database-url) para configurar a conexão com o banco de dados.
| LANGUAGE_CODE | ```string``` | ```en-us``` | Uma sequência que representa o código do idioma para esta instalação. Isso deve estar no padrão [language ID format](https://docs.djangoproject.com/en/2.0/topics/i18n/#term-language-code).
| TIME_ZONE | ```string``` | ```UTC``` | Uma sequência que representa o fuso horário para esta instalação. Veja o [list of time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
| STATIC_URL | ```string``` | ```/static/``` | URL a ser usada ao se referir a arquivos estáticos localizados em ```STATIC_ROOT```.
| CSRF_COOKIE_DOMAIN | ```string``` | ```None``` | O domínio a ser usado ao definir o cookie CSRF.
| CSRF_COOKIE_SECURE | ```boolean``` | ```False``` | Se você deseja usar um cookie seguro para o cookie CSRF.
| CELERY_BROKER_URL | ```string```  | ``` redis://localhost:6379/0 ``` | URL do Celery Broker, verifique as instruções de uso no Celery Docs.
| BACKEND_EXPORT | ```string```  | ``` 80 ``` | Porta exposta do backend. | 


## Agradecimento

O desenvolvimento desse projeto não seria possível sem o algoritmo [*Dijkstra*](https://github.com/vglinden/Dijkstra).
