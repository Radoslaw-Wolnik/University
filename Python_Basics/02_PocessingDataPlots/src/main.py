import pickle
from pathlib import Path

from matplotlib import pyplot as plt


### program otwiera plik galapagos.txt który zawiera dane:
#
# Year
# Month
# Day
# Surface sea temperature minimum
# Surface sea temperature maximum
# Surface sea temperature at 90th percentile
# Heat stress
# Degree heating week
#
# przykladowa linia:
# YYYY MM DD SST_MIN SST_MAX SST@90th_HS SSTA@90th_HS 90th_HS>0 DHW_from_90th_HS>1 BAA_7day_max
# 1985 01 01 22.8200 25.0700 23.8300     -0.6774       0.0000    0.0000            0
# potrzebne dane:
# 1985 01 01 22.8200 25.0700
#
# tworzy słownik {rok : srednia temperatura maksymalna}
# tworzy słownik {rok : srednia temperatura minimalna}


def pickle_max_min_temp():
    root_folder = Path(__file__).parents[1]
    minTemp = {}
    maxTemp = {}
    galapagos_path = root_folder / "resources/galapagos.txt"
    with open(galapagos_path, 'r') as galapagos_file:
        for line_index, line in enumerate(galapagos_file):
            if line_index < 22:
                continue
            if line_index == 13171:
                break
            line = line[:26].split(' ')
            try:
                minTemp[line[0]] += float(line[3])
                maxTemp[line[0]] += float(line[4])
            except KeyError:
                minTemp[line[0]] = float(line[3])
                maxTemp[line[0]] = float(line[4])

    for year, Temp in minTemp.items():
        if int(year[2:]) % 4 == 0:
            minTemp[year] = Temp / 366
        else:
            minTemp[year] = Temp / 365

    for year, Temp in maxTemp.items():
        if int(year[2:]) % 4 == 0:
            maxTemp[year] = Temp / 366
        else:
            maxTemp[year] = Temp / 365

    min_path = root_folder / "out/min_temp_galapagos_sea_surface"
    max_path = root_folder / "out/max_temp_galapagos_sea_surface"

    FileMinTemp = open(min_path, 'wb')
    pickle.dump(minTemp, FileMinTemp)
    FileMinTemp.close()

    FileMaxTemp = open(max_path, 'wb')
    pickle.dump(maxTemp, FileMaxTemp)
    FileMaxTemp.close()


def pickle_open_plot():
    root_folder = Path(__file__).parents[1]
    min_path = root_folder / "out/min_temp_galapagos_sea_surface"
    max_path = root_folder / "out/max_temp_galapagos_sea_surface"
    MinTempFile = open(min_path, 'rb')
    MaxTempFile = open(max_path, 'rb')
    MinTemp = pickle.load(MinTempFile)
    MaxTemp = pickle.load(MaxTempFile)
    MinTempFile.close()
    MaxTempFile.close()

    plt.figure(figsize=(30, 21))
    plt.plot([year for year in MinTemp.keys()], [temp for temp in MinTemp.values()], color='navy', linestyle='dotted')
    plt.xticks([el for el in MinTemp.keys()], rotation=90)
    plt.title(
        "Wykres zmiany minimalnej średniej rocznej temperatury powierzchni wody przy wyspach galapagos w latach 1985-2020")
    plt.xlabel('Lata')
    plt.ylabel('Temperatura stC')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(30, 21))
    plt.plot([year for year in MaxTemp.keys()], [temp for temp in MaxTemp.values()], color='maroon', linestyle='dotted')
    plt.xticks([el for el in MinTemp.keys()], rotation=90)
    plt.title(
        "Wykres zmiany maksymalnej średniej rocznej temperatury powierzchni wody przy wyspach galapagos w latach 1985-2020")
    plt.xlabel('Lata')
    plt.ylabel('Temperatura stC')
    plt.grid(True)
    plt.show()


