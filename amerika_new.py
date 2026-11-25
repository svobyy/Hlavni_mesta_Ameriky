import random
import time
from datetime import datetime
from pathlib import Path

DATA = {
    "Severní Ameriky": [
        ("USA", "Washington", ["Boston", "New York"]),
        ("KANADA", "Ottawa", ["Toronto", "Montreal"]),
        ("MEXIKO", "Mexico City", ["Tijuana", "Monterrey"]),
    ],
    "Střední Ameriky": [
        ("BELIZE", "Belmopan", ["Belize City", "San Ignacio"]),
        ("GUATEMALA", "Ciudad de Guatemala", ["Antigua de Guatemala", "Cobán"]),
        ("HONDURAS", "Tegucigalpa", ["San Pedro Sula", "La Ceiba"]),
        ("KOSTARIKA", "San José", ["Liberia", "Tamarindo"]),
        ("NIKARAGUA", "Managua", ["León", "Granada"]),
        ("PANAMA", "Ciudad de Panamá", ["Chitré", "Colón"]),
        ("SALVADOR", "San Salvador", ["Santa Ana", "San Miguel"]),
    ],
    "Karibiku": [
        ("ANTIGUA A BARBUDA", "Saint John's", ["All Saints", "Jolly Harbour"]),
        ("BAHAMY", "Nassau", ["Freeport", "Clarence Town"]),
        ("BARBADOS", "Bridgetown", ["Holetown", "Crab Hill"]),
        ("DOMINIKA", "Roseau", ["Canefield", "Portsmouth"]),
        ("DOMINIKÁNSKÁ REPUBLIKA", "Santo Domingo", ["La Romana", "Puerto Plata"]),
        ("GRENADA", "Saint George's", ["Gouyave", "Sauteurs"]),
        ("HAITI", "Port-au-Prince", ["Jacmel", "Pétion-Ville"]),
        ("JAMAJKA", "Kingston", ["Montego Bay", "Port Antonio"]),
        ("KUBA", "Havana", ["Santiago de Cuba", "Santa Clara"]),
        ("SVATÁ LUCIE", "Castries", ["Soufrière", "Vieux Fort"]),
        ("SVATÝ KRYŠTOF A NEVIS", "Basseterre", ["Sandy Point Town", "Charlestown"]),
        ("SVATÝ VINCENC A GRENADINY", "Kingstown", ["Port Elizabeth", "Barrouallie"]),
        ("TRINIDAD A TOBAGO", "Port of Spain", ["Arima", "San Fernando"]),
    ],
    "Jižní Ameriky": [
        ("ARGENTINA", "Buenos Aires", ["Rosario", "La Matanza"]),
        ("BOLÍVIE", "Sucre", ["La Paz", "El Alto"]),
        ("BRAZÍLIE", "Brasília", ["Rio de Janeiro", "Belo Horizonte"]),
        ("EKVÁDOR", "Quito", ["Cuenca", "Santo Domingo"]),
        ("GUYANA", "Georgetown", ["Linden", "New Amsterdam"]),
        ("CHILE", "Santiago de Chile", ["Puerto Alto", "Valparaíso"]),
        ("KOLUMBIE", "Bogotá", ["Cartagena", "Medellín"]),
        ("PARAGUAY", "Asunción", ["San Lorenzo", "Ciudad de Este"]),
        ("PERU", "Lima", ["Cuzco", "Chimbote"]),
        ("SURINAM", "Paramaribo", ["Albina", "Brownsweg"]),
        ("URUGUAY", "Montevideo", ["Rivera", "Salto"]),
        ("VENEZUELA", "Caracas", ["Maracaibo", "Valencia"]),
    ],
}

POCHVALY = ["Výborně!", "Super!", "Správně!", "Paráda!", "Bravo!", "Perfektní!", "Bomba!"]

print("Vítám tě u testu z hlavních měst Ameriky.\nOdpověď (a, b nebo c) odešli klávesou ENTER.\n")
start_time = datetime.now()
body, celkem = 0, sum(len(staty) for staty in DATA.values())

for region, staty in DATA.items():
    print(f"Teď se podíváme do {region}.\n")
    for stat, hlavni, spatne in staty:
        moznosti = [hlavni, *spatne]
        random.shuffle(moznosti)  # automatické promíchání pořadí a, b, c
        volby = dict(zip(["a", "b", "c"], moznosti))

        print(f"Jak se jmenuje hlavní město státu {stat}?")
        for klic, mesto in volby.items():
            print(f"  {klic}: {mesto}")

        odpoved = input("Tvoje odpověď?: ").strip().lower()
        if volby.get(odpoved) == hlavni:
            print(f"{random.choice(POCHVALY)}\n")
            body += 1
        else:
            print(f"Správná odpověď je {hlavni}.\n")
        time.sleep(0.5)

cas = str(datetime.now() - start_time)[:7]
uspesnost = body / celkem * 100
vysledek = f"Pocet spravnych odpovedi: {body}/{celkem}\nTvuj cas: {cas}\nTvoje uspesnost: {uspesnost:.2f}%\n"

print(f"KONEC TESTU! GRATULUJI!\n{vysledek}")
soubor = Path("C:/tvoje_skore/amerika_vysledek.txt")
soubor.parent.mkdir(parents=True, exist_ok=True)
soubor.write_text(vysledek, encoding="utf-8")
