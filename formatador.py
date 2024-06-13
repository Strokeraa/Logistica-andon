import os

def format_line(line):
    # Define as posições das barras verticais
    bar_positions = [17, 45, 63, 80, 90, 97, 107]
    
    # Remove o 'X' se estiver presente no final da linha
    if line.strip()[-1] == 'X':
        line = line.strip()[:-1]
    
    # Substitui "EM SEPAR." por "EM.SEPAR."
    line = line.replace("EM SEPAR.", "EM.SEPAR.")
    line = line.replace("HEFEI, ANH","HEFEI.AHN")
    line = line.replace("AMANHA"," AMANHA")
    line = line.replace("GM CC&A WORLD HEADQUARTERS,","GM CC&A WORLD HEADQUARTERS")
    line = line.replace("GM CC&A DAVISON ROAD PC,","GM CC&A DAVISON ROAD PC")
    
    # Insere as barras verticais nas posições especificadas
    formatted_line = (
        line[:bar_positions[0]] + ',' +
        line[bar_positions[0]:bar_positions[1]] + ',' +
        line[bar_positions[1]:bar_positions[2]] + ',' +
        line[bar_positions[2]:bar_positions[3]] + ',' +
        line[bar_positions[3]:bar_positions[4]] + ',' +
        line[bar_positions[4]:bar_positions[5]] + ',' +
        line[bar_positions[5]:bar_positions[6]-1] + ',' +  # adiciona a barra após a hora
        line[bar_positions[6]-1:]
    )

    return formatted_line.rstrip() + '\n'

def process_file(input_file, output_file):
    print(f"Diretório de trabalho atual: {os.getcwd()}")
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    formatted_lines = [format_line(line) for line in lines]
    
    with open(output_file, 'w') as file:
        file.writelines(formatted_lines)

# Especifica o caminho completo do arquivo de entrada e saída
input_file = 'C:\\andon-logistica\\andon.txt'
output_file = 'C:\\andon-logistica\\dados_formatados.txt'

# Chama a função principal para processar o arquivo
process_file(input_file, output_file)
