if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append((name, score))
print(records)


def get_lower(records):
    lower = min(records)
    for studant in records:
        if studant[1] == lower[1]:
            records.remove(studant)

print(records)
get_lower(records)

def get_second_lower(records):
    lower = min(records)
    names = []
    for studant in records:
        if studant[1] == lower[1]:
            names.append(studant[0])
    names.sort()
    print(names)

get_second_lower(records)