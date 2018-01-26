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


class Amerika:
    def __init__(self, stat, hlavni_mesto, druhe_mesto, treti_mesto):
        self.stat = stat
        self.hlavni_mesto = hlavni_mesto
        self.druhe_mesto = druhe_mesto
        self.treti_mesto = treti_mesto

    def nazev_statu(self):
        return self.stat

    def hlavni(self):
        return self.hlavni_mesto

    def druhe(self):
        return self.druhe_mesto

    def treti(self):
        return self.treti_mesto


# -----------------------------------------------------------------
# USA, Washington 1

usa = Amerika('USA', 'Washington', 'Boston', 'New York')
print('Jak se jmenuje hlavní město státu', usa.nazev_statu(), '?\n')
time.sleep(1)
print('a:', usa.hlavni(), '\nb:', usa.druhe(), '\nc:', usa.treti())
time.sleep(1)
usa_usa = input('Tvoje odpověď?:')
if usa_usa == 'a' or usa_usa == 'A':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je', usa.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Kanada, Ottawa 2

kanada = Amerika('KANADA', 'Ottawa', 'Toronto', 'Montreal')
print('Jak se jmenuje hlavní město státu', kanada.nazev_statu(), '?\n')
time.sleep(1)
print('a:', kanada.druhe(), '\nb:', kanada.treti(), '\nc:', kanada.hlavni())
time.sleep(1)
kanada_kanada = input('Tvoje odpověď?:')
if kanada_kanada == 'c' or kanada_kanada == 'C':
    print('Super!\n')
    body += 1
else:
    print('Správná odpověď je', kanada.hlavni(), '.\n')
time.sleep(1)


# -----------------------------------------------------------------
# Mexiko, Mexico City 3

mexiko = Amerika('MEXIKO', 'Mexico City', 'Tijuana', 'Monterrey')
print('Jak se jmenuje hlavní město státu', mexiko.nazev_statu(), '?\n')
time.sleep(1)
print('a:', mexiko.druhe(), '\nb:', mexiko.hlavni(), '\nc:', mexiko.treti())
time.sleep(1)
mexiko_mexiko = input('Tvoje odpověď?:')
if mexiko_mexiko == 'b' or mexiko_mexiko == 'B':
    print('Správně!\n')
    body += 1
