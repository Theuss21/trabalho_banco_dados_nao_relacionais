from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017/")
db = client["banco_simulado"]
colecao = db["documentos"]

def create_document(dados):
    resultado = colecao.insert_one(dados)
    return str(resultado.inserted_id)

def read_documents():
    documentos = []
    for doc in colecao.find():
        doc['_id'] = str(doc['_id'])
        documentos.append(doc)
    return documentos


def update_document(_id, novos_dados):
    resultado = colecao.update_one({"_id": ObjectId(_id)}, {"$set": novos_dados})
    return resultado.modified_count > 0

def delete_document(_id):
    resultado = colecao.delete_one({"_id": ObjectId(_id)})
    return resultado.deleted_count > 0

def limpar_banco():
    colecao.delete_many({})

def main():
    print("\n--- CRUD COM PyMongo E MONGODB REAL ---")

    limpar_banco()

    id1 = create_document({"nome": "Ana", "idade": 20})
    id2 = create_document({"nome": "Carlos", "idade": 28})
    print(f"\nCriado documento com ID: {id1}")
    print(f"Criado documento com ID: {id2}")

    print("\n📄 Documentos cadastrados:")
    for doc in read_documents():
        print(doc)

    print(f"\n🔄 Atualizando idade do ID {id1} para 21...")
    if update_document(id1, {"idade": 21}):
        print("Atualizado com sucesso!")

    print(f"\n❌ Deletando documento com ID: {id2}...")
    if delete_document(id2):
        print("Removido com sucesso!")

    print("\n📄 Documentos restantes após UPDATE e DELETE:")
    for doc in read_documents():
        print(doc)

if __name__ == "__main__":
    main()