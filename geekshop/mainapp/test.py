from json import load

content = load(open('fixtures/products.json'))

for c in content['products']:
    print(c)