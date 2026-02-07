import csv

# return a float -> exception handling huwi ha 
def floatConversionCheck(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

# return a int -> exception handling huwi ha 
def intConversionCheck(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

# takes a row from csv file 
def rowToDictionaryTransformation(row):
    # if a column is missing then return None
    if len(row) < 4:
        return None

    # strip will remove leading and aga wali spacesy
    country, region, year, gdp = (i.strip() for i in row)

    year = intConversionCheck(year)
    gdp = floatConversionCheck(gdp)

    return {"country": country, "region": region, "year": year, "gdp": gdp}

def loadingRows(csvFile):
    #with handles the close responsiblity , r means read mode , f is file name
    with open(csvFile, "r") as f:
        # it return a list  
        reader = csv.reader(f)
        return list(reader) 

csvFileRawData = loadingRows("records.csv")
print(csvFileRawData)
print("\n")
filteredRows = list(
    filter(None, map(rowToDictionaryTransformation, csvFileRawData)) # filter mai None remove ho raha aur maping ho rahi function ki
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