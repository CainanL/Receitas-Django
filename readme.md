o que são cada arquivos existente;
    - .mypy_cash -> vem do mypy, cash do mypy
    - venv -> ambiente virtual
    - settings.py -> arquivo de configurações do django
    - asgi.py / wsgi.py -> para fazer configurações em servidores externos

iniciar projeto django 
    - django-admin startproject PROJETO .

criar app
    - python manage.py startapp nome_do_app

coletar arquivos estaticos
    - python manage.py collectstatic
    - serve para coletar arquivos estaticos
    - é necessário configurar o statichoot -> caminho da pasta onde quero que salve todos os arquivos de minha aplicação

    - criar static rook
      - no seeting, criar uma variável "STATIC_ROOT = BASEDIR / '"