from copilot import Copilot
import time
import os
from dotenv import load_dotenv

# Define sua chave de API (assegure-se de tê-la configurada na variável de ambiente)

load_dotenv()

client = Copilot(api_key=os.getenv("COPILOT_API_KEY"))

def upload_file(file_path):
    """
    Faz o upload do arquivo para o Copilot e retorna o id do arquivo.
    """
    with open(file_path, "rb") as f:
        response = client.files.create(
            file=f,
            purpose='fine-tune'
        )
    print("Upload concluído. ID do arquivo:", response.id)
    return response.id

def start_fine_tune(training_file_id):
    """
    Inicia o treinamento (fine-tuning) utilizando o id do arquivo.
    Retorna o id do job de fine-tuning.
    """
    response = client.fine_tuning.jobs.create(
        training_file=training_file_id,
        model="copilot-turbo"  # Altere para o modelo desejado
    )

    print("Job de fine-tuning iniciado. ID do job:", response.id)
    return response.id

def check_fine_tune_status(job_id, poll_interval=60):
    """
    Verifica periodicamente o status do treinamento a cada `poll_interval` segundos.
    Quando o status for "succeeded", retorna as informações completas do job.
    """
    while True:
        # Recupera os detalhes do job de fine-tuning
        response = client.FineTune.retrieve(id=job_id)
        status = response.status
        print("Status atual do treinamento:", status)
        
        if status == "succeeded":
            # Quando concluído, retorna o objeto de resposta completo
            return response
        
        # Aguardar alguns segundos antes de nova verificação
        time.sleep(poll_interval)

def main():
    # Caminho para o arquivo de dados
    file_path = "data/ocorrencias.jsonl"
    
    # Passo 1: Upload do arquivo
    file_id = upload_file(file_path)
    
    # Passo 2: Iniciar o treinamento passando o id do arquivo
    job_id = start_fine_tune(file_id)
    
    # Passo 3: Verificar periodicamente o status do treinamento
    print("Aguardando a conclusão do treinamento...")
    final_response = check_fine_tune_status(job_id)
    
    # Passo 4: Quando concluído, imprime as informações completas e o nome do modelo fine-tuned
    print("Treinamento concluído com sucesso!")
    print("Informações completas do job:")
    print(final_response)
    
    # Extraindo o nome do modelo fine-tuned (caso esteja disponível)
    model_name = final_response.get("fine_tuned_model")
    if model_name:
        print("Nome do modelo fine-tuned:", model_name)
    else:
        print("O nome do modelo fine-tuned ainda não foi disponibilizado na resposta.")

if __name__ == "__main__":
    main()
