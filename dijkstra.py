INF = float('inf')


class Vertex:
    def __init__(self, row, col, cost, prev_vertex=None):
        self.row = row
        self.col = col
        self.cost = cost
        self.prev_vertex = prev_vertex


def find_shortest_path(board):
    rows = len(board)
    cols = len(board[0])

    costs = [[INF] * cols for _ in range(rows)]
    prev_vertices = [[None] * cols for _ in range(rows)]

    x_row, x_col = INF, INF
    breakk = False
    # Szukanie pierwszego X
    for row in range(rows):
        if breakk:
            break
        for col in range(cols):
            if board[row][col] == 'X':
                x_row, x_col = (row, col)
                breakk = True
                break

    vertices_to_visit = [Vertex(x_row, x_col, 0)]

    while vertices_to_visit:
        # Znalezienie wierzchołka o najmniejszym koszcie
        min_cost = INF
        min_vertex_index = None
        for i in range(len(vertices_to_visit)):
            if vertices_to_visit[i].cost < min_cost:
                min_cost = vertices_to_visit[i].cost
                min_vertex_index = i
        vertex = vertices_to_visit.pop(min_vertex_index)

        row, col, cost = vertex.row, vertex.col, vertex.cost

        if cost > costs[row][col]:
            continue

        costs[row][col] = cost

        prev_vertices[row][col] = vertex.prev_vertex

        # Sprawdzanie sąsiednich pól (prawo, lewo, góra, dół)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row = row + dx
            new_col = col + dy

            # Jeśli współrzędne są na planszy i pole nie jest spacją
            if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] != ' ':
                # Koszt przejścia do sąsiedniego pola
                add_cost = int(board[new_row][new_col]) if board[new_row][new_col] != 'X' else 0
                new_cost = cost + add_cost
                new_vertex = Vertex(new_row, new_col, new_cost, prev_vertex=vertex)
                vertices_to_visit.append(new_vertex)

    return costs, prev_vertices


def print_path(board, prev_ver_board):

    rows = len(board)
    cols = len(board[0])
    path_board = []
    for i in range(rows):
        path_board.append([])
        for j in range(cols):
            path_board[i].append(' ')

    # Szuknie drugiego X
    x_row, x_col = INF, INF
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 'X':
                x_row, x_col = row, col

    # Jakby rekurencyjnie od drugiego x przechodzimy po poprzednich wierzcholkach
    while True:
        path_board[x_row][x_col] = board[x_row][x_col]
        if not prev_ver_board[x_row][x_col]:
            break
        x_row, x_col = prev_ver_board[x_row][x_col].row, prev_ver_board[x_row][x_col].col

    return path_board

