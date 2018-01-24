
import datetime
import time
import pathlib

body = int(0)  # počet zodpovězených otázek
pocet = int(35)  # celkový počet otázek
# -----------------------------------------------------------------

print('Vítám tě u testu z hlavních měst Ameriky.\n')  # uvítání
time.sleep(2)
print('Test zabere asi 5 minut tvého času. Čeká tě 35 otázek.\n')
time.sleep(2)
print("Svoji odpověď (a, b nebo c) odešli stisknutím klávesy ENTER.\n")
time.sleep(2)
# -----------------------------------------------------------------

print('Nejdříve se podíváme do Severní Ameriky.\n')  # SEVERNÍ AMERIKA
time.sleep(1)
# -----------------------------------------------------------------

start_time = datetime.datetime.now()  # začátek měření času

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město USA?\n')  # USA, Washington 1
usa = ['A.Washington', 'B.Boston', 'C.New York']
time.sleep(0.5)

print('\n'.join(usa))

washington = input('Tvoje odpověď?:')
if washington == 'A' or washington == 'a':
    print('Výborně!\n')
    body += 1
else:
    print('Špatná odpověď! Je to Washington.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město KANADY?\n')  # Kanada, Ottawa 2
kanada_list = ['A.Toronto', 'B.Montreal', 'C.Ottawa']
time.sleep(0.5)

print('\n'.join(kanada_list))

kanada = input('Tvoje odpověď?:')
if kanada == 'C' or kanada == 'c':
    print('Skvěle!\n')
    body += 1
else:
    print('Bohužel! Je to Ottawa.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město MEXIKA?\n')  # Mexico, Mexico City 3
mexiko_list = ['A.Monterrey', 'B.Tijuana', 'C.Mexico City']
time.sleep(0.5)

print('\n'.join(mexiko_list))

mexico = input('Tvoje odpověď?:')
if mexico == 'C' or mexico == 'c':
    print('Paráda!\n')
    body += 1
else:
    print('Bohužel! Je to Mexico City.\n')

time.sleep(0.5)
# -----------------------------------------------------------------
print('Teď navštívíme Střední Ameriku.\n')  # STŘEDNÍ AMERIKA
time.sleep(1)

print('Jak se jmenuje hlavní město BELIZE?\n')  # Belize, Belmopan 4
belize_list = ['A.Belize City', 'B.Belmopan', 'C.San Ignacio']
time.sleep(0.5)

print('\n'.join(belize_list))

belize = input('Tvoje odpověď?:')
if belize == 'B' or belize == 'b':
    print('Bravo!\n')
    body += 1
else:
    print('Bohužel! Je to Belmopan.\n')

time.sleep(0.5)
# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město státu GUATEMALA?\n')  # Guatemala, Ciudad de Guatemala 5
guatemala_list = ['A.Ciudad de Guatemala', 'B.Antigua Guatemala', 'C.Cobán']
time.sleep(0.5)

print('\n'.join(guatemala_list))

guatemala = input('Tvoje odpověď?:')
if guatemala == 'A' or guatemala == 'a':
    print('Ano!\n')
    body += 1
else:
    print('Bohužel! Je to Ciudad de Guatemala.\n')

time.sleep(0.5)
# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město státu HONDURAS?\n')  # Honduras, Tegucigalpa 6
honduras_list = ['A.La Ceiba', 'B.San Pedro Sula', 'C.Tegucigalpa']
time.sleep(0.5)

print('\n'.join(honduras_list))

honduras = input('Tvoje odpověď?:')
if honduras == 'C' or honduras == 'c':
    print('Výborně!\n')
    body += 1
else:
    print('Bohužel! Je to Tegucigalpa.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město KOSTARIKY?\n')  # Kostarika, San José 7
kostarika_list = ['A.San José', 'B.Liberia', 'C.Tamarindo']
time.sleep(0.5)

print('\n'.join(kostarika_list))

kostarika = input('Tvoje odpověď?:')
if kostarika == 'A' or kostarika == 'a':
    print('Skvěle!\n')
    body += 1
else:
    print('Bohužel! Je to San José.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město státu NIKARAGUA?\n')  # Nikaragua, Managua 8
nikaragua_list = ['A.Granada', 'B.León', 'C.Managua']
time.sleep(0.5)

print('\n'.join(nikaragua_list))

nikaragua = input('Tvoje odpověď?:')
if nikaragua == 'C' or nikaragua == 'c':
    print('Správná odpověď!\n')
    body += 1
else:
    print('Bohužel! Je to Managua.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město státu PANAMA?\n')  # Panama, Ciudad de Panamá 9
panama_list = ['A.Ciudad de Panamá', 'B.Colón', 'C.Chitré']
time.sleep(0.5)

