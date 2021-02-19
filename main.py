import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('classic')


class Board:
    def __init__(self, x_axis_size, y_axis_size):
        self.x_axis_size = x_axis_size
        self.y_axis_size = y_axis_size
        self.state = pd.DataFrame(np.zeros(shape=(y_axis_size, x_axis_size), dtype=int))

    def fill_random(self):
        self.state = pd.DataFrame(np.random.randint(0, 2, (self.y_axis_size, self.x_axis_size), dtype=int))

    def transform_to_sum(self):
        board_left = self.state.shift(periods=-1, axis=1, fill_value=0)
        board_right = self.state.shift(periods=1, axis=1, fill_value=0)
        board_up = self.state.shift(periods=-1, axis=0, fill_value=0)
        board_down = self.state.shift(periods=1, axis=0, fill_value=0)
        board_left_up = board_left.shift(periods=-1, axis=0, fill_value=0)
        board_left_down = board_left.shift(periods=1, axis=0, fill_value=0)
        board_right_up = board_right.shift(periods=-1, axis=0, fill_value=0)
        board_right_down = board_right.shift(periods=1, axis=0, fill_value=0)
        self.state = self.state + board_left + board_right + board_up + board_down + \
            board_left_up + board_left_down + board_right_up + board_right_down

    def change_state(self, nparray):
        self.state = pd.DataFrame(nparray)
        self.x_axis_size = len(self.state.columns)
        self.y_axis_size = len(self.state.index)

    def next_state(self, toprint=0):
        board_sum = Board(self.x_axis_size, self.y_axis_size)
        board_sum.state = self.state
        board_sum.transform_to_sum()
        for x in range(0, len(self.state.columns)):
            board_sum.state.loc[(
                                        (((board_sum.state[x] < 3) | (board_sum.state[x] > 4)) & (
                                                    self.state[x] == 1)) |
                                        ((board_sum.state[x] != 3) & (self.state[x] == 0))
                                ), x] = 0
            board_sum.state.loc[
                (((board_sum.state[x] >= 3) & (board_sum.state[x] <= 4) & (self.state[x] == 1)) |
                 ((board_sum.state[x] == 3) & (self.state[x] == 0))), x] = 1
        self.state = board_sum.state
        if toprint != 0:
            print(self.state, '\n')

    def get_coord_x(self):
        x = []
        for i in zip(*np.where(self.state.values == 1)):
            x.append(i[0])
        return x

    def get_coord_y(self):
        x = []
        for i in zip(*np.where(self.state.values == 1)):
            x.append(i[1])
        return x


def live_plotter(df_board, steps, pause_sec=0.1):
    fig, ax = plt.subplots(1, 1)
    plt.ion()
    plt.show()
    plt.grid(1)
    for k in range(0, steps, 1):
        ax.clear()
        x = df_board.get_coord_x()
        y = df_board.get_coord_y()
        ax.scatter(x, y, s=40)
        plt.xlim(0, len(df_board.state.columns)-1)
        plt.ylim(len(df_board.state.index)-1, 0)
        df_board.next_state()
        plt.pause(pause_sec)


board1 = Board(9, 9)
board1.change_state(np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]).T.tolist())

board2 = Board(19, 19)
board2.fill_random()

if __name__ == '__main__':
    live_plotter(board2, steps=100)  # this is random m x n board
#    live_plotter(board1, steps=30)  # this is a preset board
