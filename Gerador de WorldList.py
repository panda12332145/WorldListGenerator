import time

def generate_wordlist():
    # Caracteres minúsculos, maiúsculos, números e especiais
    lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_chars = lowercase_chars.upper()
    numeric_chars = '0123456789'
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    all_chars = lowercase_chars + uppercase_chars + numeric_chars + special_chars

    with open('WDL.txt', 'w') as file:
        # Escreve caracteres individuais na primeira parte da wordlist
        for char in all_chars:
            file.write(char + '\n')

    while True:
        with open('WDL.txt', 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)

        with open('WDL.txt', 'a') as file:
            for char in all_chars:
                for line in lines:
                    new_line = line.strip() + char + '\n'
                    file.write(new_line)

        # Mostra a quantidade de linhas no arquivo
        print(f"Número de linhas no arquivo 'WDL.txt': {num_lines}")

        # Aguarda por 2 segundos antes de continuar a gerar a wordlist
        time.sleep(2)

if __name__ == '__main__':
    generate_wordlist()
