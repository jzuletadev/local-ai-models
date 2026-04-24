from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.ollama import Ollama

# 1. Cargar tu proyecto
documents = SimpleDirectoryReader("C:/proyectos/mi_app").load_data()

# 2. Crear índice (memoria)
index = VectorStoreIndex.from_documents(documents)

# 3. Conectar modelo
llm = Ollama(model="gemma4:e4b")

# 4. Crear chat
query_engine = index.as_query_engine(llm=llm)

print("IA lista. Escribe 'salir' para terminar.\n")

while True:
    pregunta = input("Tú: ")

    if pregunta.lower() == "salir":
        break

    respuesta = query_engine.query(pregunta)
    print("\nIA:", respuesta, "\n")