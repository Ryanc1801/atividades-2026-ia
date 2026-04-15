import pandas as pd
import unicodedata

def normalizar(texto: str) -> str:
    texto = texto.lower().strip()
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def carregar_mapa(caminho_csv: str):
    df = pd.read_csv(caminho_csv)
    for col in ["Sintoma1", "Sintoma2", "DoencaAssociada"]:
        if col not in df.columns:
            raise ValueError(f"Coluna obrigatória ausente: {col}")
    return df

def identificar_diagnosticos(frases_txt: str, mapa_csv: str):
    mapa = carregar_mapa(mapa_csv)
    with open(frases_txt, "r", encoding="utf-8") as f:
        frases = [linha.strip() for linha in f if linha.strip()]

    resultados = []

    for frase in frases:
        frase_norm = normalizar(frase)
        sintomas_encontrados = []
        doencas = []

        for _, row in mapa.iterrows():
            sintoma1 = normalizar(str(row["Sintoma1"]))
            sintoma2 = normalizar(str(row["Sintoma2"]))
            doenca = str(row["DoencaAssociada"])

            encontrou_1 = sintoma1 in frase_norm
            encontrou_2 = sintoma2 in frase_norm

            if encontrou_1:
                sintomas_encontrados.append(row["Sintoma1"])
                doencas.append(doenca)
            if encontrou_2:
                sintomas_encontrados.append(row["Sintoma2"])
                doencas.append(doenca)

        if doencas:
            # escolhe a doença mais frequente
            diagnostico = max(set(doencas), key=doencas.count)
        else:
            diagnostico = "Sem correspondência no mapa"

        resultados.append({
            "frase": frase,
            "sintomas_identificados": ", ".join(sorted(set(sintomas_encontrados))) if sintomas_encontrados else "Nenhum",
            "diagnostico_sugerido": diagnostico
        })

    return pd.DataFrame(resultados)

if __name__ == "__main__":
    resultado = identificar_diagnosticos("frases_sintomas.txt", "mapa_conhecimento.csv")
    print("\n=== RESULTADO DA EXTRAÇÃO DE SINTOMAS ===\n")
    print(resultado.to_string(index=False))
    resultado.to_csv("resultado_diagnosticos.csv", index=False, encoding="utf-8-sig")
    print("\nArquivo 'resultado_diagnosticos.csv' gerado com sucesso.")