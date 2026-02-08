import pandas as pd

def to_long_format(df):
    id_vars = ["Country_Name", "Country_Code", "Indicator_Name", "Indicator_Code", "Continent"]
    year_cols = [c for c in df.columns if str(c).isdigit()]

    long_df = pd.melt(
        df,
        id_vars=id_vars,
        value_vars=year_cols,
        var_name="Year",
        value_name="Value"
    )
    return long_df

#filling mean values inplace of missing values wala code
def clean_long_data(long_df):
    long_df["Year"] = pd.to_numeric(long_df["Year"],errors = "coerce")
    long_df["Value"] = pd.to_numeric(long_df["Value"], errors = "coerce")

    long_df = long_df.dropna(subset=["Year"])

    long_df["Value"] = (
        long_df
        .groupby("Country_Name")["Value"]
        .transform(lambda x: x.fillna(x.mean()))
    )

    global_mean = long_df["Value"].mean()
    long_df["Value"] = long_df["Value"].fillna(global_mean)

    long_df["Year"] = long_df["Year"].astype(int)

    return long_df

def filter_by_config(long_df, cfg):
    filters = cfg["filters"]
    region = filters.get("region") #continent hai ye
    year = filters.get("year")
    country = filters.get("country")

    df = long_df

    if region:
        df = df[df["Continent"].str.lower() == region.strip().lower()]

    if year is not None:
        df = df[df["Year"] == year]

    if country:
        df = df[df["Country_Name"].str.lower() == country.strip().lower()]

    return df

# def compute_stat(filtered_df, cfg):
#     op = cfg["operation"]

#     if filtered_df.empty:
#         return None

#     values = filtered_df["Value"]

#     if op == "average":
#         return float(values.mean())
#     elif op == "sum":
#         return float(values.sum())

#     raise ValueError("Unsupported operation in config.")