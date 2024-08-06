import random

class BallitChampionship:
    def __init__(self):
        self.teams = []
        self.current_phase_matches = []

    def add_team(self, name, chant, founding_year):
        if len(self.teams) >= 16:
            print("Erro: O número máximo de times (16) já foi atingido.")
            return
        if any(team['name'] == name for team in self.teams):
            print(f"Erro: O time com o nome '{name}' já está cadastrado.")
            return
        self.teams.append({
            'name': name,
            'chant': chant,
            'founding_year': founding_year,
            'points': 0
        })
        print(f"Time '{name}' cadastrado com sucesso.")

    def validate_teams(self):
        num_teams = len(self.teams)
        if num_teams < 8:
            print("Erro: O número mínimo de times (8) não foi atingido.")
            return False
        if num_teams % 2 != 0:
            print("Erro: O número de times deve ser par.")
            return False
        return True

    def display_teams(self):
        if not self.teams:
            print("Nenhum time cadastrado.")
        else:
            print("Times cadastrados:")
            for team in self.teams:
                print(f"Nome: {team['name']}, Grito de Guerra: {team['chant']}, Ano de Fundação: {team['founding_year']}")

    def start_championship(self):
        if not self.validate_teams():
            print("Não é possível iniciar o campeonato. Validação dos times falhou.")
            return
        
        self.current_phase_matches = self.organize_matches(self.teams)
        self.manage_phase()

    def organize_matches(self, teams):
        random.shuffle(teams)
        matches = []
        if len(teams) % 2 != 0:
            bye_team = teams.pop()
            print(f"{bye_team['name']} avançou automaticamente para a próxima fase.")
            matches.append((bye_team, None))
        
        matches += [(teams[i], teams[i + 1]) for i in range(0, len(teams), 2)]
        return matches

    def manage_phase(self):
        while self.current_phase_matches:
            print("\nPartidas a serem realizadas:")
            for idx, (team1, team2) in enumerate(self.current_phase_matches):
                if team2:
                    print(f"{idx + 1}: {team1['name']} vs {team2['name']}")
            
            match_index = int(input("Escolha a partida para administrar (número): ")) - 1
            team1, team2 = self.current_phase_matches.pop(match_index)
            if team2:
                self.administer_match(team1, team2)
            else:
                print(f"{team1['name']} avançou automaticamente para a próxima fase.")
        
        if len(self.teams) > 1:
            print("\nTodas as partidas desta fase foram realizadas.")
            self.current_phase_matches = self.organize_matches(self.teams)
            self.manage_phase()
        else:
            print(f"\nO vencedor do campeonato é o time '{self.teams[0]['name']}'!")

    def administer_match(self, team1, team2):
        while True:
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
                winner = team1 if team1['points'] > team2['points'] else team2
                print(f"Vencedor: {winner['name']}")
                self.teams = [team for team in self.teams if team['name'] != team1['name'] and team['name'] != team2['name']]
                self.teams.append(winner)
                break
            else:
                print("Opção inválida. Tente novamente.")

def add_teams_interactively(championship):
    while len(championship.teams) < 8:
        name = input(f"Qual o nome do time {len(championship.teams) + 1}? ")
        chant = input(f"Qual o grito de guerra do time {name}? ")
        founding_year = int(input(f"Em que ano foi fundado o time {name}? "))
        championship.add_team(name, chant, founding_year)
        
    while len(championship.teams) < 16:
        add_more = input("Deseja adicionar mais um time? (s/n): ").strip().lower()
        if add_more == 'n':
            break
        name = input(f"Qual o nome do time {len(championship.teams) + 1}? ")
        chant = input(f"Qual o grito de guerra do time {name}? ")
        founding_year = int(input(f"Em que ano foi fundado o time {name}? "))
        championship.add_team(name, chant, founding_year)

if __name__ == "__main__":
    print("Bem-vindo ao Campeonato Internacional de BALLIT!")
    
    while True:
        championship = BallitChampionship()
        
        add_teams_interactively(championship)

        if championship.validate_teams():
            championship.display_teams()
            start = input("Deseja iniciar o campeonato? (s/n): ").strip().lower()
            if start == 's':
                championship.start_championship()
                break
        else:
            print("A validação dos times falhou. Por favor, comece novamente.")
