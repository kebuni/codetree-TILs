good1 = ('codetree','50')

new_name, new_code = input().split()
good2 = (new_name, new_code)

for name, code in [good1,good2]:
    print(f"product {code} is {name}")