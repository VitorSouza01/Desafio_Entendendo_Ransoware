
# Importando as Bibliotecas
import os
import pyaes

# Arquivo criptografado
file_name = 'teste.txt.ransomware'

# Ler conteúdo criptografado
with open(file_name, 'rb') as infile:
    file_data = infile.read()

# Chave de descriptografia (igual à usada na criptografia)
key = b"testeransomwares"  # 16 bytes, AES-128
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# Salvar arquivo descriptografado
new_file_name = 'teste.txt'
with open(new_file_name, 'wb') as outfile:
    outfile.write(decrypt_data)

# Remover arquivo criptografado
os.remove(file_name)

print(f'Arquivo "{file_name}" descriptografado como "{new_file_name}".')