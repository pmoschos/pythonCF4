def department_id_generator(department):
    """Generate unique IDs for students based on department"""
    last_id = 0

    def generate_id():
        nonlocal last_id
        last_id += 1
        return f"{department}-{last_id}", last_id
    
    return generate_id

python_id_gen = department_id_generator("Python")
android_id_gen = department_id_generator("Android")

print(python_id_gen()) # Python-1
print(python_id_gen()) # Python-2
print(android_id_gen()) # Android-1
print(python_id_gen()) # Python-3