print('\n'.join(panama_list))

panama = input('Tvoje odpověď?:')
if panama == 'A' or panama == 'a':
    print('Výborně!\n')
    body += 1
else:
    print('Bohužel! Je to Ciudad de Panamá.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město státu SALVADOR?\n')  # Salvador, San Salvador 10
salvador_list = ['A.San Miguel', 'B.Santa Ana', 'C.San Salvador']
time.sleep(0.5)

print('\n'.join(salvador_list))

salvador = input('Tvoje odpověď?:')
if salvador == 'C' or salvador == 'c':
    print('Správná odpověď!\n')
    body += 1
else:
    print('Správná odpověď je San Salvador.\n')

time.sleep(0.5)

# -----------------------------------------------------------------
print('Teď se podíváme do Karibiku.\n')  # KARIBIK
time.sleep(1)
# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město ostrovního státu ANTIGUA A BARBUDA?\n')  # Antigua a Barbuda, Saint John's 11
antigua_list = ['A.All Saints', "B.Saint John's", 'C.Jolly Harbour']
time.sleep(0.5)

print('\n'.join(antigua_list))

antigua = input('Tvoje odpověď?:')
if antigua == 'B' or antigua == 'b':
    print('Klobouk dolů!\n')
    body += 1
else:
    print("Správná odpověď je Saint John's.\n")

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město BAHAMSKÝCH OSTROVŮ?\n')  # Bahamy, Nassau 12
bahamy_list = ['A.Nassau', 'B.Freeport', 'C.Clarence Town']
time.sleep(0.5)

print('\n'.join(bahamy_list))

bahamy = input('Tvoje odpověď?:')
if bahamy == 'A' or bahamy == 'a':
    print('Krása!\n')
    body += 1
else:
    print('Správná odpověď je Nassau.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město BARBADOSU?\n')  # Barbados, Bridgetown 13
barbados_list = ['A.Crab Hill', 'B.Holetown', 'C.Bridgetown']
time.sleep(0.5)

print('\n'.join(barbados_list))

barbados = input('Tvoje odpověď?:')
if barbados == 'C' or barbados == 'c':
    print('Paráda!\n')
    body += 1
else:
    print('Správná odpověď je Bridgetown.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město státu DOMINIKA?\n')  # Dominika, Roseau 14
dominika_list = ['A.Portsmouth', 'B.Canefield', 'C.Roseau']
time.sleep(0.5)

print('\n'.join(dominika_list))

dominika = input('Tvoje odpověď?:')
if dominika == 'C' or dominika == 'c':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je Roseau.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město státu DOMINIKÁNSKÁ REPUBLIKA?\n')  # Dominikánská republika, Santo Domingo 15
dominikanska_list = ['A.La Romana', 'B.Santo Domingo', 'C.Puerto Plata']
time.sleep(0.5)

print('\n'.join(dominikanska_list))

dominikanska = input('Tvoje odpověď?:')
if dominikanska == 'B' or dominikanska == 'b':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je Santo Domingo.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město státu GRENADA?\n')  # Grenada, Saint George's 16
grenada_list = ["A.Saint George's", 'B.Gouyave', 'C.Sauteurs']
time.sleep(0.5)

print('\n'.join(grenada_list))

grenada = input('Tvoje odpověď?:')
if grenada == 'A' or grenada == 'a':
    print('Bravo!\n')
    body += 1
else:
    print("Správná odpověď je Saint George's.\n")

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město HAITI?\n')  # Haiti, Port-au-Prince 17
haiti_list = ['A.Port-au-Prince', 'B.Jacmel', 'C.Pétion-Ville']
time.sleep(0.5)

print('\n'.join(haiti_list))

haiti = input('Tvoje odpověď?:')
if haiti == 'A' or haiti == 'a':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je Port-au-Prince.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město JAMAJKY?\n')  # Jamajka, Kingston 18
jamajka_list = ['A.Port Antonio', 'B.Kingston', 'C.Montego Bay']
time.sleep(0.5)

print('\n'.join(jamajka_list))

jamajka = input('Tvoje odpověď?:')
if jamajka == 'B' or jamajka == 'b':
    print('Správná odpověď!\n')
    body += 1
else:
    print('Správná odpověď je Kingston.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město KUBY?\n')  # Kuba, Havana 19
kuba_list = ['A.Santa Clara', 'B.Havana', 'C.Santiago de Cuba']
time.sleep(0.5)

print('\n'.join(kuba_list))

kuba = input('Tvoje odpověď?:')
if kuba == 'B' or kuba == 'b':
    print('Krása!\n')
    body += 1
else:
    print('Správná odpověď je Havana.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město SVATÉ LUCIE?\n')  # Svatá Lucie, Castries 20
