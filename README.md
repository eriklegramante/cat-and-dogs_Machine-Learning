# 🐶🐱 Classificação de Imagens — Cães vs Gatos com TensorFlow

## 📌 Descrição do Projeto
Este projeto tem como objetivo desenvolver um **classificador binário de imagens** capaz de distinguir entre **cães e gatos**, utilizando **Redes Neurais Convolucionais (CNNs)** com **TensorFlow/Keras**.

O foco do projeto está na **compreensão do pipeline completo de Machine Learning**, incluindo organização de dados, treinamento de modelos, experimentação controlada e análise crítica de resultados, seguindo boas práticas utilizadas no mercado.

---

## 📂 Dataset
- Total de imagens: **25.000**
  - 12.500 imagens de cães  
  - 12.500 imagens de gatos
- Estrutura de pastas:
  - `train/`
  - `val/`
  - `test/`

A separação foi feita de forma balanceada para evitar viés entre as classes.

---

## 🧠 Arquitetura do Modelo
- **Transfer Learning** com `MobileNetV2`
- Camadas convolucionais pré-treinadas congeladas
- Camadas densas adicionadas para classificação binária
- Função de ativação final: `sigmoid`
- Função de perda: `binary_crossentropy`
- Otimizador: `Adam`

Essa abordagem permite um treinamento eficiente mesmo com um grande volume de imagens.

---

## 🧪 Experimentos Realizados

### 🔹 Experimento 1 — Baseline
- Modelo base sem Data Augmentation
- Learning rate padrão do otimizador
- Objetivo: estabelecer um ponto de referência inicial

**Resultado:**  
Alta acurácia e rápida convergência, indicando que o problema é bem separável para CNNs modernas.

---

### 🔹 Experimento 2 — Data Augmentation
- Aplicação de transformações artificiais (rotações, zoom, flips)
- Objetivo: melhorar a capacidade de generalização do modelo

**Resultado:**  
Acurácia elevada com maior robustez, reduzindo o risco de overfitting e tornando o modelo mais adequado para dados reais.

---

## 📊 Registro de Resultados
Os resultados de cada experimento foram registrados em arquivos **CSV**, contendo:
- Loss
- Accuracy de validação
- Configurações utilizadas
- Descrição da modificação aplicada

Essa prática facilita a comparação entre experimentos e garante rastreabilidade.

---

## 🏆 Conclusão
Apesar do baseline apresentar excelente desempenho, o **modelo com Data Augmentation demonstrou melhor equilíbrio entre desempenho e capacidade de generalização**, sendo mais adequado para cenários reais de aplicação.

O projeto evidencia a importância de testar hipóteses de forma controlada e interpretar métricas além da acurácia isolada.

---

## 🚀 Tecnologias Utilizadas
- Python  
- TensorFlow / Keras  
- NumPy  
- Pandas  
- Jupyter Notebook  

---

## 📌 Possíveis Extensões
- Fine-tuning das camadas convolucionais
- Matriz de confusão
- Análise de falsos positivos e falsos negativos
- Exportação do modelo para produção

---

## 👤 Autor
Projeto desenvolvido com foco educacional e preparação para o mercado de trabalho em **Machine Learning e Visão Computacional**.
