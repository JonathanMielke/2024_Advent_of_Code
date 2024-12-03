def format_input(input_text_file: str) -> list[list[int]]:
    with open(input_text_file, 'r') as file:
        lines = file.readlines()
    formatted_data = []
    for line in lines:

        formatted_data.append([int(x) for x in line.strip().split(" ")])
    return formatted_data


def get_safe_reports_number(reports_formatted: list[list[int]]) -> int:
    safe_reports_number = 0
    for report in reports_formatted:
        error_count = 0
        is_increasing = None
        for i, number in enumerate(report):
            if i != 0:
                previous_is_increasing = is_increasing
                if report[i - 1] - number > 0:
                    is_increasing = False
                if report[i - 1] - number < 0:
                    is_increasing = True

                increase = abs(report[i - 1] - number)
                if is_increasing != previous_is_increasing and previous_is_increasing is not None:
                    error_count += 1

                if increase < 1 or increase > 3:
                    error_count += 1
        print(error_count)
        if error_count < 2:
            print(report)
            safe_reports_number += 1

    return safe_reports_number


def main():
    print(f"This many reports are safe: {get_safe_reports_number(format_input('./input_example.txt'))} ")


if __name__ == '__main__':
    main()
