def discounted(price, discount, max_discount=50):
    price=abs(float(price))
    discount=abs(float(discount))
    max_discount=abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Скидка не может быть больлше 99%')
    if discount >= max_discount:
        price_with_discount=price-(price*max_discount/100)
    else: 
        price_with_discount=price-(price*discount/100)
    return price_with_discount

product = {'name': 'Samsung Galaxy S21', 'price': 50000.0, 'discount': 60}
product ['with_discount'] = discounted(product['price'], product['discount'])
print(product)