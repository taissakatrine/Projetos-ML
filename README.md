# Transfer Learning
# Projeto de Transfer Learning em Python

Este projeto consiste em aplicar o método de Transfer Learning em uma rede de Deep Learning na linguagem Python no ambiente COLAB. O objetivo é classificar imagens de gatos e cachorros usando um modelo pré-treinado.

## Descrição do Projeto

O projeto utiliza o dataset de gatos e cachorros disponível no [TensorFlow Datasets](https://www.tensorflow.org/datasets/catalog/cats_vs_dogs). O modelo pré-treinado utilizado é o MobileNetV2, que é ajustado para classificar as imagens em duas classes: gatos e cachorros.

## Estrutura do Projeto

- `notebook.ipynb`: Notebook Jupyter com o código completo do projeto.
- `cats_vs_dogs_model.h5`: Modelo treinado salvo.
- `README.md`: Este arquivo README.

## Requisitos

- Python 3.x
- TensorFlow
- TensorFlow Datasets
- Matplotlib

## Instruções

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu_usuario/seu_repositorio.git
    ```

2. Instale as dependências:
    ```bash
    pip install tensorflow tensorflow-datasets matplotlib
    ```

3. Abra o notebook no Google Colab e execute as células para treinar o modelo e fazer previsões.

## Uso

### Treinamento do Modelo

O notebook inclui o código para carregar o dataset, preparar os dados, definir o modelo de Transfer Learning, compilar e treinar o modelo. O modelo é salvo no arquivo `cats_vs_dogs_model.h5`.

### Teste do Modelo

Para testar o modelo com uma imagem específica, faça o upload da imagem para o Google Colab e execute o código para fazer a previsão. O notebook inclui um exemplo de como fazer isso.

### Envio para o GitHub

O projeto deve ser enviado para o GitHub da DIO. Use os comandos Git no terminal do COLAB para enviar o projeto:

```bash
!git init
!git remote add origin https://github.com/seu_usuario/seu_repositorio.git
!git add .
!git commit -m "Projeto de Transfer Learning"
!git push -u origin master
