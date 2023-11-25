rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
inp = str(input())
sen = f"{inp} запретил букву"


for i, x in enumerate(rus):
    if x in sen:
        print(f"{sen} {x}".lstrip(' ').replace('  ', ' '))
        while sen.count(x) != 0:
            sen = sen.replace(rus[i], '').replace('  ', ' ')

