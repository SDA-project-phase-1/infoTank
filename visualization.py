import matplotlib.pyplot as plt

def plot_region_bar(df):
    grouped = (
        df.groupby("Continent")["Value"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    grouped.plot(kind="bar")
    plt.title("Continent-wise GDP (Top 10)")
    plt.xlabel("Continent")
    plt.ylabel("GDP (Sum)")
    plt.tight_layout()
    plt.show()

def plot_region_pie(df):
    grouped = (
        df.groupby("Continent")["Value"]
        .sum()
        .sort_values(ascending=False)
        .head(6)
    )
    grouped.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Continent-wise GDP Share")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

def plot_year_line(df, country_name):
    d = df[df["Country_Name"].str.lower() == country_name.lower()]
    series = d.groupby("Year")["Value"].sum().sort_index()

    series.plot(kind="line", marker="o")
    plt.title(f"GDP Over Years: {country_name}")
    plt.xlabel("Year")
    plt.ylabel("GDP")
    plt.tight_layout()
    plt.show()

def plot_year_histogram(df):
    df["Value"].plot(kind="hist", bins=20)
    plt.title("GDP Value Distribution")
    plt.xlabel("GDP")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()