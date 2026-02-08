import pandas
from dataLoader import load_csv
from dataProcessor import to_long_format, clean_long_data, filter_by_config, compute_stat
from configReader import load_config, validate_config
import visualization as viz

def main():
    try:
        cfg = validate_config(load_config("config.json"))
        print("Config loaded:")
        print(cfg)

        df = load_csv("gdp_with_continent_filled.csv")

        long_df = to_long_format(df)
        long_df = clean_long_data(long_df)

        filtered_df = filter_by_config(long_df, cfg)
        result = compute_stat(filtered_df, cfg)

        print("\n====== DASHBOARD ======")
        print("Filters:", cfg["filters"])
        print("Operation:", cfg["operation"])

        if result is None:
            print("Result: No data found for the given filters.")
            return

        print("Result:", result)

        # Charts
        # Region-wise charts (these are more meaningful if you DON'T filter region too narrowly)
        viz.plot_region_bar(filtered_df)
        viz.plot_region_pie(filtered_df)

        # Year-specific charts
        country = cfg["filters"].get("country")
        if country:
            viz.plot_year_line(long_df, country_name=country)

        viz.plot_year_histogram(filtered_df)

    except FileNotFoundError as e:
        print("File not found:", e)
    except ValueError as e:
        print("Config/Data error:", e)
    except Exception as e:
        print("Unexpected error:", e)

if __name__ == "__main__":
    main()