import pandas as pd
import json

def xlsx_to_json(xlsx_file, json_file):
    xls = pd.ExcelFile(xlsx_file)
    
    df = pd.read_excel(xls, sheet_name='Registros')
    
    df['Data'] = df['Data'].astype(str)
    
    handling_incorrect_values(df)

    data = df.to_dict(orient='records')

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def handling_incorrect_values(df):
    df['Nº'] = df['Nº'].fillna(0).replace('#REF!', 0)
    df['Contador'] = df['Contador'].fillna(0).replace('#REF!', 0)
    df['Data'] = df['Data'].fillna("").replace('#REF!', "")
    df['Mês'] = df['Mês'].fillna("").replace('#REF!', "")
    df['Matrícula'] = df['Matrícula'].fillna(0.0).replace('#REF!', 0)
    df['Nome'] = df['Nome'].fillna("").replace('#REF!', "")
    df['Sexo'] = df['Sexo'].fillna("").replace('#REF!', "")
    df['Unidade Organizacional'] = df['Unidade Organizacional'].fillna("").replace('#REF!', "")
    df['Liderança'] = df['Liderança'].fillna("").replace('#REF!', "")
    df['Turno'] = df['Turno'].fillna(0).replace('#REF!', 0)
    df['Setor da Ocorrência'] = df['Setor da Ocorrência'].fillna("").replace('#REF!', "")
    df['Descrição da Ocorrência'] = df['Descrição da Ocorrência'].fillna("").replace('#REF!', "")
    df['Tipo'] = df['Tipo'].fillna("").replace('#REF!', "")
    df['Riscos Críticos'] = df['Riscos Críticos'].fillna("").replace('#REF!', "")
    df['SIF ou PSIF'] = df['SIF ou PSIF'].fillna("").replace('#REF!', "")
    df['Agente causador'] = df['Agente causador'].fillna("").replace('#REF!', "")
    df['Parte do corpo atingida'] = df['Parte do corpo atingida'].fillna("").replace('#REF!', "")
    df['Outras partes do corpo específico'] = df['Outras partes do corpo específico'].fillna("").replace('#REF!', "")
    df['Alerta'] = df['Alerta'].fillna(0).replace('#REF!', 0)
    df['Nota QM_SAP'] = df['Nota QM_SAP'].fillna(0).replace('#REF!', 0)
    df['Dia do Mês'] = df['Dia do Mês'].fillna(0).replace('#REF!', 0)
    df['Dia da Semana'] = df['Dia da Semana'].fillna("").replace('#REF!', "")
    return df