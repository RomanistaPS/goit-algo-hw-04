from pathlib import Path

file_path = Path("salary_file.txt")

def total_salary(path):
    total_salary_sum = 0
    employee_count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                name, salary = line.split(',')
                total_salary_sum += int(salary)
                employee_count += 1

        if employee_count == 0:
            return 0, 0

        average_salary = total_salary_sum // employee_count
        return total_salary_sum, average_salary

    except FileNotFoundError:
        print("Файл не знайдено")
        return 0, 0

    except Exception as e:
        print(f"Помилка: {e}")
        return 0, 0


total, average = total_salary(file_path)

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")