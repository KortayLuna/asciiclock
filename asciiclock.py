import time

digits = [
    [
        "  ###  ",
        " #   # ",
        "#     #",
        "#     #",
        "#     #",
        " #   # ",
        "  ###  "
    ],
    [
        "   #   ",
        "  ##   ",
        "   #   ",
        "   #   ",
        "   #   ",
        "   #   ",
        " ##### "
    ],
    [
        "  ###  ",
        " #   # ",
        "     # ",
        "    #  ",
        "   #   ",
        "  #    ",
        " ######"
    ],
    [
        "  ###  ",
        " #   # ",
        "     # ",
        "   ##  ",
        "     # ",
        " #   # ",
        "  ###  "
    ],
    [
        "    #  ",
        "   ##  ",
        "  # #  ",
        " #  #  ",
        " ######",
        "    #  ",
        "    #  "
    ],
    [
        " ######",
        " #     ",
        " #     ",
        " ##### ",
        "     # ",
        " #   # ",
        "  ###  "
    ],
    [
        "  ###  ",
        " #   # ",
        " #     ",
        " ####  ",
        " #   # ",
        " #   # ",
        "  ###  "
    ],
    [
        " ######",
        "     # ",
        "    #  ",
        "   #   ",
        "  #    ",
        " #     ",
        " #     "
    ],
    [
        "  ###  ",
        " #   # ",
        " #   # ",
        "  ###  ",
        " #   # ",
        " #   # ",
        "  ###  "
    ],
    [
        "  ###  ",
        " #   # ",
        " #   # ",
        "  #### ",
        "     # ",
        " #   # ",
        "  ###  "
    ]
]

def get_ascii_digit(number):
    return digits[number]

def get_ascii_clock(hour, minute, second):
    time_str = f"{hour}:{minute}:{second}"

    ascii_digits = [get_ascii_digit(int(digit)) for digit in time_str if digit != ':']

    clock = [" "]*7

    for row in range(7):
        for digit_ascii in ascii_digits:
            clock[row] += digit_ascii[row] + " "
    return "\n".join(clock)

def main():
    while True:
        cTime = time.localtime()
        hour = cTime.tm_hour
        minute = cTime.tm_min
        second = cTime.tm_sec

        clock_ascii = get_ascii_clock(hour, minute, second)
        print(clock_ascii)
        time.sleep(1)


if __name__ == "__main__":
    main()