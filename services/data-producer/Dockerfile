# 1. Imagem Base: Comece com uma imagem oficial e leve do Python.
FROM python:3.11-slim

# 2. Diretório de Trabalho: Crie um diretório dentro do contêiner para o seu app.
WORKDIR /app

# 3. Otimização de Cache: Copie *apenas* o arquivo de requisitos primeiro.
COPY requirements.txt .

# 4. Instalar Dependências: Instale as bibliotecas.
# Usamos --no-cache-dir para manter a imagem menor.
RUN python -m pip install --no-cache-dir -r requirements.txt

# 5. Copiar o Código: Agora, copie o resto do código-fonte do seu projeto.
COPY . .

# 6. Comando de Execução: Diga ao Docker como rodar seu programa.
CMD ["python", "main.py"]