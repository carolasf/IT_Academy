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
            'points': 0,
            'blots': 0,
            'plifs': 0,
            'advrunghs': 0
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
            print("A validação dos times falhou. Iniciando novamente...")
            return

        round_number = 1
        while True:
            print(f"\n--- Fase {round_number} ---")
            self.manage_phase()
            if len(self.teams) == 1:
                print(f"\nO vencedor do campeonato é o time '{self.teams[0]['name']}'!")
                self.display_final_report()
                break
            round_number += 1

    def organize_matches(self, teams):
        random.shuffle(teams)  # Embaralha os times para formar duplas aleatórias
        matches = []
        if len(teams) % 2 != 0:  # Número ímpar de times
            bye_team = teams.pop()  # Remove um time para receber bye
            matches.append((bye_team, None))
        for i in range(0, len(teams), 2):
            matches.append((teams[i], teams[i + 1]))
        return matches

    def manage_phase(self):
        self.current_phase_matches = self.organize_matches(self.teams)
        winners = []
        while self.current_phase_matches:
            print("Partidas a serem realizadas:")
            for idx, (team1, team2) in enumerate(self.current_phase_matches):
                if team2 is None:
                    print(f"{idx + 1}: {team1['name']} avança automaticamente (bye)")
                else:
                    print(f"{idx + 1}: {team1['name']} vs {team2['name']}")
            match_number = int(input("Escolha uma partida para administrar (número): "))
            team1, team2 = self.current_phase_matches.pop(match_number - 1)
            if team2 is None:
                print(f"{team1['name']} avança automaticamente para a próxima fase.")
                winners.append(team1)
            else:
                self.administer_match(team1, team2)
                winner = self.determine_winner(team1, team2)
                winners.append(winner)
        self.teams = winners

    def administer_match(self, team1, team2):
        team1['points'] = 50
        team2['points'] = 50
        print(f"\n--- Partida: {team1['name']} vs {team2['name']} ---")
        while True:
            print(f"Pontuação: {team1['name']} - {team1['points']} | {team2['name']} - {team2['points']}")
            print("Opções: ")
            print("1. Registrar um 'blot' para o time A")
            print("2. Registrar um 'blot' para o time B")
            print("3. Registrar um 'plif' para o time A")
            print("4. Registrar um 'plif' para o time B")
            print("5. Aplicar um 'advrungh' (punição) para um time")
            print("6. Encerrar a partida")
            choice = input("Escolha uma opção: ").strip()
            if choice == '1':
                team1['points'] += 5
                team1['blots'] += 1
            elif choice == '2':
                team2['points'] += 5
                team2['blots'] += 1
            elif choice == '3':
                team1['points'] += 1
                team1['plifs'] += 1
            elif choice == '4':
                team2['points'] += 1
                team2['plifs'] += 1
            elif choice == '5':
                punished_team = input("Escolha o time a ser punido: ").strip()
                self.apply_advrungh(punished_team)
            elif choice == '6':
                break
            else:
                print("Opção inválida. Tente novamente.")

    def apply_advrungh(self, team_name):
        for team in self.teams:
            if team['name'].lower() == team_name.lower():
                team['points'] -= 10
                team['advrunghs'] += 1
                print(f"O time '{team['name']}' foi punido com um advrungh e perdeu 10 pontos.")
                return
        print(f"Nenhum time com o nome '{team_name}' encontrado.")

    def determine_winner(self, team1, team2):
        print(f"Partida encerrada: {team1['name']} vs {team2['name']}")
        if team1['points'] > team2['points']:
            print(f"Vencedor: {team1['name']}")
            return team1
        elif team2['points'] > team1['points']:
            print(f"Vencedor: {team2['name']}")
            return team2
        else:
            return self.handle_grusht(team1, team2)

    def handle_grusht(self, team1, team2):
        print("Empate! Iniciando Grusht (desempate)...")
        team1['points'] += 3
        team2['points'] += 3
        print(f"{team1['name']} e {team2['name']} receberam 3 pontos adicionais.")
        return team1 if team1['points'] > team2['points'] else team2

    def display_final_report(self):
        sorted_teams = sorted(self.teams, key=lambda x: x['points'], reverse=True)
        print("\n--- Relatório Final ---")
        print("Time\t\tBlots\tPlifs\tAdvrunghs\tPontos Totais")
        for team in sorted_teams:
            print(f"{team['name']}\t\t{team['blots']}\t{team['plifs']}\t{team['advrunghs']}\t{team['points']}")
        print(f"\nO grito de guerra do time campeão '{sorted_teams[0]['name']}' é: {sorted_teams[0]['chant']}")

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
    print("Bem-vindo ao Campeonato Internacional de Ballit! Cadastre os times! Instruções: cadastre um número par entre 8 e 16 times!")
    while True:
        championship = BallitChampionship()

        # Adicionar times interativamente
        add_teams_interactively(championship)

        # Validar times cadastrados
        if championship.validate_teams():
            championship.display_teams()
            iniciar = input("Deseja iniciar o campeonato? (s/n): ").strip().lower()
            if iniciar == 's':
                championship.start_championship()
                break
        else:
            print("A validação dos times falhou. Cadastre um número par de times.")

