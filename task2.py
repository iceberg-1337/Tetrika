import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('ru')

arr = {}.fromkeys('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ', 0)


def print_categorymembers(categorymembers):
    for c in categorymembers.values():
        if c.title[0] in arr:
            arr[c.title[0]] += 1

    for key in arr:
        print(key+':', arr[key])


cat = wiki_wiki.page("Категория:Животные по алфавиту")
print_categorymembers(cat.categorymembers)
