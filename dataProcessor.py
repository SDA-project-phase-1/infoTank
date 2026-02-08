import pandas

def cleaning_data(data):
    print(type(data))
    data = pandas.DataFrame(filter(lambda x : x.notna(), data))
    print(data)
    # changing the format of the data from wide to long
        #because its esy to plot, and process 
    long_data = pandas.melt(
        data,
        id_vars=['Country_Name','Country_Code','Indicator_Name','Indicator_Code','Continent'],
        var_name= 'Year',
        value_name= 'Value'
    )

    print(long_data )

    #now handling missing values 
    return long_data