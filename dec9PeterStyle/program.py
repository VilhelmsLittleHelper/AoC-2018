# Från att ha tittas på Peters kod

from collections import deque


def play_game(players, max_marble):
    game_board = deque([0])
    s = [0 for apa in range(players)]
    i = 1

    while i < max_marble:
        if i % 23 == 0:
            game_board.rotate(7)
            value = game_board.pop()
            index = (i - 1) % players
            s[index] += i + value
            game_board.rotate(-1)
        else:
            game_board.rotate(-1)
            game_board.append(i)
        i += 1

    high_score = max(s)
    print(high_score)

play_game(10, 30)
play_game(10, 1618)
play_game(13, 7999)
play_game(17, 1104)  # Får fel på denna
play_game(21, 6111)
play_game(30, 5807)

play_game(462, 71938 * 100)
