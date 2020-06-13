from covid import Covid

covid = Covid()
country_name = input('\nWrite the country name to search in the database: ')
country = covid.get_status_by_country_name(country_name)
data = {
    key:country[key]
    for key in country.keys() and {'confirmed',
                                   'active',
                                   'deaths',
                                   'recovered'}
}

print('\nThe information requested from ' + country_name + ' is below: ')
print(data)
print()

def covid_worldwide():
    print('Total active cases:', covid.get_total_active_cases())
    print('Total confirmed cases:', covid.get_total_confirmed_cases())
    print('Total deaths:', covid.get_total_deaths())
    print('Total recovered cases:', covid.get_total_recovered())

print('The global information is below: ')
covid_worldwide()
