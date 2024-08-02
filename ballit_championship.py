class BallitChampionship:
    def __init__(self):
        self.teams = []

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
            'founding_year': founding_year
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

# Exemplo de uso:
if __name__ == "__main__":
    championship = BallitChampionship()
    championship.add_team("Time A", "Grito A", 2000)
    championship.add_team("Time B", "Grito B", 2001)
    championship.add_team("Time C", "Grito C", 2002)
    championship.add_team("Time D", "Grito D", 2003)
    championship.add_team("Time E", "Grito E", 2004)
    championship.add_team("Time F", "Grito F", 2005)
    championship.add_team("Time G", "Grito G", 2006)
    championship.add_team("Time H", "Grito H", 2007)

    # Validar times cadastrados
    if championship.validate_teams():
        championship.display_teams()
    else:
        print("A validação dos times falhou.")
