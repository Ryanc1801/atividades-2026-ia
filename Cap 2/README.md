# CardioIA - Fase 2  
Diagnóstico Automatizado com Inteligência Artificial

## 📌 Descrição do Projeto

Este projeto tem como objetivo simular um sistema de apoio ao diagnóstico médico utilizando Inteligência Artificial.

A solução foi dividida em duas partes:

- Parte 1: Extração de sintomas a partir de textos e sugestão de diagnóstico
- Parte 2: Classificação de risco com Machine Learning

---

## 🧠 Tecnologias Utilizadas

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Jupyter Notebook

---

## 📂 Estrutura do Projeto

- frases_sintomas.txt  
- mapa_conhecimento.csv  
- dataset_risco.csv  
- parte1_extracao.py  
- parte2_classificador.py  
- resultado_diagnosticos.csv  
- cardioia_fase2.ipynb  

---

## 🔍 Parte 1 - Extração de Sintomas

O sistema:
- Lê frases de pacientes (.txt)
- Identifica sintomas
- Sugere diagnósticos com base no mapa

Saída:
resultado_diagnosticos.csv

---

## 🤖 Parte 2 - Classificador de Risco

Classifica frases como:
- Alto risco
- Baixo risco

Processo:
- TF-IDF
- Logistic Regression
- Avaliação com:
  - Acurácia
  - Matriz de confusão
  - Relatório de classificação

---

## ⚠️ Observações

O dataset é simulado e pode conter vieses. Em cenários reais, seria necessário:

- Mais dados
- Melhor balanceamento
- Validação médica

---

## ▶️ Como Executar

Instalar dependências:
pip install pandas scikit-learn

Executar:
python parte1_extracao.py
python parte2_classificador.py

Ou abrir:
cardioia_fase2.ipynb

---

## 🎥 Vídeo

https://youtu.be/qJRQuNxWsuY

---


---

## 📌 Conclusão

O projeto demonstra como técnicas simples de IA podem simular sistemas reais de apoio ao diagnóstico.
