def remover_caracteres_transformar_inteiro(valor):
    if valor == '':
        raise ValueError(f'O produto está sem preço')
    valor_formatado = int(valor.replace('.', '').replace(',', ''))
    return valor_formatado
