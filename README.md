# OAuth Backend

Este projeto é uma API Django Rest Framework que fornece autenticação OAuth utilizando GitHub e Google. <br/>
Integrada com o repositório **getmovies-nextjs** vai oferecer uma solução completa de autenticação e autorização.

## Tecnologias Utilizadas

- **Django Rest Framework (DRF)**: Framework para criação de APIs RESTful.
- **dj-rest-auth**: Biblioteca para autenticação e gerenciamento de sessões.
- **django-allauth**: Sistema de autenticação de terceiros para Django.
- **djangorestframework-simplejwt**: Implementação de JWT (JSON Web Token) para autenticação.
- **drf-spectacular**: Gerador de esquemas OpenAPI para DRF.

## Configurações

### Criar e Ativar um Ambiente Virtual
```
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

### Instalar as Dependências
```
pip install -r requirements.txt
```

### Criar .env com variáveis de ambiente 
```
- **`GITHUB_CLIENT_ID`**
- **`GITHUB_CLIENT_SECRET`**
- **`GITHUB_CALLBACK_URL`**
- **`GOOGLE_CLIENT_ID`**
- **`GOOGLE_CLIENT_SECRET`**
- **`GOOGLE_CALLBACK_URL`**
```

### Aplicar migrações 
```
python manage.py migrate
```

### Criar superusuário 
```
python manage.py createsuperuser
```
