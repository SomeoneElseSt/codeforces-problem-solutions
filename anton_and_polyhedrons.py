n = int(input())

sides_counter = 0

for figure in range(n):
    current_figure = input()

    if current_figure == "Tetrahedron":
        sides_counter += 4
    elif current_figure == "Cube":
        sides_counter += 6
    elif current_figure == "Octahedron":
        sides_counter += 8 
    elif current_figure == "Dodecahedron":
        sides_counter += 12
    elif current_figure == "Icosahedron":
        sides_counter += 20

print(sides_counter)