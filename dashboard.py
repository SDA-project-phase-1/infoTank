def dashboard(long_data, config):
    region = config.get("filters").get("region")
    country = config.get("filters").get("country")
    year = config.get("filters").get("year")
    operation = config.get("operation")

    print("\n===== DASHBOARD =====")
    print(f"Region: {region}")
    print(f"Country: {country}")
    print(f"Year: {year}")
    print(f"Operation: {operation}")
    print("=====================\n")

    #converting to  dictionary kkioke maps etc work with lists not with dataframe
    records = long_data.to_dict("records")

    #taking avg of all the gdp of countries in that region
    
    filtered = list(
        filter(lambda r:
            r["Continent"] == region and
            r["Year"] == year,
            records
        )
    )

    sum_of_gdp_values_of_region = list(map(lambda r: r["Value"], filtered))

    result = sum(sum_of_gdp_values_of_region) / len(sum_of_gdp_values_of_region) if sum_of_gdp_values_of_region else 0
    print(f"the avg of GDP of region is : {result}\n")
    print(f"the sum of GDP of region is : {sum(sum_of_gdp_values_of_region)}\n")

    filtered = list(
            filter(lambda r:
                r["Country_Name"] == country,
                records
            )
        )

    sum_of_gdp_values_of_country = list(map(lambda r: r["Value"], filtered))

    result = sum(sum_of_gdp_values_of_country) / len(sum_of_gdp_values_of_country) if sum_of_gdp_values_of_country else 0

    print(f"The avg of gdp of this country is {result}\n")


    print("=====================\n")

    return result
