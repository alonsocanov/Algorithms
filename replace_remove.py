def replaceRemove(s):
    write_idx, a_count = 0, 0
    for i in range(len(s)):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1
    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    while cur_idx >= 0:
        if s[cur_idx] == 'a':
            s[write_idx - 1:write_idx + 1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return final_size


def main():
    my_array = ['a', 'c', 'a', 'a']
    print(my_array)
    replaceRemove(my_array)
    print(my_array)


if __name__ == '__main__':
    main()
