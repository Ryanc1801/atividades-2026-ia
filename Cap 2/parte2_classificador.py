import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def treinar_classificador(caminho_csv: str):
    df = pd.read_csv(caminho_csv)

    X = df["frase"]
    y = df["situacao"]

    X_treino, X_teste, y_treino, y_teste = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    modelo = Pipeline([
        ("tfidf", TfidfVectorizer(lowercase=True, ngram_range=(1, 2))),
        ("clf", LogisticRegression(max_iter=1000))
    ])

    modelo.fit(X_treino, y_treino)
    previsoes = modelo.predict(X_teste)

    acc = accuracy_score(y_teste, previsoes)
    matriz = confusion_matrix(y_teste, previsoes, labels=["alto risco", "baixo risco"])
    relatorio = classification_report(y_teste, previsoes)

    return modelo, acc, matriz, relatorio, X_teste, y_teste, previsoes

if __name__ == "__main__":
    modelo, acc, matriz, relatorio, X_teste, y_teste, previsoes = treinar_classificador("dataset_risco.csv")

    print("\n=== AVALIAÇÃO DO CLASSIFICADOR ===\n")
    print(f"Acurácia: {acc:.2f}")
    print("\nMatriz de confusão:")
    print(matriz)
    print("\nRelatório de classificação:")
    print(relatorio)

    exemplos = [
        "dor no peito com suor frio",
        "leve desconforto nas costas depois do trabalho",
        "falta de ar e cansaço intenso"
    ]

    print("\n=== TESTE COM NOVAS FRASES ===\n")
    for frase, pred in zip(exemplos, modelo.predict(exemplos)):
        print(f"Frase: {frase} -> Predição: {pred}")