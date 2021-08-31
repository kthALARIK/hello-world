import csv

'''
1. Skriv en egen klass som representerar en Pokémon.
    Klassen ska ha ett attribut för varje egenskap i tabellen.
    Klassen ska ha minst fem metoder, bland annat dessa tre. Du får välja övriga metoder själv!
        __init__                        (v1.0 CHECK)
        __str__                         (v1.0 CHECK)
        __lt__                          (WTF???)
2. Skriv en funktion som skapar ett Pokémon-objekt (hitta på egna testdata) och anropar metoderna, så att du ser att dom fungerar som dom ska.
3. Skriv sedan en funktion som (v.1.0, tror CHECK)
    läser in alla rader från filen,                                 (JUPP)
    skapar objekt,                                                  (JUPP)
    lagrar objekten i en lista (Pythons list())                     (JUPP)
    returnerar listan. (JUPP)
4. Skriv också en funktion för att söka efter en pokémon i listan.  (SAKNAS)
5. Testa till sist att programmet fungerar korrekt.                 (KVARSTÅR)
'''

# https://docs.python.org/3/library/csv.html - ang. kodning för att öppna csv
# https://stackoverflow.com/questions/3216954/python-no-csv-close ang avsaknad av close-statement
def csv_to_list():
    with open('pokemon.csv', newline='') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=' ', quotechar='|');
        tot_pokemons = [];
        for row in readcsv:
            pokemon = [];
            i=0;
            for davulskap in row: # csv-filen är djävulskt manipulerad från standardformat för att försvåra standardavläsning.
                target = row[i].split(',');
                pokemon= pokemon + target;
                i=+1
            if len(pokemon)==14:
                pokemon = pokemon[0:1]+ [pokemon[1]+' '+pokemon[2]]+pokemon[3:];
            tot_pokemons = tot_pokemons + [pokemon];
        del tot_pokemons[0] # Bulbazar ligger först i listan nu - AKA skiten i första raden är raderat.
    return tot_pokemons


#KOD FÖR ATT TESTA csv_to_list

pokemons = csv_to_list();


print(len(pokemons))
print(pokemons[0])
print(len(pokemons[0]))
x = int(pokemons[0][0])
print(x)
print(type(x))

        #if pokemon[0]!='#':
        #    for k in [0, 4, 5, 6, 7, 8, 9, 10, 11]: # slår fel härruntomkring
        #        pokemon[k]=int(pokemon[k]);
        #print(pokemon)
        #if pokemon[0]!='#':
        #    if pokemon[12]=='True':
        #        pokemon[12]=True;
        #    else:
        #        pokemon[12]=False;
        #if pokemon[3]=='':
        #    pokemon[3]=None;
        #tot_pokemons = tot_pokemons + [pokemon];

#for element in tot_pokemons:
#    print(element);
#    print(len(element));

