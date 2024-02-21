from pathlib import Path
results = {'gen2': 0, 'gen37': 0, 'same': -1, 'same_how_many': 0}


def reset_game():
    root_folder = Path(__file__).parents[1]
    my_path = root_folder / "resources/gra_first.txt"
    with open(my_path, 'r') as first:
        out_path = root_folder / "out/gra.txt"
        with open(out_path, 'w') as new_game:
            for line in first:
                new_game.write(line)


def read_game():
    root_folder = Path(__file__).parents[1]
    my_path = root_folder / "out/gra.txt"

    current = []
    with open(my_path, 'r') as game_file:
        for line in game_file:
            line = line[:-1]
            line = [0 if letter == '.' else -10 for letter in line]
            current.append(line)

    return current


def write_game(current):
    # przepisuje uklad komorek do pliku
    root_folder = Path(__file__).parents[1]
    my_path = root_folder / "out/gra.txt"

    with open(my_path, 'w') as next_gen:
        for i in range(len(current)):
            for j in range(len(current[i])):
                if current[i][j] == -8 or current[i][j] == -7 or current[i][j] == 3:
                    next_gen.write('X')
                else:
                    next_gen.write('.')
            next_gen.write('\n')


def print_table(current, gen):
    i = 0
    for el in current:
        print(''.join(['X' if letter == -10 else '.' for letter in el]))
        # podpunkty a i b ----------------------------------------------------
        if gen == 2:
            results['gen2'] += sum([1 for letter in el if letter == -10])
        if gen == 37:
            if i == 0 or i == 2:
                results['gen37'] += sum([1 for letter in el[17::] if letter == -10])
            if i == 1:
                results['gen37'] += sum([1 for letter in [el[17], el[19]] if letter == -10])
            i += 1
        # -------------------------------------------------------------------
    print('\n')


def propagation(current):
    # okreslanie zywych komorek w next_gen
    for i in range(len(current)):
        for j in range(len(current[i])):
            if current[i][j] < 0:

                j_diff1 = 0
                j_diff2 = 0
                i_diff1 = 0
                i_diff2 = 0

                if j == 0:
                    j_diff1 = len(current[i])
                if j == len(current[i]) - 1:
                    j_diff2 = -len(current[i])
                if i == 0:
                    i_diff1 = len(current)
                if i == len(current) - 1:
                    i_diff2 = -len(current)

                current[i][j - 1 + j_diff1] += 1  # +j_diff1
                current[i - 1 + i_diff1][j - 1 + j_diff1] += 1  # +j_diff1  +i_diff1
                current[i - 1 + i_diff1][j] += 1  # +i_diff1
                current[i - 1 + i_diff1][j + 1 + j_diff2] += 1  # +j_diff2  +i_diff1
                current[i][j + 1 + j_diff2] += 1  # +j_diff2
                current[i + 1 + i_diff2][j + 1 + j_diff2] += 1  # +j_diff2  +i_diff2
                current[i + 1 + i_diff2][j] += 1  # +i_diff2
                current[i + 1 + i_diff2][j - 1 + j_diff1] += 1  # +j_diff1  +i_diff2
    return current


def isSame(current, next_gen):
    current_c = []
    result = False
    for line in current:
        temp = []
        for number in line:
            if number == -8 or number == -7 or number == 3:
                temp.append('X')
            else:
                temp.append('.')
        current_c.append(''.join(temp))
    if current_c == next_gen:
        results['same'] = generation
        for line in current_c:
            results['same_how_many'] += sum([1 for letter in line if letter == 'X'])
        result = True
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    how_many_gen = 60
    reset_game()
    for generation in range(1, how_many_gen):
        current_gen = read_game()
        print_table(current_gen, generation)
        next_gen = propagation(current_gen)
        if results['same'] == -1:
            if isSame(current_gen, next_gen):
                break
        write_game(next_gen)

    print(results)
    root_folder = Path(__file__).parents[1]
    my_path = root_folder / "out/results_gra.txt"
    with open(my_path, 'w') as result_file:
        result_file.write('w drugim pokoleniu jest zywych {} komorek\n'.format(results['gen2']))
cd Git        result_file.write('w 37 generacji komurka w 2 wierszu 19 kolumnie ma {} sąsiadów\n'.format(results['gen37']))
        result_file.write(
            'populacja stabilizyje sie w {} pokoleniu, sklada sie z {} zywych komorek\n'.format(results['same'],
                                                                                                results[
                                                                                                    'same_how_many']))

# zawsze ma 8 sasiadow
# kazda komorka jest oznaczana liczba ujemna
# jesli znaleziona zostaje komorka to wszystkie dookoła maja + 1
# komórka jest dalej żywa jesli ma -8 lub -7
# nowa komórka jest żywa jeśli == 3
