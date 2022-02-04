
## KONVERTOR POZIC KAMERY DO RŮZNÝCH FORMÁTŮ

# Využití programu
Tento program je používán ke zpracování dat, které naměří auto s kamerami na střeše, které dělají 360stupňové fotky s mračnem bodů. Data obsahují informace o poloze, natočení a umístění kamer při vytvoření konkrétních fotek a příslušných mračen bodů. Informace z kamer se následně používaní k vizualizaci terénu, kterým auto projíždí (podobné známému Street View od Googlu).

# Jak program funguje a co dělá

Program dostane na vstupu soubor ve formátu txt, který následně konvertuje do jiného formátu pro další práci s ním. Nejdůležitějším formátem pro zpracování těchto dat je JSON nebo jeho rozšířená verze GEOJSON, která jde napřímo nahrát do GISu, což je geografický informační systém. Může se ovšem hodit také výstup v jiných formátech jako je například XML nebo YAML, a proto je v tomto programu možnost konvertování i do těchto formátů. Program je navržen tak, že i případé doplnění o další formáty nebude problém. Software je koncipovám tak, že jeho argumenty se dají přímo zadat do argumenty programu, což umožňuje volání tohoto skriptu z jiného kódu, který může tuto funkcionalitu využívat.

Použití:
python convert.py -i fileName -o directory -f format -d delimiter -s skipheader

Argumenty:
    -i, --input         Cesta k vstupnímu txt souboru, ze kter0ho budeme konvertovat,
    -o, --output        Cesta k adresáři, do kterého se konvertovaný soubor uloží
    -f, --format        Formát, do kterého chceme původní txt soubor konvertovat
                            (podporované formáty: JSON, GEOJSON, XML, YAML)
    -d, --delimiter     Oddělovač, který odděluje jednotlivé prvky dat (defaultně mezera)
    -s, --skipheader   Jestli txt soubor obhasuje na prvním řádku záhlaví
                            ('A' - ano; 'N' - ne (defaultně 'N'))

V případě nepředání argumentů programu se aktivuje takzvaný uživatelský režim v terminálu. V tomto režimu se vás bude program dotazovat na všechny výše zmíněné parametry potřebné pro úspěšné konvertování. V případě že zadané odpovědi na otázky nebudou validní tak program vypíše příslušný error spolu s textem popisujícím, kde byl problém. U otázek s volitenou odpovědí v případě nezadání žádného textu a zmáčknutí klávesy ENTER se zvolí defaultí možnost.

# Technická dokumentace

Při spušténí programu se načtou argumenty zadané v příkazové řádce a mohou nastat dvě situace - 1. hlavní funkce convertToFormat dostane parametry; 2. hlavní funkce nedostane požadované parametry a zapne se uživatelský režim. V uživatelském režimu se pomocí funkcí input() zjistí požadované informace, které nebyly předány funkci jako parametry. Následně už je postup pro obě varianty stejný. Nejdříve se zjistí zda-li jsou parametry validní a pokud ne tak program vypíše error. Pokud jsou všechny parametry validní program zjistí do jakého formátu má být vstupní txt soubor konvertován a vytvoří příslušny objekt obsahující funkce pro následné operace. Nejříve je zavolají funkce "generateStart" respektive "generateEnd", které vygenerují začátek a konec v příslušném formátu. Následně se zavolá funkce readLines(), která přečte všechny řádky souboru a dočasně uloží. Poté se zavolá funkce "convertLines", která zpracuje a uloží konvertované data tak, že do pole ukláda stringy, tak že každá položka (string) zastupuje jeden řádek, který bude uložený v novém souboru. Jako poslední se zavolá funkce, která vytvoří nový soubor, který uloží do adresáře, který uživatel zadal na začátku programu a následně uloží do souboru jednotlivé řádky uložené v listu pomocí cyklu.
