n = int(input())

polyhedrons_sides = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}

sides_counter = 0

for input_figure in range(n):
    current_figure = input()
    sides_counter += polyhedrons_sides[current_figure]

print(sides_counter)