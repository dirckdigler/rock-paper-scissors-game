import random

# Define the options
options = ('piedra', 'papel', 'tijera')
counter = 0
empate = 0
perdiste = 0
ganaste = 0

# Define the results dictionary
results = {
  'piedra': {
    'piedra': 'empate',
    'papel': 'perdiste',
    'tijera': 'ganaste'
  },
  'papel': {
    'piedra': 'ganaste',
    'papel': 'empate',
    'tijera': 'perdiste'
  },
  'tijera': {
    'piedra': 'perdiste',
    'papel': 'ganaste',
    'tijera': 'empate'
  }
}

# Prompt the user to choose an option
for i in range(3):
  print('*' * 10)
  print('ROUND ', counter + 1)
  print('*' * 10)
  for index, chosen_option in enumerate(options):
    print(f"{index+1}. {chosen_option}")

  # Get user input and convert to integer
  while True:
    try:
      option_selected = int(
        input("Ingresa el número de la opción que deseas: "))
      counter += 1
      if option_selected < 1 or option_selected > len(options):
        print(
          "Ese número no es una opción válida. Por favor, ingresa un número del 1 al 3."
        )
      if counter <= 3:
        # Process user input
        chosen_option = options[option_selected - 1]
        # Generate random value to choose one of the 3 options
        random_value = random.choice(options)
        result = results[chosen_option][random_value]
        if result == 'empate':
          empate += 1
        elif result == 'perdiste':
          perdiste += 1
        else:
          ganaste += 1
        print(
          f"{result}, elegiste {chosen_option} y la máquina eligió {random_value}."
        )
        results_dict = {
          'empate': empate,
          'perdiste': perdiste,
          'ganaste': ganaste
        }

      if counter == 3:
        # Get the variable name with the maximum value
        max_var = max(results_dict, key=results_dict.get)

        # Check if the machine or the player won
        if max_var == 'empate':
          print("Hubo un empate.")
        elif max_var == 'perdiste':
          print("La máquina ganó.")
        else:
          print("Ganasteeeee!")
          
        # Print the results
        print("\nResultados finales:\n")
        print(f"\033[33mEmpates:\033[0m {empate}")
        print(f"\033[31mPerdiste:\033[0m {perdiste}")
        print(f"\033[32mGanaste:\033[0m {ganaste}")
        break
      else:
        break
    except ValueError:
      print("Ese no es un número. Por favor, ingresa un número del 1 al 3.")
