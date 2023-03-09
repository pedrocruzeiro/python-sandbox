from prettytable import PrettyTable

pokemon_table = PrettyTable()

pokemon_table.add_column("PokemonName", ["Pikachu", "Squirtle", "Charmander"])
pokemon_table.add_column("Type", ["Electric", "Water", "Fire"])
pokemon_table.align["Type"] = "l"
print(pokemon_table)
