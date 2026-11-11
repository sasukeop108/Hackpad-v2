import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D4 , board.D5 , board.D6 , board.D7)
keyboard.row_pins = (board.D0 , board.D1 , board.D2 , board.D3)

keyboard.keymap = [
    [KC.CTRL , KC.C , KC.W , KC.A , KC.S , KC.D , KC.E , KC.F , KC.L , KC.M , KC.END , KC.ESC , KC.R , KC.Q , KC.DEL , KC.HOME]
]

if __name__ == '__main__':
    keyboard.go()