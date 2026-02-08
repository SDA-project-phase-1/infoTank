
import matplotlib.pyplot as plt


def bar_chart(data,year):
    data.plot(kind="bar")
    plt.title("Sum of GDP by Region")
    plt.xlabel("Region")
    plt.ylabel("GDP")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# region wise plot
# avg ya sum of all the countries in that continent 
# over all the years

# year wise gdp plot 
# continents fix uske sare countries ki avg gdp show kardi ha
   