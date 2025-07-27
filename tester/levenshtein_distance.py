import Levenshtein
def levenshtein_distance(s1, s2):
    return Levenshtein.distance(s1, s2)


if __name__ == "__main__":
    s1 = "Саша Шахов"
    s2 = "Олег Данилов"
    print(f"Расстояние Левенштейна между '{s1}' и '{s2}':", levenshtein_distance(s1, s2))