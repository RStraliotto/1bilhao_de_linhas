import pandas as pd
from tqdm import tqdm # Importa o tqdm para barra de progresso
import os

# Exemplo de total de linhas conhecido
total_linhas = 1_000_000

# Define o tamanho do chunk
chunksize = 100_000

# Caminho do arquivo TXT
txt_filename = os.path.join("data", "measurements.txt")

# Verifica se o arquivo existe
if not os.path.exists(txt_filename):
    raise FileNotFoundError(f"Arquivo não encontrado: {txt_filename}")

def process_chunk(chunk):
    # Agrupa os dados por estação e calcula as estatísticas agregadas
    df_agg = chunk.groupby('station')['measure'].agg(['min', 'max', 'mean'])
    return df_agg

def create_df_with_pandas(filename, total_linhas, chunksize=chunksize, sep=';'):
    # Calcula o número total de chunks
    total_chunks = total_linhas // chunksize + (1 if total_linhas % chunksize else 0)
    results = []

    # Lê o arquivo em chunks e processa cada chunk
    for chunk in tqdm(pd.read_csv(filename, sep=sep, header=None, names=['station', 'measure'], chunksize=chunksize), total=total_chunks):
        df_agg = process_chunk(chunk)
        results.append(df_agg)
    
    # Concatena todos os resultados dos chunks
    final_df = pd.concat(results)
    
    # Realiza uma agregação final e ordena os dados pelo nome da estação
    final_df = final_df.groupby(level=0).agg({
        'min': 'min',
        'max': 'max',
        'mean': 'mean'
    }).sort_values('station')
    
    return final_df

# Chama a função para processar o arquivo TXT em chunks
final_txt_df = create_df_with_pandas(txt_filename, total_linhas)

# Exibição dos resultados
print("TXT DataFrame:")
print(final_txt_df)
