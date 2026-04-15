# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# FASE 1 - CAP 1 -2026

## MAVI (Medical Assistance Virtual)

## 👨‍🎓 Integrantes: 
- <a href="www.linkedin.com/in/vinicius-santana-97a9b54a">Vinícius Pereira Santana 1</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Vitor Augusto Prado Guisso 2</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Caique Nonato da Silva Bezerra</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">Andre Godoi Chiovato</a>

### Link para o banco de imagens:
- <a href="https://drive.google.com/drive/folders/10XfEQaJWGqeGNbswBUARRGu5X6W8Mboe?usp=drive_link">Banco de Imagens</a>


## 📜 Descrição

*Este repositório foi desenvolvido para fins acadêmicos, integrando três pilares fundamentais da IA na saúde: Dados Numéricos (IoT), Processamento de Linguagem Natural (NLP) e Visão Computacional (VC). O objetivo é criar uma base de dados multimodal para o estudo de doenças cardiovasculares.

Objetivos do Projeto;

Consolidar um dataset estruturado para predição de risco cardíaco.

Explorar textos clínicos e científicos para extração de entidades e sintomas.;

Reunir um banco de imagens diagnósticas para treinamento de algoritmos de detecção de anomalias.  *

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: Aqui estão presentes os arquivos relacionados ao dataset heart.csv pertinentes a atividade.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: Aqui estão os textos Hipertensão (pressão alta) e artigo de estatísticas cardiovascular

- <b>scripts</b>: Aqui serão localizados os arquivos de schema.sql de criação de tabelas, o arquivo load_data.sql para carregamentos.

- <b>src</b>: Aqui serão localizado a pasta nova com os arquivos contendo o código fonte do sistema.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Requisitos

*

🔢 Parte 1: Dados Numéricos (IoT e Sensores)

Descrição dos Dados

O dataset contém 1026 registros de pacientes com variáveis clínicas fundamentais. Os dados são simulados com base em padrões reais do UCI Heart Disease Dataset.
Variável	Descrição Clínica	Relevância para IA
Idade/Sexo	Perfil demográfico	Identifica grupos de risco epidemiológico.
Pressão Arterial	Medição sistólica em repouso	Variável crítica para predição de hipertensão e AVC.
Colesterol	Nível de colesterol sérico	Essencial para modelos de cálculo de aterosclerose.
Frequência Cardíaca	Batimentos por minuto (Máx)	Indicador de esforço e saúde do miocárdio.

Justificativa: Estas variáveis são os "inputs" primários para algoritmos de classificação (como Random Forest ou SVM) que conseguem prever a probabilidade de um evento cardíaco com alta precisão.

🔤 Parte 2: Dados Textuais (NLP)

Localização: Arquivos disponíveis na pasta /assets (ou /docs) deste repositório.
Fontes dos Textos

    Texto 1: Estatística Cardiovascular – Brasil 2020 (Fonte: SciELO/Sociedade Brasileira de Cardiologia).

    Texto 2: Guia de Hipertensão Arterial (Fonte: Ministério da Saúde/SUS).

Potencial de Exploração via NLP

    Extração de Sintomas: Algoritmos podem mapear termos como "angina", "dispneia" e "síncope" para automatizar a triagem.

    Análise de Tópicos: Classificar se o texto trata de prevenção, diagnóstico ou tratamento farmacológico.

    Reconhecimento de Entidades Nomeadas (NER): Identificar dosagens de medicamentos e valores de pressão arterial mencionados em textos não estruturados.

🖼️ Parte 3: Dados Visuais (Visão Computacional)

Link para o Banco de Imagens: https://drive.google.com/drive/folders/10XfEQaJWGqeGNbswBUARRGu5X6W8Mboe?usp=drive_link

Detalhes do Dataset Visual

Contém 10.000 imagens de Raio-X de Tórax / ECG em formato .jpg/.png, focadas em diagnósticos cardiológicos.
Justificativa e Análise de IA

O uso de Visão Computacional (Redes Neurais Convolucionais - CNNs) nestas imagens permite:

    Segmentação de Órgãos: Delimitar o tamanho do coração para calcular o índice cardiotorácico (detecção de Cardiomegalia).

    Identificação de Padrões: No caso de ECGs, identificar arritmias através da análise da morfologia das ondas P, QRS e T.

    Reconhecimento de Anomalias: Filtrar exames normais de exames que apresentam sinais de congestão ou calcificações vasculares.

*

## 🗃 Histórico de lançamentos

* 0.1.0 - 10/03/2026
    * 

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