lucie_list = ['A.Castries', 'B.Soufrière', 'C.Vieux Fort']
time.sleep(0.5)

print('\n'.join(lucie_list))

lucie = input('Tvoje odpověď?:')
if lucie == 'A' or lucie == 'a':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je Castries.\n')

time.sleep(0.5)


# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město ostrovního státu SVATÝ KRYŠTOF A NEVIS?\n')  # Svatá Kryštof a Nevis, Basseterre 21
krystof_list = ['A.Sandy Point Town', 'B.Charlestown', 'C.Basseterre']
time.sleep(0.5)

print('\n'.join(krystof_list))

krystof = input('Tvoje odpověď?:')
if krystof == 'C' or krystof == 'c':
    print('Klobouk dolů!\n')
    body += 1
else:
    print('Správná odpověď je Basseterre.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město ostrovního státu SVATÝ VINCENC A GRENADINY?\n')  # Svatý Vincenc a Grenadiny, Kingstown 22
vincenc_list = ['A.Barrouallie', 'B.Port Elizabeth', 'C.Kingstown']
time.sleep(0.5)

print('\n'.join(vincenc_list))

vincenc = input('Tvoje odpověď?:')
if vincenc == 'C' or vincenc == 'c':
    print('Super!\n')
    body += 1
else:
    print('Správná odpověď je Kingstown.\n')

time.sleep(0.5)


# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město ostrovního státu TRINIDAD A TOBAGO?\n')  # Trinidad a Tobago, Port of Spain 23
trinidad_list = ['A.San Fernando', 'B.Port of Spain', 'C.Arima']
time.sleep(0.5)

print('\n'.join(trinidad_list))

trinidad = input('Tvoje odpověď?:')
if trinidad == 'B' or trinidad == 'b':
    print('Super!\n')
    body += 1
else:
    print('Správná odpověď je Port of Spain.\n')

time.sleep(0.5)


# -----------------------------------------------------------------
print('Teď se podíváme do Jižní Ameriky.\n')  # JIŽNÍ AMERIKA
time.sleep(1)


# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město ARGENTINY?\n')  # Argentina, Buenos Aires 24
argentina_list = ['A.La Matanza', 'B.Buenos Aires', 'C.Rosario']
time.sleep(0.5)

print('\n'.join(argentina_list))

argentina = input('Tvoje odpověď?:')
if argentina == 'B' or argentina == 'b':
    print('Ano!\n')
    body += 1
else:
    print('Správná odpověď je Buenos Aires.\n')

time.sleep(0.5)


# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město BOLÍVIE?\n')  # Bolívie, Sucre 25
bolivie_list = ['A.Sucre', 'B.La Paz', 'C.El Alto']
time.sleep(0.5)

print('\n'.join(bolivie_list))

bolivie = input('Tvoje odpověď?:')
if argentina == 'A' or argentina == 'a':
    print('Správně!\n')
    body += 1
else:
    print('Správná odpověď je Sucre.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město BRAZÍLIE?\n')  # Brazílie, Brasília 26
brazilie_list = ['A.Belo Horizonte', 'B.Brasília', 'C.Rio de Janeiro']
time.sleep(0.5)

print('\n'.join(brazilie_list))

brazilie = input('Tvoje odpověď?:')
if brazilie == 'B' or brazilie == 'b':
    print('Správná odpověď!\n')
    body += 1
else:
    print('Správná odpověď je Brasília.\n')

time.sleep(0.5)


# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město EKVÁDORU?\n')  # Ekvádor, Quito 27
ekvador_list = ['A.Santo Domingo', 'B.Cuenca', 'C.Quito']
time.sleep(0.5)

print('\n'.join(ekvador_list))

ekvador = input('Tvoje odpověď?:')
if ekvador == 'C' or ekvador == 'c':
    print('Super!\n')
    body += 1
else:
    print('Správná odpověď je Quito.\n')

time.sleep(0.5)


# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město státu GUYANA?\n')  # Guyana, Georgetown 28
guyana_list = ['A.New Amsterdam', 'B.Georgetown', 'C.Linden']
time.sleep(0.5)

print('\n'.join(guyana_list))

guyana = input('Tvoje odpověď?:')
if guyana == 'B' or guyana == 'b':
    print('Krása!\n')
    body += 1
else:
    print('Správná odpověď je Georgetown.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město CHILE?\n')  # Chile, Santiago de Chile 29
chile_list = ['A.Valparaíso', 'B.Santiago de Chile', 'C.Puerto Alto']
time.sleep(0.5)

print('\n'.join(chile_list))

chile = input('Tvoje odpověď?:')
if chile == 'B' or chile == 'b':
    print('Perfektní!\n')
    body += 1
