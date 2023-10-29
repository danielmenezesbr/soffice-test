import subprocess

# Comando que você deseja executar
command = ["soffice", "--convert-to", "pdf", "sample-docx-file-for-testing.docx"]

# Inicie o processo
process = subprocess.Popen(command)

# Aguarde o processo terminar
process.wait()

# Verifique o código de saída
if process.returncode == 0:
    print("Conversão concluída com sucesso.")
    exit(0)
else:
    print("Ocorreu um erro durante a conversão.")