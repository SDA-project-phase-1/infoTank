import csv
import json 

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


def loadingRows(csvFile):
    #with handles the close responsiblity , r means read mode , f is file name
    with open(csvFile, "r") as f:
        # DictReader uses the first row of the CSV as keys for every subsequent row
        reader = csv.DictReader(f)
        return list(reader) 

csvFileRawData = loadingRows("gdp_with_continent_filled.csv")
for row in csvFileRawData[:5] :
    print(row['Continent'].strip().lower(), '\n')

#&opening the json file
try:
    with open("config.json", 'r') as config_file:
        file_data = json.load(config_file)
except FileNotFoundError:
    print(f"Error: The file {"config.json"} was not found.")
    exit(1)
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from the file {"config.json"}.")
    exit(1)

userRegion = file_data['region']
userYear = file_data['year']
userOperation = file_data['operation']

print("Before filtering:", len(csvFileRawData))
print(f"The region is {userRegion} and the year is {userYear} and the operarion is {userOperation}")
# filteredRows = list(
#     filter(None, map(rowToDictionaryTransformation, csvFileRawData)) # filter mai None remove ho raha aur maping ho rahi function ki
# )

# regionOnly = input("Enter region to filter: ").strip().lower()
# yearOnly = intConversionCheck(input("Enter year to filter: ").strip())
# countryOnly = input("Enter country to filter: ").strip().lower()

csvFileRawData = list(
    filter(lambda r: r['Continent'].strip().lower() == userRegion.strip().lower(), csvFileRawData)
)
# csvFileRawData = list(
#     filter(lambda r: r['year'] == userYear, csvFileRawData)
# )
print("Afetr filtering:", len(csvFileRawData))
# print(csvFileRawData)

# GDPsRegional = list(map(lambda r: r["gdp"], filteredRows))
# avgGDPRegional = sum(GDPsRegional) / len(GDPsRegional) if GDPsRegional else 0

# GDPsCountrial = list(map(lambda r: r["gdp"], filteredCountry))
# avgGDPCountrial = sum(GDPsCountrial) / len(GDPsCountrial) if GDPsCountrial else 0

# print(f"Clean rows: {len(filteredRows)}")
# for row in filteredRows:
#     print(row)
# for row in filteredRegion:
#     print(row)
# for row in filteredYear:
#     print(row)
# for row in filteredCountry:
#     print(row)

# print("Average GDP of regions:", avgGDPRegional)
# print(f"Average GDP of {countryOnly}: {avgGDPCountrial}")
# print("Sum of GDP of regions:", sum(GDPsRegional))