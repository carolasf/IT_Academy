import random

class BallitChampionship:
    # construtor da classe
    def __init__(self):
        self.teams = []
        self.current_phase_matches = []

    def add_team(self, name, chant, founding_year):
        # Verifica se o número máximo de times foi atingido
        if len(self.teams) >= 16:
            print("Erro: O número máximo de times (16) já foi atingido.")
            return
        # Verifica se já existe um time com o mesmo nome
        if any(team['name'] == name for team in self.teams):
            print(f"Erro: O time com o nome '{name}' já está cadastrado.")
            return
        # Adiciona o time à lista de times
        self.teams.append({
            'name': name,
            'chant': chant, # grito de guerra
            'founding_year': founding_year,
            'points': 0  # Inicializa a pontuação do time com 0
        })
        print(f"Time '{name}' cadastrado com sucesso.")

    def validate_teams(self):
        num_teams = len(self.teams)
        # Verifica se o número mínimo de times foi atingido
        if num_teams < 8:
            print("Erro: O número mínimo de times (8) não foi atingido.")
            return False
        # Verifica se o número de times é par
        if num_teams % 2 != 0:
            print("Erro: O número de times deve ser par.")
            return False
        return True

    # Exibe os times cadastrados
    def display_teams(self):
        if not self.teams:
            print("Nenhum time cadastrado.")
        else:
            print("Times cadastrados:")
            for team in self.teams:
                print(f"Nome: {team['name']}, Grito de Guerra: {team['chant']}, Ano de Fundação: {team['founding_year']}")

    def start_championship(self):
        # Valida os times antes de iniciar o campeonato
        if not self.validate_teams():
            print("Não é possível iniciar o campeonato. Validação dos times falhou.")
            return
        
        # Organiza as partidas para a primeira fase
        self.current_phase_matches = self.organize_matches(self.teams)
        # Gerencia as fases do campeonato
        self.manage_phase()

    def organize_matches(self, teams):
        random.shuffle(teams)  # Embaralha os times para formar duplas aleatórias
        matches = []
        if len(teams) % 2 != 0:  # Se o número de times for ímpar
            bye_team = teams.pop()
            print(f"{bye_team['name']} avançou automaticamente para a próxima fase.")
            matches.append((bye_team, None))  # Time com "bye"
        
        # Forma as duplas para as partidas
        matches += [(teams[i], teams[i + 1]) for i in range(0, len(teams), 2)]
        return matches

    def manage_phase(self):
        # Enquanto houver partidas na fase atual
        while self.current_phase_matches:
            print("\nPartidas a serem realizadas:")
            for idx, (team1, team2) in enumerate(self.current_phase_matches):
                if team2:  # Apenas exibe se ambos os times existirem
                    print(f"{idx + 1}: {team1['name']} vs {team2['name']}")
            
            match_index = int(input("Escolha a partida para administrar (número): ")) - 1
            team1, team2 = self.current_phase_matches.pop(match_index)
            if team2:  # Apenas administra se ambos os times existirem
                self.administer_match(team1, team2)
            else:
                print(f"{team1['name']} avançou automaticamente para a próxima fase.")
        
        # Se restarem mais de um time, organiza a próxima fase
        if len(self.teams) > 1:
            print("\nTodas as partidas desta fase foram realizadas.")
            self.current_phase_matches = self.organize_matches(self.teams)
            self.manage_phase()
        else:
            print(f"\nO vencedor do campeonato é o time '{self.teams[0]['name']}'!")

    def administer_match(self, team1, team2):
        while True:
            # Exibe o painel da partida
            print(f"\nPartida: {team1['name']} vs {team2['name']}")
            print(f"Pontuação: {team1['name']} - {team1['points']} | {team2['name']} - {team2['points']}")
            print("1: Registrar um 'blot' para o time A")
            print("2: Registrar um 'blot' para o time B")
            print("3: Registrar um 'plif' para o time A")
            print("4: Registrar um 'plif' para o time B")
            print("5: Encerrar a partida")

            choice = input("Escolha uma opção: ")
            if choice == '1':
                team1['points'] += 1
            elif choice == '2':
                team2['points'] += 1
            elif choice == '3':
                team1['points'] += 2
            elif choice == '4':
                team2['points'] += 2
            elif choice == '5':
                # Determina o vencedor com base na pontuação
                winner = team1 if team1['points'] > team2['points'] else team2
                print(f"Vencedor: {winner['name']}")
                # Remove os times perdedores da lista e mantém o vencedor
                self.teams = [team for team in self.teams if team['name'] != team1['name'] and team['name'] != team2['name']]
                self.teams.append(winner)
                break
            else:
                print("Opção inválida. Tente novamente.")

# Função para adicionar times interativamente
def add_teams_interactively(championship):
    # Adiciona times até atingir o número mínimo de 8 times
    while len(championship.teams) < 8:
        name = input(f"Qual o nome do time {len(championship.teams) + 1}? ")
        chant = input(f"Qual o grito de guerra do time {name}? ")
        founding_year = int(input(f"Em que ano foi fundado o time {name}? "))
        championship.add_team(name, chant, founding_year)
        
    # Adiciona mais times até atingir o número máximo de 16 times
    while len(championship.teams) < 16:
        if len(championship.teams) >= 16:
            print("Erro: O número máximo de times (16) já foi atingido.")
            break
        add_more = input("Deseja adicionar mais um time? (s/n): ").strip().lower()
        if add_more == 'n':
            break
        name = input(f"Qual o nome do time {len(championship.teams) + 1}? ")
        chant = input(f"Qual o grito de guerra do time {name}? ")
        founding_year = int(input(f"Em que ano foi fundado o time {name}? "))
        championship.add_team(name, chant, founding_year)

# Exemplo de uso:
if __name__ == "__main__":
    print("Bem-vindo ao Campeonato Internacional de BALLIT! Cadastre os times para que o campeonato inicie!")
    
    while True:
        championship = BallitChampionship()
        
        # Adicionar times interativamente
        add_teams_interactively(championship)

        # Validar times cadastrados
        if championship.validate_teams():
            championship.display_teams()
            start = input("Deseja iniciar o campeonato? (s/n): ").strip().lower()
            if start == 's':
                championship.start_championship()
                break
        else:
            print("A validação dos times falhou. Por favor, comece novamente.")