else:
    print('Správná odpověď je Santiago de Chile.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město KOLUMBIE?\n')  # Kolumbie, Bogotá 30
kolumbie_list = ['A.Bogotá', 'B.Medellín', 'C.Cartagena']
time.sleep(0.5)

print('\n'.join(kolumbie_list))

kolumbie = input('Tvoje odpověď?:')
if kolumbie == 'A' or kolumbie == 'a':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je Bogotá.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město státu PARAGUAY?\n')  # Paraguay, Asunción 31
paraguay_list = ['A.Ciudad del Este', 'B.San Lorenzo', 'C.Asunción']
time.sleep(0.5)

print('\n'.join(paraguay_list))

paraguay = input('Tvoje odpověď?:')
if paraguay == 'C' or paraguay == 'c':
    print('Jo!\n')
    body += 1
else:
    print('Správná odpověď je Asunción.\n')

time.sleep(0.5)


# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město PERU?\n')  # Peru, Lima 32
peru_list = ['A.Lima', 'B.Cuzco', 'C.Chimbote']
time.sleep(0.5)

print('\n'.join(peru_list))

peru = input('Tvoje odpověď?:')
if peru == 'A' or peru == 'a':
    print('Ano!\n')
    body += 1
else:
    print('Správná odpověď je Lima.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město státu SURINAM?\n')  # Surinam, Paramaribo 33
surinam_list = ['A.Paramaribo', 'B.Albina', 'C.Brownsweg']
time.sleep(0.5)

print('\n'.join(surinam_list))

surinam = input('Tvoje odpověď?:')
if surinam == 'A' or surinam == 'a':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je Paramaribo.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město státu URUGUAY?\n')  # Uruguay, Montevideo 34
uruguay_list = ['A.Salto', 'B.Montevideo', 'C.Rivera']
time.sleep(0.5)

print('\n'.join(uruguay_list))

uruguay = input('Tvoje odpověď?:')
if uruguay == 'B' or uruguay == 'b':
    print('Ano!\n')
    body += 1
else:
    print('Správná odpověď je Montevideo.\n')

time.sleep(0.5)

# -----------------------------------------------------------------

print('Jak se jmenuje hlavní město VENEZUELY?\n')  # Venezuela, Caracas 35
venezuela_list = ['A.Caracas', 'B.Maracaibo', 'C.Valencia']
time.sleep(0.5)

print('\n'.join(venezuela_list))

venezuela = input('Tvoje odpověď?:')
if venezuela == 'A' or venezuela == 'a':
    print('Paráda!\n')
    body += 1
else:
    print('Správná odpověď je Caracas.\n')

time.sleep(0.5)


# -----------------------------------------------------------------
end_time = datetime.datetime.now()  # konec měření času
# -----------------------------------------------------------------
konecny_cas = end_time - start_time
cas = str(konecny_cas)              # převod času na řetězec
# -----------------------------------------------------------------

c = float(body / pocet * 100)  # úspěšnost v procentech, výpočet
# -----------------------------------------------------------------

print('KONEC TESTU! GRATULUJI!\n')  # konec testu
time.sleep(1)
# -----------------------------------------------------------------

print('POČET SPRÁVNÝCH ODPOVĚDÍ:', body)  # vyhodnocení
time.sleep(1)
# -----------------------------------------------------------------

print('TVOJE ÚSPĚŠNOST JE:', '{0:.2f}%'.format(c))
time.sleep(1)                                          # úspěšnost v procentech
# -----------------------------------------------------------------

print('TVŮJ ČAS: {:.7}'.format(cas))  # konečný čas
time.sleep(1)
# -----------------------------------------------------------------
# převod čísel (proměnné --- body a úspěšnost) na řetězec

pocet_bodu = str(body)  # body
uspesnost = str(c)  # procentuální úspěšnost
# -----------------------------------------------------------------
# vytvoření adresáře a souboru s výsledkem na disku C:

pathlib.Path('C:/tvoje_skore').mkdir(parents=True, exist_ok=True)
x = open('C:/tvoje_skore/amerika_vysledek.txt', 'w')
# -----------------------------------------------------------------


# zápis do souboru

with open("C:/tvoje_skore/amerika_vysledek.txt", "w") as text_file:
    text_file.write('Pocet spravnych odpovedi je:{}\n'.format(pocet_bodu))
    text_file.write('Tvuj cas je:{:.7}\n'.format(cas))
    text_file.write('Tvoje uspesnost je:{:.4}%'.format(uspesnost))
x.close()
# -----------------------------------------------------------------

print('Na disku C: v adresáři tvoje_skore máš soubor amerika_vysledek.txt')
print('Soubor můžeš otevřít a podívat se na svůj výsledek.')

input("\nProgram ukončíte stisknutím klávesy ENTER...")
