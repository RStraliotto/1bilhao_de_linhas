# Gerador de Dados Meteorológicos
Este repositório contém um script para gerar um arquivo de medições meteorológicas com um bilhão de linhas. O arquivo gerado pode ser usado para testes de desempenho e outras finalidades relacionadas a grandes volumes de dados.

## Estrutura do Repositório

- `data/weather_stations.csv`: Arquivo CSV de entrada contendo os nomes das estações meteorológicas.
- `create_measurements.py`: Script principal para gerar o arquivo de medições.

## Requisitos

- Python 3.x

## Como Usar

### 1. Preparar o Ambiente

Clone este repositório e navegue até o diretório do projeto:

```sh
git clone https://github.com/RStraliotto/1bilhao_de_linhas
cd weather-data-generator
```
2. Estrutura do Arquivo CSV
O arquivo data/weather_stations.csv deve conter os nomes das estações meteorológicas, separados por ponto e vírgula (;). Cada linha deve representar uma estação.

3. Executar o Script
Para executar o script, use o seguinte comando:
```sh
python create_measurements.py
```
O script gera um arquivo data/measurements.txt contendo um bilhão de linhas de medições meteorológicas.


Funcionamento do Script
Funções Principais
check_args(file_args): Verifica se os argumentos de entrada são válidos.
build_weather_station_name_list(): Lê os nomes das estações meteorológicas do arquivo CSV.
convert_bytes(num): Converte bytes para um formato legível (KiB, MiB, GiB).
format_elapsed_time(seconds): Formata o tempo decorrido em um formato legível.
estimate_file_size(weather_station_names, num_rows_to_create): Estima o tamanho do arquivo de dados gerado.
build_test_data(weather_station_names, num_rows_to_create): Gera e escreve os dados de teste no arquivo.
Execução Principal
main(): Função principal do programa que coordena a leitura dos nomes das estações, a estimativa do tamanho do arquivo e a geração dos dados de teste.

Exemplo de Uso
Ao executar o script, você verá a estimativa do tamanho do arquivo e o tempo necessário para gerar o arquivo data/measurements.txt. A saída do terminal incluirá algo como:
```sh
O tamanho estimado do arquivo é: X.XX GiB.
Criando o arquivo... isso vai demorar uns 10 minutos...
Arquivo escrito com sucesso em data/measurements.txt
Tamanho final: Y.YY GiB
Tempo decorrido: HH horas MM minutos SS segundos

```
![image](https://github.com/user-attachments/assets/d8b8c24b-8cad-4e87-afcb-03e0a6e7b0e7)


# Processamento de Dados Meteorológicos

Este script em Python processa um arquivo de medições meteorológicas e calcula estatísticas como temperatura mínima, média e máxima para cada estação meteorológica listada no arquivo.

## Como Executar

### 1. Preparar o Ambiente

Clone este repositório e navegue até o diretório do projeto:

```sh
git clone https://github.com/RStraliotto/1bilhao_de_linhas
cd weather-data-processor
```
Executar o Script
Para executar o script, use o seguinte comando:
```sh
python processar_temperaturas.py
```
Isso iniciará o processamento do arquivo de medições. O script carregará os dados, calculará as estatísticas de temperatura para cada estação e exibirá os resultados formatados no terminal.
Exemplo de Uso
## Python
![image](https://github.com/user-attachments/assets/6cca3d9a-f937-4548-89ec-e6d2bfb67062)

## Pandas
![image](https://github.com/user-attachments/assets/1de0437b-e14c-4ef5-bac4-c13f0e2da5d4)

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.

Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

# Workshop Jornada de Dados:
https://github.com/lvgalvao/1bilhaodelinhasaovivo
Vídeo: https://www.youtube.com/live/X3_QTVIjJz0


