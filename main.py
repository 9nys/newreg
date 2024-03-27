def compare_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r', encoding='utf-8') as file1, \
             open(file2_path, 'r', encoding='utf-8') as file2:
            file1_lines = file1.readlines()
            file2_lines = file2.readlines()

            unique_lines = set(file1_lines) - set(file2_lines)

            if unique_lines:
                print("Рядки, які є у першому файлі, але відсутні у другому:")
                for line in unique_lines:
                    print(line.strip())
            else:
                print("Усі рядки з першого файлу присутні у другому.")
    except FileNotFoundError as e:
        print(f"Файл не знайдено: {e.filename}")
    except Exception as e:
        print(f"Виникла помилка: {e}")


file1_path = input("Введіть шлях до першого файлу: ")

file2_path = input("Введіть шлях до другого файлу: ")

compare_files(file1_path, file2_path)