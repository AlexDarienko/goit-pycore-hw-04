def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total += float(salary)
                    count += 1
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
            if count == 0:
                return 0, 0
            average = total / count
            return total, average
    except FileNotFoundError:
        print(f"File not found: {path}")
        return 0, 0

# Example usage:
path_to_file = "task01/salary_file.txt"
total, average = total_salary(path_to_file)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
