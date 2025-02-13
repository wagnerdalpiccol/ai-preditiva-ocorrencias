from converter import xlsx_to_json

def main():
    xlsx_to_json("../ia-preditiva-acidentes/data/ocurrences_xlsx/1. Matriz_Ocorrências.xlsx", 
                 "../ia-preditiva-acidentes/data/ocurrences_json/caxias1_ocorrencias.json")

if __name__ == "__main__":
    main()
