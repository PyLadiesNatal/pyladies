Pyladies
=======
Conteúdo do Projeto feito no Hangout para as meninas do Pyladies

Como Instalar
===============
1. Clone ou Baixe esse repositório;
2. Entre na pasta do projeto, onde se encontra os códigos:
    - Caso você tenha clonado: `$ cd pyladies/pyladies_natal` 
    - Caso você tenha baixado: `$ cd pyladies-master/pyladies_natal` 
3. Certifique-se de instalar o [pip](http://www.pip-installer.org/en/latest/) caso ainda não o tenha.
4. Instale as dependências do projeto;
    - `$ sudo pip install -r requirements.txt`
5. Rode o seu projeto:
    - ```python app.py```
6. Veja ele rodando na `localhost:5000`;
    - ```http://127.0.0.1:5000```

Duvidas Comuns
===============
#### O que é: `import ipdb;ipdb.set_trace()`
O `ipdb` é um módulo instalável pelo pip: `$ pip install ipdb` ele oferece algumas coisas legais, porém é usado apenas para Depuração. É uma versão melhorada do `pdb`, nativo do Python.

#### Resolvendo: `ImportError: No module named flask_wft`
Esse erro normalmente é causando por um Módulo externo que não está instalado corretamente.
digite: `$ pip install Flask-WTF` para resolvêlo, isso normalmente funciona.
