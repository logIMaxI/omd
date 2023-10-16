import csv


def get_data(path_to_file: str) -> list[dict]:
    """
    Function for reading data from the selected file
    ------
    :param path_to_file: path to read file
    :type path_to_file: str

    :rtype: list
    :return: list of personal info about each employee in dict form
    """
    with open(path_to_file, "r", encoding="UTF-8") as file:
        result_data = []
        data_frame = file.read().split("\n")
        keys_for_data = data_frame[0].split(";")
        for data_about_pers in data_frame[1:]:
            new_info_about_person = {
                key: elem
                for key, elem in zip(keys_for_data, data_about_pers.split(";"))
                if elem != ""
            }
            if new_info_about_person:
                result_data.append(new_info_about_person)

        return result_data


def preprocess_data(data: list[dict]) -> list[dict]:
    """
    Function for convert attributes "Оценка" and "Оклад" to float type
    ------
    :param data: data from the file about employees
    :type data: list

    :rtype: list
    :return: list of personal info about each employee in dict form but
    attributes "Оценка" and "Оклад" are float
    """
    for personal_info in data:
        personal_info["Оценка"] = float(personal_info["Оценка"])
        personal_info["Оклад"] = float(personal_info["Оклад"])

    return data


def show_menu() -> int:
    """
    Function for demonstrating menu to user
    ------
    :rtype: int
    :return: selected command
    """
    print(
        "Выберите интересующее действие:",
        "1.Вывод иерархии команд",
        "2.Сводный отчёт по департаментам",
        "3.Сохранение отчёта",
        "4.Выход из программы",
        sep="\n",
    )
    command = int(input())
    return command


def generate_summary_report(data: list[dict]) -> list[dict]:
    """
    Function for generating summary report based on gotten data: group by
    department counting aggregate functions (min, max, average, length) by
    salary
    ------
    :param data: data from the file about employees
    :type data: list

    :rtype: list
    :return: list with dictionaries which contains information about each
    departament: count of employees, min/average/max salary
    """
    depart_division = {pers_data["Департамент"]: [] for pers_data in data}
    for personal_data in data:
        depart_division[personal_data[
            "Департамент"]].append(personal_data["Оклад"])

    result = []
    for keys_pers_data in depart_division.keys():
        result.append(
            {
                "Департамент": keys_pers_data,
                "Численность": len(depart_division[keys_pers_data]),
                "Минимальный оклад": min(depart_division[keys_pers_data]),
                "Средний оклад": round(
                    sum(depart_division[keys_pers_data])
                    / len(depart_division[keys_pers_data]),
                    2,
                ),
                "Максимальный оклад": max(depart_division[keys_pers_data]),
            }
        )

    return result


def first_command(data: list[dict]) -> None:
    """
    Output hierarchy tree by departments
    ------
    :param data: data from file about employees
    :type data: list
    """
    depart_division = {pers_data["Департамент"]: set() for pers_data in data}
    for personal_data in data:
        depart_division[personal_data[
            "Департамент"]].add(personal_data["Отдел"])

    for department in depart_division.keys():
        print(f'Департамент "{department}"')
        print("|-", ",".join(depart_division[department]))


def second_command(data: list[dict]) -> None:
    """
    Output summary report by departments into console
    ------
    :param data: data from file about employees
    :type data: list
    """
    report = generate_summary_report(data)
    for current_info in report:
        info_for_display = [
            f"{key}: {current_info[key]}" for key in current_info.keys()
        ]
        info_for_display = "\n".join(info_for_display)
        print(info_for_display, end="\n\n\n")


def third_command(data: list[dict]) -> None:
    """
    Export summary report by departments into console to csv file
    ------
    :param data: data from file about employees
    :type data: list
    """
    report = generate_summary_report(data)
    print("Введите путь файла для сохранения отчёта")
    path_for_write = input()
    with open(path_for_write, "w", newline="") as write_file:
        writer = csv.writer(write_file, quotechar=";")
        writer.writerow(report[0].keys())
        for info in report:
            write_info = [str(elem) for elem in info.values()]
            writer.writerow(write_info)


def main() -> None:
    """
    Function modeling work of application
    """
    print("Введите путь до файла с данными по работникам")
    path_for_read = input()
    data = get_data(path_for_read)
    data = preprocess_data(data)
    command = show_menu()

    while command != 4:
        if command == 1:
            first_command(data)
        elif command == 2:
            second_command(data)
        elif command == 3:
            third_command(data)
        elif command == 4:
            break
        else:
            print("Введена неверная команда!")
        if command != 4:
            command = show_menu()


if __name__ == "__main__":
    main()
