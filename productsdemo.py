import functools
from functools import reduce





products= [
{
        'productId' :1,
        'productName': 'Iphone',
        'price':13555.6
},
{
        'productId' :4,
        'productName': 'oneplus',
        'price':699991.5
},
{
        'productId' :3,
        'productName': 'Samsungflip',
        'price':149999.5
}
]

def myFunc():
return ""
print(reduce(lambda price1, price2 : price1+price2,(map(lambda p : p['price'],filter(lambda product: product['price'] > 10000.0, products))),10))

myFunc()

#print(list(filter(lambda product: product['price'] > 100000.0,products)))
#print(list(map(lambda p : p ['price'],filter(lambda product: product['price'] > 100000.0,products))))
#print(functools.reduce(lambda i,j : i if i<j else j,(list(map(lambda p:p['price'],(filter(lambda product:product['price']>10000.0,products)))))))
#print(functools.reduce(lambda i,j : i if i>j else j,(list(map(lambda p:p['price'],(filter(lambda product:product['price']>10000.0,products)))))))

#print(functools.reduce(lambda i,j : i if i>j else j,(list(map(lambda p:p['price'],(filter(lambda product:product['price']>100000.0,products)))))))
#print(functools.reduce(lambda i,j : i if i<j else j,(list(map(lambda p:p['price'],(filter(lambda product:product['price']>100000.0,products)))))))