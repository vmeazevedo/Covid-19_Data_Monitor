from covid import Covid

covid = Covid()
country_name = input('\nEnter the country name: ')
country = covid.get_status_by_country_name(country_name)
data = {
    key:country[key]
    for key in country.keys() and {'confirmed',
                                   'active',
                                   'deaths',
                                   'recovered'}
}

print('\nPresenting the requested information from: ' + country_name + '.')
print(data)
print()

def covid_worldwide():
    print('Total active cases:', covid.get_total_active_cases())
    print('Total confirmed cases:', covid.get_total_confirmed_cases())
    print('Total deaths:', covid.get_total_deaths())
    print('Total recovered cases:', covid.get_total_recovered())

print('Presenting the global information: ')
covid_worldwide()

# Adding a loop
flag = True
while flag == True:
    response = input(str('\nWould you like to make another search? [Y/N]?')).lower()
    if response == "y":
        covid_worldwide()
    else:
        break

print("\nBe safe.")
        
