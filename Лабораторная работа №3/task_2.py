def find_common_participants(participants1, participants2, delimiter=","):
    participants_set1 = set(participants1.split(delimiter))
    participants_set2 = set(participants2.split(delimiter))
    common_participants = list(participants_set1.intersection(participants_set2))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники: ", participants)
