import pandas as pd

revenues = pd.Series([5555, 7000, 1980])

print(revenues.values)
print(revenues.index)

city_revenues = pd.Series(
    [4200, 8000, 3453],
    index=['Amsterdam', 'Toronto', 'Tokyo']
)
city_employee_count_data = {'Amsterdam': 5, 'Tokyo': 8}
city_employee_count = pd.Series(city_employee_count_data)

print(city_employee_count.keys())

city_data = pd.DataFrame({
    'revenue': city_revenues,
    'employee_count': city_employee_count
})

print(city_data)

# You can get the axes like this
print(city_data.axes)

print(revenues[1])
print(city_revenues["Toronto"])

print(city_data.revenue)

further_city_data = pd.DataFrame(
    {
        'revenue': [7000, 3400],
        'employee_count': [2, 2]
    },
    index = ['New York', 'Barcelona']
)

all_city_data = pd.concat([city_data, further_city_data], sort=False)
print(all_city_data)
