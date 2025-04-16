from itertools import product

# Define o conjunto de dígitos
digits0= 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

digits = '0123456789'
# Define os limites do número de dígitos antes/depois de "DTI"
min_digits = 0

# Arquivo de saída

with open("senhas_dti_numeros.txt", "w") as f:
    for pre_len in range(min_digits, max_digits + 1):
        for suf_len in range(min_digits, max_digits + 1):
            for pre in product(digits, repeat=pre_len):
                for suf in product(digits, repeat=suf_len):
                    senha = ''.join(pre) + 'DTI' + ''.join(suf)
                    f.write(senha + '\n')

#somente sufixo
with open("senhas_dti_sufixo.txt", "w") as f:
    for suf_len in range(min_digits, max_digits + 1):
        for suf in product(digits, repeat=suf_len):
            senha = 'DTI' + ''.join(suf)
            f.write(senha + '\n')

#somente prefixo
with open("senhas_dti_prefixo.txt", "w") as f:
    for pre_len in range(min_digits, max_digits + 1):
        for pre in product(digits, repeat=pre_len):
            senha = ''.join(pre) + 'DTI'
            f.write(senha + '\n')