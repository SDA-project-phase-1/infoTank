import csv

def floatConversionCheck(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def intConversionCheck(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def rowToDictionaryTransformation(row):
    if len(row) < 4:
        return None

    country, region, year, gdp = (i.strip() for i in row)

    year = intConversionCheck(year)
    gdp = floatConversionCheck(gdp)

    if not country or not region or year is None or gdp is None:
        return None

    return {"country": country, "region": region, "year": year, "gdp": gdp}

def loadingRows(csvFile):
    with open(csvFile, "r") as f:
        reader = csv.reader(f)
        return list(reader)

csvFileRawData = loadingRows("records.csv")

filteredRows = list(
    filter(None, map(rowToDictionaryTransformation, csvFileRawData))
)

regionOnly = input("Enter region to filter: ").strip().lower()
yearOnly = intConversionCheck(input("Enter year to filter: ").strip())
countryOnly = input("Enter country to filter: ").strip().lower()

filteredRegion = list(
    filter(lambda r: r["region"].lower() == regionOnly, filteredRows)
)
filteredYear = list(
    filter(lambda r: r["year"] == yearOnly, filteredRows)
)
filteredCountry = list(
    filter(lambda r: r["country"].lower() == countryOnly, filteredRows)
)

GDPsRegional = list(map(lambda r: r["gdp"], filteredRows))
avgGDPRegional = sum(GDPsRegional) / len(GDPsRegional) if GDPsRegional else 0

GDPsCountrial = list(map(lambda r: r["gdp"], filteredCountry))
avgGDPCountrial = sum(GDPsCountrial) / len(GDPsCountrial) if GDPsCountrial else 0

print(f"Clean rows: {len(filteredRows)}")
for row in filteredRows:
    print(row)
for row in filteredRegion:
    print(row)
for row in filteredYear:
    print(row)
for row in filteredCountry:
    print(row)

print("Average GDP of regions:", avgGDPRegional)
print(f"Average GDP of {countryOnly}: {avgGDPCountrial}")
print("Sum of GDP of regions:", sum(GDPsRegional))