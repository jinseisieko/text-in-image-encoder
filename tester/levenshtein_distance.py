import Levenshtein
def levenshtein_distance(s1, s2):
    return Levenshtein.distance(s1, s2)


if __name__ == "__main__":
    s1 = "aboba10"
    s2 = "aababa011"
    print(f"Расстояние Левенштейна между '{s1}' и '{s2}':", levenshtein_distance(s1, s2))