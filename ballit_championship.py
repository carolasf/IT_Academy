import random

# Responsável por gerenciar os times e suas operações.
class BallitChampionship:
    def __init__(self):
        self.teams = []

    def add_team(self, name, chant, founding_year):
        #len define o número de iscritos até 16
        if len(self.teams) >= 16:
            print("Erro: O número máximo de times (16) já foi atingido.")
            return
        if any(team['name'] == name for team in self.teams):
            print(f"Erro: O time com o nome '{name}' já está cadastrado.")
            return
        self.teams.append({
            'name': name,
            'chant': chant,
            'founding_year': founding_year
        })
        print(f"Time '{name}' cadastrado com sucesso.")

# O método validate_teams: Verifica se o número de times cadastrados está entre 8 e 16 e se é par.
    def validate_teams(self):
        num_teams = len(self.teams)
        if num_teams < 8:
            print("Erro: O número mínimo de times (8) não foi atingido.")
            return False
        if num_teams % 2 != 0:
            print("Erro: O número de times deve ser par.")
            return False
        return True
    
# Método display_teams: Exibe a lista de times cadastrados.
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
        
        round_number = 1
        current_teams = self.teams.copy()

        while len(current_teams) > 1:
            print(f"\n--- Fase {round_number} ---")
            winners = self.play_round(current_teams)
            current_teams = winners
            round_number += 1
        
        print(f"\nO vencedor do campeonato é o time '{current_teams[0]['name']}'!")

    def play_round(self, teams):
        random.shuffle(teams)
        winners = []

        for i in range(0, len(teams), 2):
            team1 = teams[i]
            team2 = teams[i + 1]
            winner = self.play_match(team1, team2)
            winners.append(winner)
        
        return winners

    def play_match(self, team1, team2):
        print(f"Partida: {team1['name']} vs {team2['name']}")
        winner = random.choice([team1, team2])
        print(f"Vencedor: {winner['name']}")
        return winner


# Exemplo de uso:
if __name__ == "__main__":
    championship = BallitChampionship()
    championship.add_team("Time Amarelo", "Vai time Amarelo", 2022)
    championship.add_team("Time Branco", "Vai time Branco", 2021)
    championship.add_team("Time Cinza", "Vai time Cinza", 2012)
    championship.add_team("Time Dourado", "Vai time Dourado", 2013)
    championship.add_team("Time Verde", "Vai time Verde", 2014)
    championship.add_team("Time Preto", "Vai time Preto", 2015)
    championship.add_team("Time Azul", "Vai time Azul", 2016)
    championship.add_team("Time Rosa", "Vai time Rosa", 2017)

    # Validar times cadastrados
    if championship.validate_teams():
        championship.display_teams()
    else:
        print("A validação dos times falhou.")
