import random 

class BallitChampionship:
    #Este é o "construtor" da classe. Sempre que você cria um novo campeonato, ele inicializa uma lista vazia para armazenar os times.
    def __init__(self):
        self.teams = [] # Cria uma lista vazia para armazenar os times cadastrados

    # Adiciona um time ao campeonato
    def add_team(self, name, chant, founding_year):
        # Verifica se o número máximo de times (16) já foi atingido
        if len(self.teams) >= 16:
            print("Erro: O número máximo de times (16) já foi atingido.")
            return
        # Verifica se já existe um time com o mesmo nome
        if any(team['name'] == name for team in self.teams):
            print(f"Erro: O time com o nome '{name}' já está cadastrado.")
            return
        # Adiciona o time à lista de times
        self.teams.append({
            'name': name, # Nome do time
            'chant': chant, # Grito de guerra do time
            'founding_year': founding_year # Ano de fundação do time
        })
        print(f"Time '{name}' cadastrado com sucesso.")

    # Valida os times cadastrados
    def validate_teams(self):
        num_teams = len(self.teams) #obtém o número de times cadastrados
        if num_teams < 8:
            # Verifica se o número de times é menor que 8
            print("Erro: O número mínimo de times (8) não foi atingido.")
            return False
        # Verifica se o número de times é ímpar
        if num_teams % 2 != 0:
            print("Erro: O número de times deve ser par.")
            return False
        return True # Retorna True se a validação foi bem-sucedida

    # Exibe os times cadastrados
    def display_teams(self):
        if not self.teams: # Verifica se a lista de times está vazia
            print("Nenhum time cadastrado.")
        else:
            print("Times cadastrados:")
            # Exibe informações de cada time
            for team in self.teams:
                print(f"Nome: {team['name']}, Grito de Guerra: {team['chant']}, Ano de Fundação: {team['founding_year']}")

    # Inicia o campeonato
    def start_championship(self):
        # Valida os times antes de iniciar o campeonato
        if not self.validate_teams():
            print("Não é possível iniciar o campeonato. Validação dos times falhou.")
            return
        
        round_number = 1 #número da fase inicial
        current_teams = self.teams.copy() # Faz uma cópia da lista de times para manipulação durante o campeonato
    
        # Continua até restar apenas um time
        
        while len(current_teams) > 1:
            print(f"\n--- Fase {round_number} ---")
            winners = self.play_round(current_teams) # Organiza e realiza as partidas da fase
            current_teams = winners # Atualiza a lista de times com os vencedores
            round_number += 1  # Avança para a próxima fase
        
        print(f"\nO vencedor do campeonato é o time '{current_teams[0]['name']}'!") 
        
    
    # Organiza e realizar as partidas de uma fase
    def play_round(self, teams):
        # Verifica se o número de times é par
        # Se não for, levanta uma exceção com uma mensagem de erro.
        if len(teams) % 2 != 0:
            print("Número ímpar de times. Adicionando um 'bye'.")
            # Adiciona um 'bye' fictício para que o número de times seja par
            teams.append({'name': 'Bye', 'chant': 'None', 'founding_year': 0})

        random.shuffle(teams)  # Embaralha os times para formar duplas aleatórias
        # cria uma lista de tuplas, onde cada tupla representa uma partida entre dois times. A lista teams é percorrida de dois em dois, formando duplas de times para as partidas.
        matches = [(teams[i], teams[i + 1]) for i in range(0, len(teams), 2)]
        winners = [] # Lista para armazenar os vencedores das partidas

        # Loop para gerenciar as partidas da fase atual
        while matches:
            # Exibe as partidas restantes que ainda precisam ser realizadas
            print("Partidas a serem realizadas:")

            # Percorre cada partida (tupla de dois times) na lista matches
            for idx, (team1, team2) in enumerate(matches):
                # Exibe o índice da partida (iniciado em 1) e os nomes dos times que vão jogar
                print(f"{idx + 1}: {team1['name']} vs {team2['name']}")
            
            match_choice = int(input("Escolha o número da partida que deseja administrar: ")) - 1
            team1, team2 = matches.pop(match_choice)
            winner = self.play_match(team1, team2)
            winners.append(winner)
        
        return winners

    # Simula uma partida entre dois times e escolhe aleatoriamente um vencedor
    def play_match(self, team1, team2):
        if team2['name'] == 'Bye':
            # Se o time adversário é um 'bye', o time 1 avança automaticamente
            print(f"{team1['name']} avança automaticamente para a próxima fase.")
            return team1
        
        print(f"Partida: {team1['name']} vs {team2['name']}")
        winner = random.choice([team1, team2])  # Escolhe aleatoriamente o vencedor
        print(f"Vencedor: {winner['name']}")
        return winner # Retorna o time vencedor
    

# Função para adicionar
def add_teams_interactively(championship):
    # Continua solicitando informações sobre novos times até que haja pelo menos 8 times
    while len(championship.teams) < 8:
        name = input(f"Qual o nome do time {len(championship.teams) + 1}? ")
        chant = input(f"Qual o grito de guerra do time {name}? ")
        # Solicita o ano de fundação do time e converte para um número inteiro
        founding_year = int(input(f"Em que ano foi fundado o time {name}? "))
        # Adiciona o time ao campeonato usando o método add_team
        championship.add_team(name, chant, founding_year)

    # Depois de ter pelo menos 8 times, pergunta se o usuário deseja adicionar mais    
    while len(championship.teams) < 16:
        add_more = input("Deseja adicionar mais um time? (s/n): ").strip().lower()
        # Se a resposta for n encerra o loop
        if add_more == 'n':
            break
        # Solicita as informações do novo time da mesma forma que antes
        name = input(f"Qual o nome do time {len(championship.teams) + 1}? ")
        chant = input(f"Qual o grito de guerra do time {name}? ")
        founding_year = int(input(f"Em que ano foi fundado o time {name}? "))
        # Adiciona o novo time ao campeonato
        championship.add_team(name, chant, founding_year)

# Exemplo de uso:
if __name__ == "__main__":
    print("Bem-vindo ao Campeonato Internacional de BALLIT! Iicie o cadastro dos times!")

    while True:
        # Cria uma nova instância da classe BallitChampionship
        championship = BallitChampionship()
        
        # Adiciona times interativamente
        add_teams_interactively(championship)

        # Verifica se os times cadastrados são válidos para iniciar o campeonato
        if championship.validate_teams():
            # Exibe os times cadastrados
            championship.display_teams()
            # Pergunta ao usuário se deseja iniciar o campeonato
            start = input("Deseja iniciar o campeonato? (s/n): ").strip().lower()
            if start == 's':
            # Inicia o campeonnato
                championship.start_championship()
        else:
            # Se a validação dos times falhar, exibe uma mensagem de erro
            print("A validação dos times falhou, insira mais um time pois o número de times cadastrados deverá ser par.")