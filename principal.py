import logging
import traceback

from modelo.arquivo_entrada_csv import ArquivoEntrada
from tradutor.relatorio_html import renderizar_template, escrever_relatorio_html


try:
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] %(message)s',
                        handlers=[
                            logging.FileHandler('processo.log'),
                            logging.StreamHandler()
                        ])

    logging.info('Lendo o arquivo .csv e preenchendo os objetos')
    objeto_arquivo_entrada = ArquivoEntrada()
    objeto_arquivo_entrada.construir_arquivo_entrada()

    logging.info('Renderizando template... ')
    template_texto_pronto = renderizar_template(objeto_arquivo_entrada)

    logging.info('Iniciando escrita do relatório .html...')
    escrever_relatorio_html(template_texto_pronto)
    logging.info('Relatório gerado com sucesso.')

except Exception as erro:
    logging.error(f'Deu ruim: {erro}')
    logging.error(traceback.format_exc())