def slupki_plot():
    root_folder = Path(__file__).parents[1]
    min_path = root_folder / "out/min_temp_galapagos_sea_surface"
    max_path = root_folder / "out/max_temp_galapagos_sea_surface"
    MinTempFile = open(min_path, 'rb')
    MaxTempFile = open(max_path, 'rb')
    MinTemp = pickle.load(MinTempFile)
    MaxTemp = pickle.load(MaxTempFile)
    MinTempFile.close()
    MaxTempFile.close()

    year = [int(year) for year in MinTemp.keys()]
    temp = [temp for temp in MinTemp.values()]
    plt.figure(figsize=(30, 15))
    plt.bar(year, temp, color='skyblue')
    plt.ylim(ymax=26, ymin=20)
    plt.xticks(year, rotation=90)
    plt.title(
        "Wykres przedstawiający roczną średnią temperatury minimalną powierzchni wody przy wyspach galapagos w latach 1985-2020")
    plt.xlabel('Lata')
    plt.ylabel('Temperatura stC')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(30, 15))
    plt.ylim(ymax=30, ymin=22)
    plt.bar([int(year) for year in MaxTemp.keys()], [temp for temp in MaxTemp.values()], color='palevioletred')
    plt.xticks([int(year) for year in MaxTemp.keys()], rotation=90)
    plt.title(
        "Wykres przedstawiający roczną średnią temperatury maksymalnej powierzchni wody przy wyspach galapagos w latach 1985-2020")
    plt.xlabel('Lata')
    plt.ylabel('Temperatura stC')
    plt.grid(True)
    plt.show()


def points_plot():
    root_folder = Path(__file__).parents[1]
    min_path = root_folder / "out/min_temp_galapagos_sea_surface"
    max_path = root_folder / "out/max_temp_galapagos_sea_surface"
    MinTempFile = open(min_path, 'rb')
    MaxTempFile = open(max_path, 'rb')
    MinTemp = pickle.load(MinTempFile)
    MaxTemp = pickle.load(MaxTempFile)
    MinTempFile.close()
    MaxTempFile.close()

    plt.figure(figsize=(30, 21))
    plt.plot([int(year) for year in MinTemp.keys()], [temp for temp in MinTemp.values()], 'co')
    plt.xticks([i for i in range(1985, 2021)], rotation=90)
    plt.title(
        "Wykres przedstawiający roczną średnią temperatury minimalnej powierzchni wody przy wyspach galapagos w latach 1985-2020")
    plt.xlabel('Lata')
    plt.ylabel('Temperatura stC')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(30, 21))
    plt.plot([int(year) for year in MaxTemp.keys()], [temp for temp in MaxTemp.values()], 'o', color='firebrick')
    plt.xticks([i for i in range(1985, 2021)], rotation=90)
    plt.title(
        "Wykres przedstawiający roczną średnią temperatury maksymalnej powierzchni wody przy wyspach galapagos w latach 1985-2020")
    plt.xlabel('Lata')
    plt.ylabel('Temperatura stC')
    plt.grid(True)
    plt.show()


def pie_chart():
    root_folder = Path(__file__).parents[1]
    min_path = root_folder / "out/min_temp_galapagos_sea_surface"
    max_path = root_folder / "out/max_temp_galapagos_sea_surface"
    MinTempFile = open(min_path, 'rb')
    MaxTempFile = open(max_path, 'rb')
    MinTemp = pickle.load(MinTempFile)
    MaxTemp = pickle.load(MaxTempFile)
    MinTempFile.close()
    MaxTempFile.close()

    year = [year for year in MinTemp.keys()]
    temp = [temp for temp in MinTemp.values()]

    plt.figure(figsize=(30, 33))
    plt.pie(temp, labels=year, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.grid(True)
    plt.title(
        "Wykres przedstawiający udział każdej rocznej średniej temperatury minimalnej powierzchni wody przy wyspach galapagos\n w ogólnej średniej minimalnej temperaturze (1985-2020)")
    plt.show()

    year = [year for year in MaxTemp.keys()]
    temp = [temp for temp in MaxTemp.values()]

    plt.figure(figsize=(30, 33))
    plt.pie(temp, labels=year, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.grid(True)
    plt.title(
        "Wykres przedstawiający udział każdej rocznej średniej temperatury maksymalnej powierzchni wody przy wyspach galapagos\n w ogólnej średniej maksymalnej temperaturze (1985-2020)")
    plt.show()


if __name__ == '__main__':
    print("Galpagos\n")
    pickle_max_min_temp()
    pickle_open_plot()
    slupki_plot()
    points_plot()
    pie_chart()
