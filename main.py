import requests
from bs4 import BeautifulSoup
from csv import DictWriter
import statistics
import url_formats


# funcao para extrair a info sobre quartos do url da pagina fornecido
def extract_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser') # html soup

    #numero de quartos para as datas selecionadas
    numero_quartos = soup.find(class_="_78tyg5")
    numero_quartos = numero_quartos.string
    numero_quartos = str(numero_quartos)

    # info sobre a data e localizacao
    data_localizacao = soup.select("div ._l6n8jt")
    info = [d.text for d in data_localizacao]

    # juntar toda a info
    info.append(numero_quartos)
    info.append(calc_preco_medio(url))

    return info


def calc_preco_medio(url):
    # acesso a pagina
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser') # html soup

    # extracao de precos da pagina
    precos_html = soup.select("div ._1jo4hgw") # extrair html com precos
    precos_lista = [p.text for p in precos_html] # extrair texto do html
    precos = [p[0:4] for p in precos_lista] # extrair parte numerica

    # lista final de preços em formato int
    final_precos = []

    for p in precos:
        final_precos.append(int(''.join(i for i in p if i.isdigit())))

    # calculo da media dos precos a ser devolvida
    media_precos = statistics.mean(final_precos)

    return media_precos


# escreve a informacao obtida para um csv
def write_info(info):
    # guardar em dicionario de resultados
    resultados = {}
    resultados["Cidade"] = info[0]
    resultados["Data"] = info[1]
    resultados["Numero de Alojamentos"] = info[2]
    resultados["Preco Medio"] = info[3]

    ## guardar no CSV
    CSV_headers = ["Cidade", "Data", "Numero de Alojamentos", "Preco Medio"] # headers

    # csv com dados
    nome_csv = str(info[0]) # nome do csv é o nome da cidade
    nome_csv = nome_csv + '.csv' # para especificar o formato

    with open(nome_csv, 'a', newline='') as f_object:
    # para escrever dados do dicionario de resultados
        dictwriter_object = DictWriter(f_object, fieldnames=CSV_headers)
        dictwriter_object.writerow(resultados)
        f_object.close() # fechar o ficheiro


if __name__ == "__main__":
    # extrair info das localizacoes pretendidas - numero de alojamentos disponiveis
    lisboa = extract_info(url_formats.url_lisboa)
    cascais = extract_info(url_formats.url_cascais)
    sintra = extract_info(url_formats.url_sintra)

    porto = extract_info(url_formats.url_porto)

    madeira = extract_info(url_formats.url_madeira)
    sao_miguel = extract_info(url_formats.url_sao_miguel)

    vilamoura = extract_info(url_formats.url_vilamoura)
    lagos = extract_info(url_formats.url_lagos)

    # guardar para csv
    write_info(lisboa)
    write_info(porto)
    write_info(madeira)
    write_info(sao_miguel)
    write_info(vilamoura)
    write_info(lagos)
    write_info(cascais)
    write_info(sintra)

