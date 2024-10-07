# Django Project with Docker

Este é um projeto Django simples, configurado para rodar com Docker. A aplicação está configurada para rodar na porta `8000` e pode ser acessada em `http://localhost:8000` após o build e execução dos serviços via Docker.

## Requisitos

- Docker
- Docker Compose

## Instruções para Buildar e Rodar o Projeto com Docker

1. Clone este repositório:
   ```bash
   git clone https://github.com/danieldiasbarbo/kanastra
   cd kanastra
   ```

2. Execute o Docker Compose para criar a imagem, instalar as dependências e rodar o servidor:
   ```bash
   docker-compose up --build
   ```

   Isso irá:
   - Criar o container do Django.
   - Instalar as dependências do projeto.
   - Aplicar as migrações necessárias.
   - Rodar o servidor Django na porta `8000`.

   Acesse o servidor em: [http://localhost:8000](http://localhost:8000)

## Executando Localmente com Virtualenv

Se você deseja rodar o projeto localmente sem Docker, siga os passos abaixo:

1. Instale um ambiente virtual:
   ```bash
   python -m venv venv
   ```

2. Ative o ambiente virtual:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

3. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplique as migrações:
   ```bash
   python manage.py migrate
   ```

5. Execute o servidor Django:
   ```bash
   python manage.py runserver
   ```

   Agora, o servidor estará disponível em [http://localhost:8000](http://localhost:8000).

## Environment Variables (Variáveis de Ambiente)

Embora este projeto não utilize variáveis de ambiente por padrão, você pode configurá-las facilmente. Para isso, crie um arquivo `.env` na raiz do projeto e defina suas variáveis conforme necessário.

Por exemplo:
```env
DJANGO_DEBUG=True
SECRET_KEY=seu-segredo-aqui
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

O Docker pode ser configurado para carregar essas variáveis automaticamente usando o arquivo `.env`.

## Como Testar a API

Este projeto inclui um endpoint para upload de arquivos CSV via uma requisição `POST`. Para testar, faça o seguinte:

1. Faça uma requisição `POST` para o endpoint correspondente com o `Content-Type` configurado como `multipart/form-data`.
2. Inclua uma chave chamada `"file"` e envie o arquivo `.csv` em formato binário.

Exemplo de `curl`:

```bash
curl -X POST -F "file=@caminho/para/seu/arquivo.csv" http://localhost:8000/charge/csv
```

## Executando Testes

Para rodar os testes do projeto, execute:

```bash
python manage.py test
```

Isso executará todos os testes definidos no projeto.