Extração de dados com web scrapping do website airbnb.com
Permite conhecer o número de alojamentos disponíveis para cada data, assim como o preço médio dos quartos
Frequência de atualização diária - check_in para o dia de hoje, check_out para o dia de amanhã, com atualização automática através da formatação do URL

Ficheiros
- url_formats.py - contém urls para cada cidade/localização + dia de hoje/amanhã como datas de checkin/checkout
- Main.py - faz a extração dos dados, o cálculo e a escrita para o csv

Cada localização tem um ficheiro CSV (gerado pelo programa, cada vez que corre) com o formato nome_da_localização.csv e os dados sobre número de alojamentos disponíveis para cada data;

*****Porto está como "Area do Mapa" - área que representa Porto Central apenas (a pesquisa inclui vários concelhos e teve que se fazer um filtro só para o centro, a área mais turística);


-PARA CORRER- 
Neste diretório:
python main.py