size=5
alphabet = 'abcdefghijklmnopqrstuvwxyz'
pattern = alphabet[:size]  # if size = 5 ; then 'abcde'

row_length = size * 2 - 1  # 9 rows/lines in total
col_length = 2 * row_length - 1  # 17 characters per row
size_until_mid = (row_length-1)//2

down = []

   # top               beginning to mid
for i in range(1, size_until_mid + 1):
                                          # considering i =4
    r_part = pattern[len(pattern) - i:]  # bcde
    l_part = r_part[::-1][:i-1]         # edc
    all_part = l_part + r_part    # edc + bcde = edcbcde
    joining = "-".join(all_part)  # e-d-c-b-c-d-e
    final = joining.center(col_length, '-')  # putting dashes
    # becomes like this:    --e-d-c-b-c-d-e--

    down.append(final)     # adding to list (for bottom part)
    print(final)

    # middle
print("-".join(pattern[::-1]+pattern[1:]))

    # down           mid to down (same length as begin to mid)
for _ in range(size_until_mid):
    print(down.pop())  # .pop > first in last out (FIFO)
        # thus, no need to reverse it
