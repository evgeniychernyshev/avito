from app.lib import create_flat, add_flat, search_flats_by_district, search_flats_by_price

container = list()
flat = dict()


def test_create_flat():
    expected = {
        'owner': 'Александр',
        'phone': '+79170000000',
        'price': 14_000,
        'district': 'Вахитовский',
        'address': 'Вишневского, 12-5'
    }
    actual = create_flat(
        'Александр',
        '+79170000000',
        14_000,
        'Вахитовский',
        'Вишневского, 12-5'
    )
    global flat
    flat = actual
    assert actual == expected


def test_add_flat():
    expected = [
        {
            'owner': 'Александр',
            'phone': '+79170000000',
            'price': 14_000,
            'district': 'Вахитовский',
            'address': 'Вишневского, 12-5'
        }
    ]
    global container
    actual = add_flat(container, flat)
    container = actual
    assert actual == expected


def test_search_flats_by_district():
    expected = [
        {
            'owner': 'Александр',
            'phone': '+79170000000',
            'price': 14_000,
            'district': 'Вахитовский',
            'address': 'Вишневского, 12-5'
        }
    ]
    actual = search_flats_by_district(container, ['вахитовский'])
    assert actual == expected


def test_search_flats_by_price():
    expected = [
        {
            'owner': 'Александр',
            'phone': '+79170000000',
            'price': 14_000,
            'district': 'Вахитовский',
            'address': 'Вишневского, 12-5'
        }
    ]
    actual = search_flats_by_price(container, 14_000)
    assert actual == expected





