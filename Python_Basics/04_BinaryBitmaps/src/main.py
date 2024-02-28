from pathlib import Path
# root_folder = Path(__file__).parents[1]
# my_path = root_folder / "resources/a.pbm"
# my_path = root_folder / "out/Cris.ppm"
import subprocess


def text_to_pbm(string, outfileName='OutputName'):
    '''Funkcja zamienia dowolny napis w rastowy plik PBM na którym znajduje się ten napis
    inpout: string, file name
    additionaly: converts any polish character into national standard one
                 converts upper letters to lower
    if the character ar not any of: abcdefghijklmnopqrstuvwxyz ,.!+- then it will be left out
    return: None'''

    root_folder = Path(__file__).parents[1]
    resource_path = root_folder / "resources"
    out_path = root_folder / 'out' / (outfileName + '.pbm')

    string = string.lower()
    string = string.replace('ą', 'a')
    string = string.replace('ę', 'e')
    string = string.replace('ó', 'o')
    string = string.replace('ł', 'l')
    string = string.replace('ż', 'z')
    string = string.replace('ź', 'z')

    character_list = list('abcdefghijklmnopqrstuvwxyz ,.!+-')
    list_str = [letter for letter in string if letter in character_list]

    result = [[] for i in range(12)]

    for character in list_str:
        if character in list(' ,.!+-'):
            if character == ' ':
                character = 'spacja'
            elif character == ',':
                character = 'przecinek'
            elif character == '.':
                character = 'kropka'
            elif character == '!':
                character = 'wykrzyknik'
            elif character == '+':
                character = 'plus'
            elif character == '-':
                character = 'minus'

        full_name = character + '.pbm'
        pbm_src = open(resource_path / full_name, 'r+')

        for index, line in enumerate(pbm_src):
            if index > 2:
                result[index - 3] += line[:-1]

        pbm_src.close()

    with open(out_path, 'w+') as output:
        output.writelines(['P1\n', '# ' + outfileName + '\n'])
        output.write(str(len(result[0])) + ' 12\n')
        for line in result:
            line = ''.join(line)
            output.write(line + '\n')

    return None

def print_pbm(filePath):
    root_folder = Path(__file__).parents[1]
    file_path = root_folder / filePath

    # Define the PowerShell command to run the script with the file name as an argument
    ps_command = "powershell -ExecutionPolicy Unrestricted -File print.ps1 " + str(file_path)
    # Execute the PowerShell command using subprocess.run
    #subprocess.run(ps_command)
    result = subprocess.run(ps_command, capture_output=True, text=True)
    # Check if the command was successful
    if result.returncode == 0:
        # Print the output with proper formatting
        print(result.stdout)
    else:
        # Print any errors
        print("Error:", result.stderr)


def rescale_pbm(pbmfilePath, name="rescaled", scale=2):
    '''Funkcja skaluje pliki pbm'''
    root_folder = Path(__file__).parents[1]
    file_path = root_folder / pbmfilePath
    out_path = root_folder / 'out' / (name + '.pbm')

    src_file = open(file_path, 'r+')
    rescaled = []

    for line in src_file:
        rescaled.append(line)
    src_file.close()

    prev_len = len(rescaled[0])
    temp = [rescaled[0], rescaled[1], rescaled[2]]
    for line in rescaled[3:]:
        new_line = []
        for number in line[:-1]:
            new_line.append(number * scale)
        temp.append(''.join(new_line) + '\n')
    rescaled = temp

    for i in range(len(rescaled) - 1, 2, -1):
        for skala in range(scale - 1):
            rescaled.insert(i, rescaled[i])
    print(len(rescaled))

    wymiar = rescaled[2][:-1].split(' ')
    rescaled[2] = str(int(wymiar[0]) * scale) + ' ' + str(int(wymiar[1]) * scale) + '\n'

    #for line in rescaled:
    #    print(line, end='')

    with open(out_path, 'w+') as output:
        output.writelines(['P1\n', '# ' + name + '\n'])
        output.write(str(int(wymiar[0]) * scale) + ' ' + str(int(wymiar[1]) * scale) + '\n')
        for line in rescaled:
            line = ''.join(line)
            output.write(line)


def colorify_pbm(plik_pbm, outfile=None, color='red', bgr='white'):
    '''zmienia kolor'''
    kolory = {'red': '1 0 0', 'green': '0 1 0', 'blue': '0 0 1', 'white': '1 1 1', 'black': '0 0 0',
              'yellow': '1 1 0', 'pink': '1 0 1', 'cyan': '0 1 1'}  # 3 niestandardowe kolory

    if '0' in color or '1' in color:
        if len(color) == 3:
            color = color[0] + ' ' + color[1] + ' ' + color[2]
    else:
        color = kolory[color]

    if '0' in bgr or '1' in bgr:
        if len(bgr) == 3:
            bgr = bgr[0] + ' ' + bgr[1] + ' ' + bgr[2]
    else:
        bgr = kolory[bgr]

    root_folder = Path(__file__).parents[1]
    file_path = root_folder / plik_pbm

    comment = ''
    size = ''
    colorlist = []
    File = open(file_path, 'r+')
    for index, line in enumerate(File):
        if index == 1:
            comment = line
        if index == 2:
            size = line[:-1]

        if index > 2:
            line = list(line)
            for i in range(len(line) - 1):
                if line[i] == '0':
                    line[i] = bgr
                elif line[i] == '1':
                    line[i] = color
            colorlist.append('  '.join(line))
    File.close()

    if outfile is None:
        temp = plik_pbm.split("/")
        outfile = temp[-1][:-4] + '.ppm'
    else:
        outfile = outfile + '.ppm'
    out_path = root_folder / 'out' / outfile

    #print(colorlist)

    outFile = open(out_path, 'w')
    outFile.write('P3\n')
    outFile.write(comment)
    outFile.write(size + ' 1\n')

    outFile.writelines(colorlist)
    outFile.close()


if __name__ == '__main__':

    temp = "Krzysztof"
    text_to_pbm('Krzysztof!', temp)
    print_pbm("out/" + temp + ".pbm")

    text_to_pbm('Krążkowany Krystianin Ź.', 'Krazek')
    text_to_pbm('29ke"V[5]iN+')

    rescale_pbm('resources/x.pbm', "x", 3)
    print_pbm("out/" + "x" + ".pbm")

    rescale_pbm('out/OutputName.pbm', "rescaledKevin")
    print_pbm("out/" + "rescaledKevin" + ".pbm")

    colorify_pbm('resources/o.pbm')
    colorify_pbm('out/Krzysztof.pbm', 'Cris', 'cyan', 'pink')
    colorify_pbm('out/Krzysztof.pbm', 'Cris2', '1 0 1', '111')
    print_pbm("out/" + "Cris2" + ".ppm")