else:
    print('Správná odpověď je', mexiko.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# -----------------------------------------------------------------
print('Teď navštívíme Střední Ameriku.\n')  # STŘEDNÍ AMERIKA
time.sleep(1)

# -----------------------------------------------------------------
# Belize, Belmopan 4

belize = Amerika('BELIZE', 'Belmopan', 'Belize City', 'San Ignacio')
print('Jak se jmenuje hlavní město státu', belize.nazev_statu(), '?\n')
time.sleep(1)
print('a:', belize.druhe(), '\nb:', belize.treti(), '\nc:', belize.hlavni())
time.sleep(1)
belize_belize = input('Tvoje odpověď?:')
if belize_belize == 'c' or belize_belize == 'C':
    print('Ano!\n')
    body += 1
else:
    print('Správná odpověď je', belize.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Guatemala, Ciudad de Guatemala 5

guatemala = Amerika('GUATEMALA', 'Ciudad de Guatemala', 'Antigua de Guatemala', 'Cobán')
print('Jak se jmenuje hlavní město státu', guatemala.nazev_statu(), '?\n')
time.sleep(1)
print('a:', guatemala.hlavni(), '\nb:', guatemala.treti(), '\nc:', guatemala.druhe())
time.sleep(1)
guatemala_guatemala = input('Tvoje odpověď?:')
if guatemala_guatemala == 'a' or guatemala_guatemala == 'A':
    print('Jo!\n')
    body += 1
else:
    print('Správná odpověď je', guatemala.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Honduras, Tegucigalpa 6

honduras = Amerika('HONDURAS', 'Tegucigalpa', 'San Pedro Sula', 'La Ceiba')
print('Jak se jmenuje hlavní město státu', honduras.nazev_statu(), '?\n')
time.sleep(1)
print('a:', honduras.druhe(), '\nb:', honduras.treti(), '\nc:', honduras.hlavni())
time.sleep(1)
honduras_honduras = input('Tvoje odpověď?:')
if honduras_honduras == 'c' or honduras_honduras == 'C':
    print('Skvěle!\n')
    body += 1
else:
    print('Správná odpověď je', honduras.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Kostarika, San José 7

kostarika = Amerika('KOSTARIKA', 'San José', 'Liberia', 'Tamarindo')
print('Jak se jmenuje hlavní město státu', kostarika.nazev_statu(), '?\n')
time.sleep(1)
print('a:', kostarika.druhe(), '\nb:', kostarika.hlavni(), '\nc:', kostarika.treti())
time.sleep(1)
kostarika_kostarika = input('Tvoje odpověď?:')
if kostarika_kostarika == 'b' or kostarika_kostarika == 'B':
    print('Paráda!\n')
    body += 1
else:
    print('Správná odpověď je', kostarika.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Nikaragua, Managua 8

nikaragua = Amerika('NIKARAGUA', 'Managua', 'León', 'Granada')
print('Jak se jmenuje hlavní město státu', nikaragua.nazev_statu(), '?\n')
time.sleep(1)
print('a:', nikaragua.druhe(), '\nb:', nikaragua.hlavni(), '\nc:', nikaragua.treti())
time.sleep(1)
nikaragua_nikaragua = input('Tvoje odpověď?:')
if nikaragua_nikaragua == 'b' or nikaragua_nikaragua == 'B':
    print('Bravo!\n')
    body += 1
else:
    print('Správná odpověď je', nikaragua.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Panama, Ciudad de Panamá 9

panama = Amerika('PANAMA', 'Ciudad de Panamá', 'Chitré', 'Colón')
print('Jak se jmenuje hlavní město státu', panama.nazev_statu(), '?\n')
time.sleep(1)
print('a:', panama.hlavni(), '\nb:', panama.druhe(), '\nc:', panama.treti())
time.sleep(1)
panama_panama = input('Tvoje odpověď?:')
if panama_panama == 'a' or panama_panama == 'A':
    print('Perfektní!\n')
    body += 1
else:
    print('Správná odpověď je', panama.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Salvador, San Salvador 10

salvador = Amerika('SALVADOR', 'San Salvador', 'Santa Ana', 'San Miguel')
print('Jak se jmenuje hlavní město státu', salvador.nazev_statu(), '?\n')
time.sleep(1)
print('a:', salvador.treti(), '\nb:', salvador.druhe(), '\nc:', salvador.hlavni())
time.sleep(1)
salvador_salvador = input('Tvoje odpověď?:')
if salvador_salvador == 'c' or salvador_salvador == 'C':
    print('Správná odpověď!\n')
    body += 1
else:
    print('Správná odpověď je', salvador.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
print('Teď se podíváme do Karibiku.\n')  # KARIBIK
time.sleep(1)
# -----------------------------------------------------------------
# Antigua a Barbuda, Saint John's 11

antigua = Amerika('ANTIGUA A BARBUDA', "Saint John's", 'All Saints', 'Jolly Harbour')
print('Jak se jmenuje hlavní město státu', antigua.nazev_statu(), '?\n')
time.sleep(1)
print('a:', antigua.hlavni(), '\nb:', antigua.druhe(), '\nc:', antigua.treti())
time.sleep(1)
antigua_antigua = input('Tvoje odpověď?:')
if antigua_antigua == 'a' or antigua_antigua == 'A':
    print('Ano!\n')
    body += 1
else:
    print('Správná odpověď je', antigua.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Bahamy, Nassau 12

bahamy = Amerika('BAHAMY', 'Nassau', 'Freeport', 'Clarence Town')
print('Jak se jmenuje hlavní město státu', bahamy.nazev_statu(), '?\n')
time.sleep(1)
print('a:', bahamy.druhe(), '\nb:', bahamy.hlavni(), '\nc:', bahamy.treti())
time.sleep(1)
bahamy_bahamy = input('Tvoje odpověď?:')
if bahamy_bahamy == 'b' or bahamy_bahamy == 'B':
    print('Skvěle!\n')
    body += 1
else:
    print('Správná odpověď je', bahamy.hlavni(), '.\n')
time.sleep(1)
# -----------------------------------------------------------------
# Barbados, Bridgetown 13

barbados = Amerika('BARBADOS', 'Bridgetown', 'Holetown', 'Crab Hill')
print('Jak se jmenuje hlavní město státu', barbados.nazev_statu(), '?\n')
time.sleep(1)
print('a:', barbados.hlavni(), '\nb:', barbados.druhe(), '\nc:', barbados.treti())
time.sleep(1)
barbados_barbados = input('Tvoje odpověď?:')
if barbados_barbados == 'a' or barbados_barbados == 'A':
    print('Super!\n')
    body += 1
else:
    print('Správná odpověď je', barbados.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Dominika, Roseau 14

dominika = Amerika('DOMINIKA', 'Roseau', 'Canefield', 'Portsmouth')
print('Jak se jmenuje hlavní město státu', dominika.nazev_statu(), '?\n')
time.sleep(1)
print('a:', dominika.druhe(), '\nb:', dominika.treti(), '\nc:', dominika.hlavni())
time.sleep(1)
dominika_dominika = input('Tvoje odpověď?:')
if dominika_dominika == 'c' or dominika_dominika == 'C':
    print('Paráda!\n')
    body += 1
else:
    print('Správná odpověď je', dominika.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Dominikánská republika, Santo Domingo 15

dominikanska_republika = Amerika('DOMINIKÁNSKÁ REPUBLIKA', 'Santo Domingo', 'La Romana', 'Puerto Plata')
print('Jak se jmenuje hlavní město státu', dominikanska_republika.nazev_statu(), '?\n')
time.sleep(1)
print('a:', dominikanska_republika.druhe(), '\nb:', dominikanska_republika.treti(), '\nc:', dominikanska_republika.hlavni())
time.sleep(1)
dominika_dominika = input('Tvoje odpověď?:')
if dominika_dominika == 'c' or dominika_dominika == 'C':
    print('Paráda!\n')
    body += 1
else:
    print('Správná odpověď je', dominikanska_republika.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Grenada, Saint George's 16

grenada = Amerika('GRENADA', "Saint George's", 'Gouyave', 'Sauteurs')
print('Jak se jmenuje hlavní město státu', grenada.nazev_statu(), '?\n')
time.sleep(1)
print('a:', grenada.hlavni(), '\nb:', grenada.treti(), '\nc:', grenada.druhe())
time.sleep(1)
grenada_grenada = input('Tvoje odpověď?:')
if grenada_grenada == 'a' or grenada_grenada == 'A':
    print('Ano!\n')
    body += 1
else:
    print('Správná odpověď je', grenada.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Haiti, Port-au-Prince 17

haiti = Amerika('HAITI', 'Port-au-Prince', 'Jacmel', 'Pétion-Ville')
print('Jak se jmenuje hlavní město státu', haiti.nazev_statu(), '?\n')
time.sleep(1)
print('a:', haiti.hlavni(), '\nb:', haiti.treti(), '\nc:', haiti.druhe())
time.sleep(1)
haiti_haiti = input('Tvoje odpověď?:')
if haiti_haiti == 'a' or haiti_haiti == 'A':
    print('Skvěle!\n')
    body += 1
else:
    print('Správná odpověď je', haiti.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Jamajka, Kingston 18

jamajka = Amerika('JAMAJKA', 'Kingston', 'Montego Bay', 'Port Antonio')
print('Jak se jmenuje hlavní město státu', jamajka.nazev_statu(), '?\n')
time.sleep(1)
print('a:', jamajka.druhe(), '\nb:', jamajka.treti(), '\nc:', jamajka.hlavni())
time.sleep(1)
jamajka_jamajka = input('Tvoje odpověď?:')
if jamajka_jamajka == 'c' or jamajka_jamajka == 'C':
    print('Správná odpověď!\n')
    body += 1
else:
    print('Správná odpověď je', jamajka.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Kuba, Havana 19

kuba = Amerika('KUBA', 'Havana', 'Santiago de Cuba', 'Santa Clara')
print('Jak se jmenuje hlavní město státu', kuba.nazev_statu(), '?\n')
time.sleep(1)
print('a:', kuba.druhe(), '\nb:', kuba.treti(), '\nc:', kuba.hlavni())
time.sleep(1)
kuba_kuba = input('Tvoje odpověď?:')
if kuba_kuba == 'c' or kuba_kuba == 'C':
    print('Správná odpověď!\n')
    body += 1
else:
    print('Správná odpověď je', kuba.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Svatá Lucie, Castries 20

svata_lucie = Amerika('SVATÁ LUCIE', 'Castries', 'Soufrière', 'Vieux Fort')
print('Jak se jmenuje hlavní město státu', svata_lucie.nazev_statu(), '?\n')
time.sleep(1)
print('a:', svata_lucie.druhe(), '\nb:', svata_lucie.hlavni(), '\nc:', svata_lucie.treti())
time.sleep(1)
lucie_lucie = input('Tvoje odpověď?:')
if lucie_lucie == 'b' or lucie_lucie == 'B':
    print('Ano!\n')
    body += 1
else:
    print('Správná odpověď je', svata_lucie.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Svatý Kryštof a Nevis, Basseterre 21

sv_krystof = Amerika('SVATÝ KRYŠTOF A NEVIS', 'Basseterre', 'Sandy Point Town', 'Charlestown')
print('Jak se jmenuje hlavní město státu', sv_krystof.nazev_statu(), '?\n')
time.sleep(1)
print('a:', sv_krystof.hlavni(), '\nb:', sv_krystof.druhe(), '\nc:', sv_krystof.treti())
time.sleep(1)
krystof_krystof = input('Tvoje odpověď?:')
if krystof_krystof == 'a' or krystof_krystof == 'A':
    print('Bravo!\n')
    body += 1
else:
    print('Správná odpověď je', sv_krystof.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Svatý Vincenc a Grenadiny, Kingstown 22

sv_vincenc = Amerika('SVATÝ VINCENC A GRENADINY', 'Kingstown', 'Port Elizabeth', 'Barrouallie')
print('Jak se jmenuje hlavní město státu', sv_vincenc.nazev_statu(), '?\n')
time.sleep(1)
print('a:', sv_vincenc.hlavni(), '\nb:', sv_vincenc.druhe(), '\nc:', sv_vincenc.treti())
time.sleep(1)
vincenc_vincenc = input('Tvoje odpověď?:')
if vincenc_vincenc == 'a' or vincenc_vincenc == 'A':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je', sv_vincenc.hlavni(), '.\n')
time.sleep(1)


# -----------------------------------------------------------------
# Trinidad a Tobago, Port of Spain 23

trinidad = Amerika('TRINIDAD A TOBAGO', 'Port of Spain', 'Arima', 'San Fernando')
print('Jak se jmenuje hlavní město státu', trinidad.nazev_statu(), '?\n')
time.sleep(1)
print('a:', trinidad.druhe(), '\nb:', trinidad.treti(), '\nc:', trinidad.hlavni())
time.sleep(1)
trinidad_trinidad = input('Tvoje odpověď?:')
if trinidad_trinidad == 'c' or trinidad_trinidad == 'C':
    print('Klobouk dolů!\n')
    body += 1
else:
    print('Správná odpověď je', trinidad.hlavni(), '.\n')
time.sleep(1)


# -----------------------------------------------------------------
print('Teď se podíváme do Jižní Ameriky.\n')  # JIŽNÍ AMERIKA
time.sleep(1)


# -----------------------------------------------------------------
# Argentina, Buenos Aires 24

argentina = Amerika('ARGENTINA', 'Buenos Aires', 'Rosario', 'La Matanza')
print('Jak se jmenuje hlavní město státu', argentina.nazev_statu(), '?\n')
time.sleep(1)
print('a:', argentina.druhe(), '\nb:', argentina.hlavni(), '\nc:', argentina.treti())
time.sleep(1)
argentina_argentina = input('Tvoje odpověď?:')
if argentina_argentina == 'b' or argentina_argentina == 'B':
    print('Bomba!\n')
    body += 1
else:
    print('Správná odpověď je', argentina.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Bolívie, Sucre 25

bolivie = Amerika('BOLÍVIE', 'Sucre', 'La Paz', 'El Alto')
print('Jak se jmenuje hlavní město státu', bolivie.nazev_statu(), '?\n')
time.sleep(1)
print('a:', bolivie.druhe(), '\nb:', bolivie.hlavni(), '\nc:', bolivie.treti())
time.sleep(1)
bolivie_bolivie = input('Tvoje odpověď?:')
if bolivie_bolivie == 'b' or bolivie_bolivie == 'B':
    print('Yes!\n')
    body += 1
else:
    print('Správná odpověď je', bolivie.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Brazílie, Brasília 26

brazilie = Amerika('BRAZÍLIE', 'Brasília', 'Rio de Janeiro', 'Belo Horizonte')
print('Jak se jmenuje hlavní město státu', brazilie.nazev_statu(), '?\n')
time.sleep(1)
print('a:', brazilie.hlavni(), '\nb:', brazilie.druhe(), '\nc:', brazilie.treti())
time.sleep(1)
brazilie_brazilie = input('Tvoje odpověď?:')
if brazilie_brazilie == 'a' or brazilie_brazilie == 'A':
    print('Výborně!\n')
    body += 1
else:
    print('Správná odpověď je', brazilie.hlavni(), '.\n')
time.sleep(1)


# -----------------------------------------------------------------
# Ekvádor, Quito 27

ekvador = Amerika('EKVÁDOR', 'Quito', 'Cuenca', 'Santo Domingo')
print('Jak se jmenuje hlavní město státu', ekvador.nazev_statu(), '?\n')
time.sleep(1)
print('a:', ekvador.druhe(), '\nb:', ekvador.treti(), '\nc:', ekvador.hlavni())
time.sleep(1)
ekvador_ekvador = input('Tvoje odpověď?:')
if ekvador_ekvador == 'c' or ekvador_ekvador == 'C':
    print('Krása!\n')
    body += 1
else:
    print('Správná odpověď je', ekvador.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Guyana, Georgetown 28

guyana = Amerika('GUYANA', 'Georgetown', 'Linden', 'New Amsterdam')
print('Jak se jmenuje hlavní město státu', guyana.nazev_statu(), '?\n')
time.sleep(1)
print('a:', guyana.druhe(), '\nb:', guyana.treti(), '\nc:', guyana.hlavni())
time.sleep(1)
ekvador_ekvador = input('Tvoje odpověď?:')
if ekvador_ekvador == 'c' or ekvador_ekvador == 'C':
    print('Ano!\n')
    body += 1
else:
    print('Správná odpověď je', guyana.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Chile, Santiago de Chile 29

chile = Amerika('CHILE', 'Santiago de Chile', 'Puerto Alto', 'Valparaíso')
print('Jak se jmenuje hlavní město státu', chile.nazev_statu(), '?\n')
time.sleep(1)
print('a:', chile.hlavni(), '\nb:', chile.treti(), '\nc:', chile.druhe())
time.sleep(1)
chile_chile = input('Tvoje odpověď?:')
if chile_chile == 'a' or chile_chile == 'A':
    print('Správná odpověď!\n')
    body += 1
else:
    print('Správná odpověď je', chile.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Kolumbie, Bogotá 30

kolumbie = Amerika('KOLUMBIE', 'Bogotá', 'Cartagena', 'Medellín')
print('Jak se jmenuje hlavní město státu', kolumbie.nazev_statu(), '?\n')
time.sleep(1)
print('a:', kolumbie.treti(), '\nb:', kolumbie.hlavni(), '\nc:', kolumbie.druhe())
time.sleep(1)
kolumbie_kolumbie = input('Tvoje odpověď?:')
if kolumbie_kolumbie == 'b' or kolumbie_kolumbie == 'B':
    print('Nádhera!\n')
    body += 1
else:
    print('Správná odpověď je', kolumbie.hlavni(), '.\n')
time.sleep(1)


# -----------------------------------------------------------------
# Paraguay, Asunción 31

paraguay = Amerika('PARAGUAY', 'Asunción', 'San Lorenzo', 'Ciudad de Este')
print('Jak se jmenuje hlavní město státu', paraguay.nazev_statu(), '?\n')
time.sleep(1)
print('a:', paraguay.treti(), '\nb:', paraguay.hlavni(), '\nc:', paraguay.druhe())
time.sleep(1)
paraguay_paraguay = input('Tvoje odpověď?:')
if paraguay_paraguay == 'b' or paraguay_paraguay == 'B':
    print('Nádhera!\n')
    body += 1
else:
    print('Správná odpověď je', paraguay.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Peru, Lima 32

peru = Amerika('PERU', 'Lima', 'Cuzco', 'Chimbote')
print('Jak se jmenuje hlavní město státu', peru.nazev_statu(), '?\n')
time.sleep(1)
print('a:', peru.hlavni(), '\nb:', peru.treti(), '\nc:', peru.druhe())
time.sleep(1)
peru_peru = input('Tvoje odpověď?:')
if peru_peru == 'a' or peru_peru == 'A':
    print('Bravo!\n')
    body += 1
else:
    print('Správná odpověď je', peru.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Surinam, Paramaribo 33

surinam = Amerika('SURINAM', 'Paramaribo', 'Albina', 'Brownsweg')
print('Jak se jmenuje hlavní město státu', surinam.nazev_statu(), '?\n')
time.sleep(1)
print('a:', surinam.treti(), '\nb:', surinam.hlavni(), '\nc:', surinam.druhe())
time.sleep(1)
surinam_surinam = input('Tvoje odpověď?:')
if surinam_surinam == 'b' or surinam_surinam == 'B':
    print('Jo!\n')
    body += 1
else:
    print('Správná odpověď je', surinam.hlavni(), '.\n')
time.sleep(1)

# -----------------------------------------------------------------
# Uruguay, Montevideo 34

uruguay = Amerika('URUGUAY', 'Montevideo', 'Rivera', 'Salto')
print('Jak se jmenuje hlavní město státu', uruguay.nazev_statu(), '?\n')
time.sleep(1)
print('a:', uruguay.treti(), '\nb:', uruguay.hlavni(), '\nc:', uruguay.druhe())
time.sleep(1)
uruguay_uruguay = input('Tvoje odpověď?:')
if uruguay_uruguay == 'b' or uruguay_uruguay == 'B':
    print('Super!\n')
    body += 1
else:
    print('Správná odpověď je', uruguay.hlavni(), '.\n')
time.sleep(1)
# -----------------------------------------------------------------
print('Poslední otázka!')
time.sleep(2)
# -----------------------------------------------------------------
# Venezuela, Caracas 35

venezuela = Amerika('VENEZUELA', 'Caracas', 'Maracaibo', 'Valencia')
print('Jak se jmenuje hlavní město státu', venezuela.nazev_statu(), '?\n')
time.sleep(1)
print('a:', venezuela.treti(), '\nb:', venezuela.hlavni(), '\nc:', venezuela.druhe())
time.sleep(1)
venezuela_venezuela = input('Tvoje odpověď?:')
if venezuela_venezuela == 'b' or venezuela_venezuela == 'B':
    print('Vynikající odpověď!\n')
    body += 1
else:
    print('Správná odpověď je', venezuela.hlavni(), '.\n')
time.sleep(1)

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
