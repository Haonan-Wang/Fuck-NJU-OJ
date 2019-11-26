import math
import itertools


if __name__ == "__main__":
    T = int(input())
    while T:
        T -= 1

        dots = [list(map(float, dot.split())) for dot in input().split(',')]

        min_dis = math.inf
        nearest_dot_pairs = []
        for dot_pair in itertools.combinations(dots, 2):
            dot_pair = list(dot_pair)
            dot_pair.sort()

            coord1, coord2 = dot_pair
            dis = (coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2
            if dis == min_dis:
                nearest_dot_pairs.append(dot_pair)
            elif dis < min_dis:
                min_dis = dis
                nearest_dot_pairs = [dot_pair]

        nearest_dot_pairs.sort(key=lambda dot_pair: dot_pair[0])
        dots = []
        for dot_pair in nearest_dot_pairs:
            for dot in dot_pair:
                for i, coord in enumerate(dot):
                    if int(coord) == coord:
                        dot[i] = int(coord)
                dots.append(' '.join(map(str, dot)))
        print(','.join(dots))
