# -*- coding: utf-8 -*-
"""Dani_workshopHandsOn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xPF_gryeergW_m_zSo1Qr0qaWd5PBM3J

**Montando drive do google localmente**
"""

from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)

#pip list #checando pacotes instalados e suas verções

#lact / proc/

import os #Módulos OS em python #Uma maneira simples de usar funcionalidades que são depe

"""Listando as pastas existentes em meu drive"""

path = "/content/gdrive/My Drive"
dirs = os.listdir (path)
for file in dirs:
  print(file)

"""Listando o arquivo que contém na minha pasta aws"""

os.listdir("/content/gdrive/My Drive/fotos workshop")

"""Criando a API de configuração

"""

!mkdir -p ~/.aws &&\
  cp /content/gdrive/My\ Drive/fotos\ workshop/credentials ~/.aws/credentials

!pip install boto3

"""importando  bibliotecas"""

import boto3 #https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
from PIL import Image #Python Pillow trabalha com largura e altura de imagens #https://pillow.readthedocs.io/en/stable/
from io import BytesIO

"""Iniciando a SESSÃO COM O BOTO3"""

session =  boto3.Session (region_name="us-east-1")

"""Iniciando recoginition"""

client = boto3.client('rekognition', 
                      region_name = 'us-east-1')

"""Defininindo função para leitura das imagens do drive"""

def get_image(image):
  return Image.open(f'/content/gdrive/My Drive/fotos workshop/{image}')
def display_image(image_content):
  return Image(image_content)

"""pegando imagens para exibir"""

def get_bytes(image):
  byteArr = BytesIO()
  image.save(byteArr, format='PNG')
  return byteArr.getvalue()

"""exibindo imagens"""

image6 = get_image ('image6.jpeg')
image6

image4 = get_image ('image4.jpeg')
image4

"""-imagens --- comparar 01"""

source_image = get_image('image6.jpeg') #imagem de origem
target_image = get_image('image4.jpeg') #imagem de destino

response = client.compare_faces(  #CompareFaces - Utiliza ML para probabilidade
    SourceImage={'Bytes': get_bytes(source_image)}, 
    TargetImage={'Bytes': get_bytes(target_image)}
)
matched = response['FaceMatches']
matched

"""----- imagem e onfidencia """

if len(matched) > 0:
  for item in matched:
    print(f"Semelhança de {item['Similarity']} % com {item['Face']['Confidence']} % de confiança")