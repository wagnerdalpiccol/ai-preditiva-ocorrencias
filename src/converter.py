import json
import sys

def converter_json_para_jsonl(input_path, output_path):
    # Abre o arquivo JSON de entrada com encoding 'utf-8'
    with open(input_path, 'r', encoding='utf-8') as f_in:
        try:
            # Supondo que o JSON seja uma lista de objetos
            dados = json.load(f_in)
        except json.JSONDecodeError as e:
            print(f"Erro ao ler o arquivo JSON: {e}")
            return

    # Abre o arquivo de saída em modo de escrita com encoding 'utf-8'
    with open(output_path, 'w', encoding='utf-8') as f_out:
        # Para cada objeto na lista, escreve uma linha em formato JSONL
        for item in dados:
            # A opção ensure_ascii=False garante que os acentos não sejam escapados
            linha = json.dumps(item, ensure_ascii=False)
            f_out.write(linha + "\n")
    
    print(f"Arquivo convertido com sucesso: {output_path}")

if __name__ == "__main__":
    
    converter_json_para_jsonl("data/ocorrencias.json", "data/ocorrencias.jsonl")
