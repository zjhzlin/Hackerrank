def count_substring(string, sub_string):
    start_index = 0
    count = 0
    while True:
        new_string = string[start_index:len(string)]
        if sub_string in new_string:
            count += 1
            start_index += new_string.find(sub_string) + 1
        else:
            break
    return count


if __name__ == '__main__':
    string = "ABCDCDC"
    sub_string = "CDC"

    count = count_substring(string, sub_string)
    print(count)