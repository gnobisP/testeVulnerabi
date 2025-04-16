import itertools

charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
min_extra = 0  # mínimo de caracteres antes/depois do "dti"
max_extra = 3  # máximo de caracteres antes/depois do "dti"

with open("palavras_dti.txt", "w") as f:
    for pre_len in range(min_extra, max_extra + 1):
        for suf_len in range(min_extra, max_extra + 1):
            for pre in itertools.product(charset, repeat=pre_len):
                for suf in itertools.product(charset, repeat=suf_len):
                    senha = ''.join(pre) + 'dti' + ''.join(suf)
                    f.write(senha + '\n')
