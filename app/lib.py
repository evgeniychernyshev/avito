def create_flat(owner, phone, price, district, address):
    return {
        'owner': owner,
        'phone': phone,
        'price': price,
        'district': district,
        'address': address
    }


def add_flat(container, flat):
    copy = container[:]
    copy.append(flat)
    return copy


def search_flats_by_district(container, search):
    search_lowercased = search.strip().lower()
    result = []
    for flat in container:
        if search_lowercased == flat['district'].lower():
            result.append(flat)

    return result


def search_flat_by_price(container, price):
    result = []
    for flat in container:
        if price >= flat['price']:
            result.append(flat)

    return result
