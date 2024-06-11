import shutil

# Caminhos dos arquivos de origem e destino
origem_andon = r"\\192.168.30.27\interfacePRD\andon\andon.txt"
origem_estoque = r"\\192.168.30.27\interfacePRD\andon\estoque.txt"
destino = r"C:\andon-logistica"

# Executa a cópia do arquivo andon.txt
try:
    shutil.copy(origem_andon, destino)
    print("Arquivo andon.txt copiado com sucesso!")
except FileNotFoundError:
    print("Arquivo andon.txt não encontrado.")

# Executa a cópia do arquivo estoque.txt
try:
    shutil.copy(origem_estoque, destino)
    print("Arquivo estoque.txt copiado com sucesso!")
except FileNotFoundError:
    print("Arquivo estoque.txt não encontrado.")
