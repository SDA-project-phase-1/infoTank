import json

def load_config(path="config.json"):
    with open(path, "r") as file: #config.json open hoti
        cfg = json.load(file) #cfg variable mein load hoti
    return cfg

def validate_config(cfg):
    #check karta hai ke filters naam ka koi variable config.json mein hai ke nai or wo dictionary form mein hai ya nai
    if "filters" not in cfg or not isinstance(cfg["filters"], dict):
        raise ValueError("config.json mein filters naam ka object nahi")

    filters = cfg["filters"] #loading values of filters from cfg in variable

    region = filters.get("region") #continent hai ye
    year = filters.get("year")
    country = filters.get("country", None)

    operation = cfg.get("operation")
    output = cfg.get("output")

    #neechey wali lines assure karti hain ke correct data type ho or extra spaces na hon variable values mein
    if not isinstance(region, str) or not region.strip(): #continent hai ye
        raise ValueError("region empty hai")

    if not isinstance(year, int):
        raise ValueError("year integer nahi hai")

    if country is not None and (not isinstance(country, str) or not country.strip()):
        raise ValueError("country string ya null nahi hai")

    if operation not in {"average", "sum"}:
        raise ValueError("operation is either average or sum")

    if output not in {"dashboard"}:
        raise ValueError("output 'dashboard' honi chahye.")

    return cfg