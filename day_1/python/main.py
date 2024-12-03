def get_two_lists(file_path_input) -> (list[int], list[int]):
    with open(file_path_input, 'r') as file:
        lines = file.readlines()

    list1 = []
    list2 = []
    for line in lines:
        tmp = line.split("   ")
        list1.append(int(tmp[0]))
        list2.append(int(tmp[1]))
    return list1, list2


def get_list_distances(list1: list[int], list2: list[int]) -> int:
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    assert len(sorted_list1) == len(sorted_list2)

    new_list = []
    for i in range(0, len(sorted_list1)):
        new_list.append(abs(sorted_list1[i] - sorted_list2[i]))

    return sum(new_list)


def get_list_similarity(list1: list[int], list2: list[int]) -> int:
    similarity_list = []
    for number in list1:
        times_in_list = list2.count(number)
        similarity_list.append(times_in_list * number)

    return sum(similarity_list)


def main():
    list1, list2 = get_two_lists("./input.txt")
    print(f"This is the distance of the two lists: {get_list_distances(list1, list2)}")
    print(f"This is the similarity of the two lists: {get_list_similarity(list1, list2)}")


if __name__ == '__main__':
    main()
