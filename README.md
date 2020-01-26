# Sistema de Entrega de Mercadorias - Grupo BR

[![Python Version](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/)


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
| CSRF_COOKIE_SECURE | ```boolean``` | ```False``` | Se você deseja usar um cookie seguro para o cookie CSRF. | 
