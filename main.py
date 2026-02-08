import dataLoader
import dataProcessor
import visualization

data = dataLoader.load_data("gdp_with_continent_filled.csv")
data = dataProcessor.cleaning_data(data)