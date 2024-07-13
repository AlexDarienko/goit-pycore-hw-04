def get_cats_info(path):
    try:
        with open(path, encoding='utf-8') as file:
            cats_info = []
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cat_dict = {"id": cat_id, "name": name, "age": age}
                    cats_info.append(cat_dict)
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
            return cats_info
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []

# Example usage:
path_to_file = "task02/cats_file.txt"
cats_info = get_cats_info(path_to_file)
print(cats_info)
