from app.lib import create_flat, add_flat, search_flats_by_district, search_flat_by_price

flats = []

flat_1 = create_flat(
    'Алексей',
    '+79270000000',
    20_000,
    'Ново-савиновский',
    'Ямашева, 37-10'
)

flat_2 = create_flat(
    'Александр',
    '+79170000000',
    14_000,
    'Вахитовский',
    'Вишневского, 12-5'
)

flat_3 = create_flat(
    'Тимур',
    '+79040000000',
    8_000,
    'Авиастроительный',
    'Копылова, 5-45'
)

flat_4 = create_flat(
    'Сергей',
    '+79600000000',
    28_000,
    'Авиастроительный',
    'Химиков, 9-15'
)

flat_5 = create_flat(
    'Василий',
    '+79060000000',
    13_000,
    'Приволжский',
    'Губкина, 44-28'
)

flats = add_flat(flats, flat_1)
flats = add_flat(flats, flat_2)
flats = add_flat(flats, flat_3)
flats = add_flat(flats, flat_4)
flats = add_flat(flats, flat_5)

print(search_flats_by_district(flats, 'авиастроительный'))
print(search_flats_by_district(flats, 'вахитовский'))

print(search_flat_by_price(flats, 20_000))
print(search_flat_by_price(flats, 15_000))
print(search_flat_by_price(flats, 9_000))
