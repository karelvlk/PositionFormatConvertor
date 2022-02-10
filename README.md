
# KONVERTOR POZIC KAMERY DO RŮZNÝCH FORMÁTŮ

## Využití programu
Tento program je používán ke zpracování dat, které naměří auto s kamerami na střeše, které dělají 360stupňové fotky s mračnem bodů. Data obsahují informace o poloze, natočení a umístění kamer při vytvoření konkrétních fotek a příslušných mračen bodů. Informace z kamer se následně používaní k vizualizaci terénu, kterým auto projíždí (podobné známému Street View od Googlu).

## Jak program funguje a co dělá

Program dostane na vstupu soubor ve formátu txt, který následně konvertuje do jiného formátu pro další práci s ním. Nejdůležitějším formátem pro zpracování těchto dat je JSON nebo jeho rozšířená verze GEOJSON, která jde napřímo nahrát do GISu, což je geografický informační systém. Může se ovšem hodit také výstup v jiných formátech jako je například XML nebo YAML, a proto je v tomto programu možnost konvertování i do těchto formátů. Program je navržen tak, že i případé doplnění o další formáty nebude problém. Software je koncipovám tak, že jeho argumenty se dají přímo zadat do argumenty programu, což umožňuje volání tohoto skriptu z jiného kódu, který může tuto funkcionalitu využívat.

```
Použití:
python convert.py -i fileName -o directory -f format -d delimiter -s skipheader

Argumenty:
    -i, --input         Cesta k vstupnímu txt souboru, ze kter0ho budeme konvertovat,
    -o, --output        Cesta k adresáři, do kterého se konvertovaný soubor uloží
    -f, --format        Formát, do kterého chceme původní txt soubor konvertovat
                            (podporované formáty: JSON, GEOJSON, XML, YAML)
    -d, --delimiter     Oddělovač, který odděluje jednotlivé prvky dat (defaultně mezera)
    -s, --skipheader    Jestli txt soubor obhasuje na prvním řádku záhlaví
                            ('A' - ano; 'N' - ne (defaultně 'N'))
```

V případě nepředání argumentů programu se aktivuje takzvaný uživatelský režim v terminálu. V tomto režimu se vás bude program dotazovat na všechny výše zmíněné parametry potřebné pro úspěšné konvertování. V případě že zadané odpovědi na otázky nebudou validní tak program vypíše příslušný error spolu s textem popisujícím, kde byl problém. U otázek s volitenou odpovědí v případě nezadání žádného textu a zmáčknutí klávesy ENTER se zvolí defaultí možnost.

## Technická dokumentace

Při spušténí programu se načtou argumenty zadané v příkazové řádce a mohou nastat dvě situace - 1. hlavní funkce convertToFormat dostane parametry; 2. hlavní funkce nedostane požadované parametry a zapne se uživatelský režim. V uživatelském režimu se pomocí funkcí input() zjistí požadované informace, které nebyly předány funkci jako parametry. Následně už je postup pro obě varianty stejný. Nejdříve se zjistí zda-li jsou parametry validní a pokud ne tak program vypíše error. Pokud jsou všechny parametry validní program zjistí do jakého formátu má být vstupní txt soubor konvertován a vytvoří příslušny objekt obsahující funkce pro následné operace. Nejříve je zavolají funkce "generateStart" respektive "generateEnd", které vygenerují začátek a konec v příslušném formátu. Následně se zavolá funkce readLines(), která přečte všechny řádky souboru a dočasně uloží. Poté se zavolá funkce "convertLines", která zpracuje a uloží konvertované data tak, že do pole ukláda stringy, tak že každá položka (string) zastupuje jeden řádek, který bude uložený v novém souboru. Jako poslední se zavolá funkce, která vytvoří nový soubor, který uloží do adresáře, který uživatel zadal na začátku programu a následně uloží do souboru jednotlivé řádky uložené v listu pomocí cyklu.

### Popis používaných formátů
    - JSON (JavaScript Object Notation) je odlehčený formát pro výměnu dat. Je jednoduše čitelný i      zapisovatelný člověkem a snadno analyzovatelný i generovatelný strojově. Je založen na podmnožině programovacího jazyka JavaScript.

    - GEOJSON je otevřený standardní formát navržený pro reprezentaci jednoduchých prostorových geografických dat společně s jejich atributy. GeoJSON formát je založen na formátu JSON

    - XML (Extensible Markup Language) je obecný značkovací jazyk, který byl vyvinut a standardizován konsorciem W3C. Je zjednodušenou podobou staršího jazyka SGML. Umožňuje snadné vytváření konkrétních značkovacích jazyků pro různé účely a různé typy dat. Používá se pro serializaci dat, v čemž soupeří např. s JSON či YAML.

    - YAML je formát pro serializaci strukturovaných dat. Mezi rysy tohoto formátu patří čitelnost nejen strojem, ale i člověkem. Struktura a hierarchie dat je řešena předsazením o jednu úroveň sestávající ze 2 nebo 4 mezer (tabulátory nejsou povoleny). V přídapě vícenásobného zanoření se může pro generování stromové struktory použít rekurze, která zařídí příslušné odsazení. Tento postup však není v případě tohoto programu nutný, jelikož máme pevně dané vstupy a výstupy obsahující pouze jedno zanoření

Jelikož všechny výše zmíněné formáty jsou textové, tak nejjednodušší cestou bylo reprezentovat jednotlivé řádky jako `stringy` a ty pak zkonvertované následně jednotlivě zapisovat do nového souboru. Pro každý řádek obsahující informace o jednom bodu se v tomto programu generuje obecná kostra podle výstupního formátu, která je tvořena opět řádky (`stringy`) doplněna o řádky obsahující proměnné s příslušnou informací o daném bodu.
Jelikož struktura všech výše uvedených formátů není nijak komplikovaná nebylo třeba využívat případné knihovny třetích stran, které by konvertování uměly zajišťovat samy. Díky tomu má program menší velikost a je snadno rozšiřitelný.

### Práce s argumenty
Pro práci s argumenty jsem zvolil standartní modul `argparse`, který je součástí základní knihovny Python. Tento modul splňuje všechny požadavky, které program potřebuje. Programování vlastní implementace takové funkcionality by bylo komplikované a nemělo by to žádné výhody. Tato knihovna není externí, tudíž ji není potřeba stahovat, čímž prakticky odpadají všechny starosti.
