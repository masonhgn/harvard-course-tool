def reorder_name(name_str):
    parts = name_str.split(',', 1)
    if len(parts) != 2:
        return name_str
    last_name, first_name = parts
    return f"{first_name.strip()} {last_name.strip()}"

name = "Grimaud,Julien Franck, Roger"
print(reorder_name(name))