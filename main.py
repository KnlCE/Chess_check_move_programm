def check_move_possibility_static_figure():
    for move in static_figure_dictionary[f"{figure}"]:
        if x_diff == int(move[0]) and y_diff == int(move[1]):
            return True
    return False


def check_move_possibility_dynamic_figure():
    if (figure == "ладья" and (x_diff == 0 or y_diff == 0)) or \
            (figure == "слон" and x_diff == y_diff) or \
            (figure == "королева" and (x_diff == 0 or y_diff == 0 or x_diff == y_diff)):
        return True
    return False


coord = input("Введите ход в формате A1-B2: ").split("-")
figure = input("Введите название фигуры (пешка, ладья,...): ")

static_figure_dictionary = {
    "пешка": ["01", "02"],
    "конь": ["21", "12"],
    "король": ["10", "01", "11"]
}
dynamic_figure_list = [
    "ладья",
    "слон",
    "королева",
]
alfabet = ["A", "B", "C", "D", "E", "F", "G", "H"]

coord_start = [alfabet.index(coord[0][0]) + 1, int(coord[0][1])]
coord_end = [alfabet.index(coord[1][0]) + 1, int(coord[1][1])]

x_diff = abs(coord_end[0] - coord_start[0])
y_diff = abs(coord_end[1] - coord_start[1])

if figure in static_figure_dictionary:
    print(check_move_possibility_static_figure())
elif figure in dynamic_figure_list:
    print(check_move_possibility_dynamic_figure())
else:
    print("Такой фигуры нет")
