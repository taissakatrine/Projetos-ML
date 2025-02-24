# 🛍️ Sistema de Recomendação por Imagens - Transfer Learning com MobileNetV2 🖼️

**Python TensorFlow License**

Sistema de recomendação baseado em similaridade visual entre imagens. Este projeto demonstra como utilizar modelos pré-treinados, como o MobileNetV2, para extrair características visuais de produtos e recomendar itens similares com base na aparência física (cor, formato, textura, etc.).

## 📋 Índice
1. [Visão Geral](#🌟-visão-geral)
2. [Dataset](#📊-dataset)
3. [Requisitos](#💻-requisitos)
4. [Instalação](#🔧-instalação)
5. [Uso](#🚀-uso)
6. [Treinamento](#🏋️‍♂️-treinamento)
7. [Estrutura do Projeto](#📂-estrutura-do-projeto)
8. [Contribuições](#🤝-contribuições)
9. [Licença](#📜-licença)
10. [Reconhecimentos](#🙏-reconhecimentos)

## 🌟 Visão Geral
O objetivo deste projeto é criar um sistema de recomendação que sugira produtos semelhantes com base em sua aparência visual. Utilizamos:

- **MobileNetV2**: Um modelo leve e eficiente pré-treinado no ImageNet.
- **Extração de Características**: Para capturar informações visuais complexas das imagens.
- **Algoritmo Nearest Neighbors**: Para encontrar os produtos mais similares com base nas características extraídas.

## 📊 Dataset
O dataset utilizado é o **Fashion MNIST**, disponível no [TensorFlow Datasets](https://www.tensorflow.org/datasets). Ele contém 70.000 imagens em escala de cinza de produtos de moda, como camisetas, sapatos, bolsas, etc. O dataset foi dividido da seguinte forma:

- **Treinamento**: 1.000 imagens (subconjunto reduzido para testes rápidos).
- **Teste**: 200 imagens (subconjunto reduzido para testes rápidos).

As imagens são redimensionadas para 32x32 pixels inicialmente e posteriormente para 224x224 pixels (entrada do MobileNetV2). Além disso, as imagens são normalizadas para o intervalo [0, 1] e convertidas para RGB antes do processamento.

## 💻 Requisitos
Para executar este projeto, você precisa dos seguintes pacotes:

- Python 3.8+
- TensorFlow 2.x
- Matplotlib
- NumPy
- Scikit-Learn

Instale as dependências com o comando abaixo:

```bash
pip install tensorflow keras numpy matplotlib scikit-learn
```
## 🔧 Instalação
Clone o repositório e instale as dependências:
```bash
git clone https://github.com/seu-usuario/image-similarity-recommendation.git
cd image-similarity-recommendation
pip install -r requirements.txt
```
## 🚀 Uso
Treinamento e Avaliação
Abra o notebook notebooks/image_similarity_recommendation.ipynb em seu ambiente Jupyter ou Google Colab para treinar e avaliar o modelo.

Teste com Imagens Externas
Você pode usar a função recommend_similar_products para testar o modelo com suas próprias imagens:
```bash
from google.colab import files
from predict import recommend_similar_products

# Upload de uma imagem personalizada
uploaded = files.upload()
file_name = list(uploaded.keys())[0]

# Carregando e processando a imagem
img = image.load_img(file_name, target_size=(32, 32), color_mode='grayscale')
img_array = image.img_to_array(img) / 255.0

# Recomendando produtos similares
recommend_similar_products(img_array)
```
## 🏋️‍♂️ Treinamento
O treinamento é dividido nas seguintes etapas:

Extração de Características:

As imagens são processadas pelo MobileNetV2 para extrair características visuais.

Modelo de Similaridade:

O algoritmo Nearest Neighbors é treinado com as características extraídas para encontrar os produtos mais similares.

📂 Estrutura do Projeto
```bash
image-similarity-recommendation/
├── notebooks/                  # Notebooks Jupyter com código detalhado
│   └── image_similarity_recommendation.ipynb
├── data/                       # Dados baixados automaticamente pelo TensorFlow Datasets
├── models/                     # Modelos salvos (opcional)
│   └── nearest_neighbors_model.pkl
├── scripts/                    # Scripts utilitários
│   └── predict.py              # Função de recomendação para imagens externas
├── assets/                     # Imagens usadas nos tutoriais
├── requirements.txt            # Lista de dependências
└── README.md                   # Este arquivo
```
## 🤝 Contribuições
Contribuições são bem-vindas! Siga os passos abaixo:

Faça um fork deste repositório.

Crie uma branch para sua contribuição: git checkout -b feature/nova-funcionalidade.

Envie um pull request detalhando suas alterações.

## 📜 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🙏 Reconhecimentos
TensorFlow Team: Pela disponibilização do dataset Fashion MNIST e do framework TensorFlow.

Autores do MobileNetV2: Pelo excelente modelo pré-treinado.

Comunidade Open Source: Por fornecer ferramentas e recursos que facilitam o desenvolvimento de projetos de IA.

## 🌐 Links Úteis
TensorFlow Documentation

MobileNetV2 Paper

Fashion MNIST Dataset
