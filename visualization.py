import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_year_line(df, cfg):
    plt.figure(figsize=(16, 8))
    sns.lineplot(
        data=df, 
        x="Year", 
        y="Value"
       # hue="Continent"
       # marker="o"
    )
    plt.title(f"{cfg['operation'].capitalize()} GDP Distribution by Continent (1960-2024)")
    plt.xlabel("Year")
    plt.ylabel("GDP Value")
    plt.legend(title="Continent")
    plt.grid(True)
    plt.show()

def plot_year_bar(df, cfg):
    plt.figure(figsize=(20, 6))  # wide figure for many years
    sns.barplot(
        data=df,
        x="Year",
        y="Value",
        palette="tab20" 
       # color="skyblue"
    )

    plt.xticks(rotation=90)  # rotate x-axis labels for readability
    plt.title(f"{cfg['operation'].capitalize()} GDP of {cfg["filters"].get("region")}  by Year (1960-2024)")
    # colors = plt.cm.viridis(np.linspace(0, 1, len(years)))  # viridis colormap
    # plt.bar(years, values, width=8, color=colors)  
    plt.xlabel("Year")
    plt.ylabel("GDP Value")
    plt.tight_layout()
    plt.show()

def plot_reg_voil(df, cfg):
    plt.figure(figsize=(20, 6))

    # Violin plot
    sns.violinplot(
        # x = df['Continent'],
        y=df["Value"],
        data=df,
        palette="viridis",  
        inner="quartile"     # shows median and quartiles inside the violin
    )

    # Overlay swarmplot (individual points) carefully
    sns.swarmplot(
    # x="Continent",
     y=df["Value"],
    data=df,
    color="k",      #black dots
    size=3,          # so points small
    alpha=0.6
)

    plt.xlabel("")  
    plt.ylabel(f"{cfg['operation'].capitalize()} GDP")
    plt.title(f"Distribution of {cfg['operation'].capitalize()} GDP in {cfg["filters"].get("region")} Countries")
    plt.grid(axis='y', alpha=0.5)
    plt.show()

def plot_reg_pie(df, cfg) :
    plt.figure(figsize=(10, 10))

    # Generate colors for each country
    colors = plt.cm.tab20(np.linspace(0, 1, len(df)))

    plt.pie(
        df["Value"],
        labels=df["Continent"],
        autopct="%1.1f%%",
        startangle=140,
        colors=colors,
        shadow=True
    )

    plt.title(f"{cfg["operation"].capitalize()} GDP Distribution by Country in {cfg["filters"].get("region").capitalize()}")
    plt.show()
