# trabalho_banco_dados_nao_relacionais

✅ README.md

# CRUD com Python e MongoDB usando PyMongo

Este projeto é uma simulação de um sistema CRUD (Create, Read, Update, Delete) utilizando Python com a biblioteca `pymongo` para interação com um banco de dados MongoDB real.

---

## 📦 Requisitos

- Python 3.7 ou superior
- MongoDB instalado localmente ou rodando via Docker
- Biblioteca PyMongo

### 📥 Instalando dependências

Use o comando abaixo para instalar o `pymongo`:

```bash
pip install pymongo


🛠️ Estrutura do projeto
.
├── app.py           # Arquivo principal com as operações CRUD
└── README.md        # Este arquivo de explicação


⚙️ Como executar

🔹 1. Certifique-se de que o MongoDB está rodando localmente

Por padrão, o código tenta se conectar à URI:
mongodb://localhost:27017/

Se estiver usando Docker, você pode iniciar o MongoDB com:
docker run -d -p 27017:27017 --name mongo mongo

🔹 2. Execute o script Python
python app.py


🔁 Operações CRUD disponíveis

Create: insere novos documentos na coleção

Read: lista todos os documentos

Update: atualiza documentos pelo _id

Delete: remove documentos pelo _id

🧪 Exemplo de saída no terminal

--- CRUD COM PyMongo E MONGODB REAL ---

Criado documento com ID: 64fabc123abc456def789000
Criado documento com ID: 64fabc123abc456def789001

📄 Documentos cadastrados:
{'_id': '64fabc123abc456def789000', 'nome': 'Ana', 'idade': 20}
{'_id': '64fabc123abc456def789001', 'nome': 'Carlos', 'idade': 28}

🔄 Atualizando idade do ID 64fabc123abc456def789000 para 21...
Atualizado com sucesso!

❌ Deletando documento com ID: 64fabc123abc456def789001...
Removido com sucesso!

📄 Documentos restantes após UPDATE e DELETE:
{'_id': '64fabc123abc456def789000', 'nome': 'Ana', 'idade': 21}


🗂️ Estrutura no MongoDB

Banco de dados: banco_simulado

Coleção: documentos

Cada documento possui os campos: nome, idade, e _id (gerado automaticamente)


📚 Tecnologias utilizadas

Python 3

PyMongo

MongoDB (local ou Docker)


✅ Autor

Este projeto foi desenvolvido para fins educacionais, com foco em praticar operações de CRUD utilizando banco de dados NoSQL com Python.
