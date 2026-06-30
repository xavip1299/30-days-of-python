
path = input('Digite o caminho do arquivo de log: ')
log_file = open(path, 'r')
log_lines = log_file.readlines()
contador_logs = 0
contador_info = 0
contador_warning = 0

if path == '':
    print('O caminho do arquivo de log não foi informado.')
    exit()

if not (path.endswith('.log') or path.endswith('.txt')):
    print('O arquivo informado não é um arquivo de log.')
    exit()

if len(log_lines) == 0:
    print('O arquivo de log está vazio.')
    exit()   

for line in log_lines:
    if 'ERROR' in line:
        contador_logs += 1
        print(f'O log contém {contador_logs} erros.')
    else: 
        print('O log não contém erros.')

for line in log_lines:
    if 'INFO' in line:
        contador_info += 1
        print(f'O log contém {contador_info} informações.')
    else: 
        print('O log não contém informações.')

for line in log_lines:
    if 'WARNING' in line:
        contador_warning += 1
        print(f'O log contém {contador_warning} avisos.')
    else: 
        print('O log não contém avisos.')

error_counts = {}

for line in log_lines:
    if 'ERROR' in line:
        error_message = line.split('msg=')[1].strip()
        error_counts[error_message] = error_counts.get(error_message, 0) + 1

# Exibir os 5 erros mais comuns
sorted_errors = sorted(error_counts.items(), key=lambda x: x[1], reverse=True)
for error, count in sorted_errors[:5]:
    print(f'{error}: {count} vezes')

# Criar relatório em arquivo txt
with open('relatorio_total.txt', 'w') as report_file:
    report_file.write('Relatório \n')
    report_file.write('==================\n\n')
    for error in sorted_errors[:5]:
        report_file.write(f'{error}: {count} vezes\n')