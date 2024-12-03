def get_two_lists(file_path_input) -> (list[int], list[int]):
    with open(file_path_input, 'r') as file:
        lines = file.readlines()

    list1 = []
    list2 = []
    for line in lines:
        tmp = line.split("   ")
        list1.append(int(tmp[0]))
        list2.append(int(tmp[1]))
    print(list1)
    print(list2)
    return list1, list2


def get_list_distances(list1: list[int], list2: list[int]) -> int:
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    assert len(sorted_list1) == len(sorted_list2)

    new_list = []
    for i in range(0, len(sorted_list1)):
        new_list.append(abs(sorted_list1[i] - sorted_list2[i]))

    return sum(new_list)


def main():
    list1, list2 = get_two_lists("./input.txt")
    distance = get_list_distances(list1, list2)
    print(distance)


if __name__ == '__main__':
    main()
