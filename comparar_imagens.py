import face_recognition

try:
    print("Carregando imagens conhecidas...")
    # Carrega a primeira imagem (rosto1.jpeg)
    imagem_rosto_1 = face_recognition.load_image_file("rosto1.jpeg")

    # Extrai as características do rosto da primeira imagem.
    # [0] pega o primeiro rosto encontrado na imagem.
    encoding_rosto_1 = face_recognition.face_encodings(imagem_rosto_1)[0]

    print("Carregando imagem de comparação...")
    # Carrega a segunda imagem (rosto2.jpeg)
    imagem_rosto_2 = face_recognition.load_image_file("rosto2.jpeg")

    # Extrai as características do rosto da segunda imagem.
    encoding_rosto_2 = face_recognition.face_encodings(imagem_rosto_2)[0]

except FileNotFoundError:
    print("Erro: Verifique se os arquivos 'rosto1.jpeg' e 'rosto2.jpeg' estão na mesma pasta do script.")
    exit()
except IndexError:
    print("Erro: Não foi possível detectar um rosto em uma das imagens. Tente usar fotos mais nítidas.")
    exit()

print("\nComparando os rostos...")
# A função compare_faces retorna uma lista de True/False.
# Comparamos o encoding_rosto_2 com uma lista que contém o encoding_rosto_1.
resultados = face_recognition.compare_faces([encoding_rosto_1], encoding_rosto_2)

# Verifica o resultado da comparação
if resultados[0]:
    print("Resultado: Os rostos são da mesma pessoa.")
else:
    print("Resultado: Os rostos são de pessoas diferentes.")