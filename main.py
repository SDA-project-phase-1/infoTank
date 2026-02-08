import pandas
import dataLoader
import dataProcessor 
from configReader import load_config, validate_config
import visualization as viz

def main():
    try:
        #*config.json file load or validate hoti
        cfg = validate_config(load_config("config.json"))
        print("Config loaded:")
        print(cfg)

        #*sir wali file load hoti
        df = dataLoader.load_csv("gdp_with_continent_filled.csv")

        #* changing the format
        long_df = dataProcessor.to_long_format(df)
        long_df = dataProcessor.clean_long_data(long_df)

        filtered_df = dataProcessor.filter_by_config(long_df, cfg)
        result = dataProcessor.compute_stat(filtered_df, cfg)

        print("\n\tDASHBOARD")
        print("Filters:", cfg["filters"])
        print("Operation:", cfg["operation"])

        if result is None:
            print("Result: No data found for the given filters.")
            return

        print("Result:", result)

        #graph plots
        #data  ko process karna ha 
        # regions ki basis pa filter karna ha 
        #phir regions ka sum ya avg nikalna ha 
        #aur usko plot karna ha

        region_to_keep = cfg["filters"].get("region", "").strip().lower()
        countries_in_that_region = pandas.DataFrame(filter(lambda row: str(row["Continent"]).strip().lower() == region_to_keep, long_df.to_dict("records")))
       
        if cfg["operation"] == "sum":
            first_year_filter = countries_in_that_region.groupby("Year")["Value"].sum().reset_index()
        elif cfg["operation"] == "average":
            first_year_filter = countries_in_that_region.groupby("Year")["Value"].mean().reset_index()
       
        print(first_year_filter)
       # viz.plot_year_line(first_year_filter, cfg)
        # viz.plot_year_bar(first_year_filter, cfg)
        print(long_df)
        if cfg["operation"] == "sum":
            sec_reg_filter = long_df.groupby("Continent")["Value"].sum().reset_index()
        elif cfg["operation"] == "average":
            sec_reg_filter = long_df.groupby("Continent")["Value"].mean().reset_index()
        
        viz.plot_reg_voil(sec_reg_filter, cfg)
        viz.plot_reg_pie(sec_reg_filter, cfg)

    #exceptions hain ye qurrat pandey
    except FileNotFoundError as e:
        print("File not found:", e)
    except ValueError as e:
        print("Config/Data error:", e)
    except Exception as e:
        print("Unexpected error:", e)

main()