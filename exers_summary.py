def longest_name(file_path):
    with open(file_path, "r") as f:
        return max(f.readlines(), key=len).strip()


def sum_len_names(file_path):
    with open(file_path, "r") as f:
        return sum([len(string.strip()) for string in f.readlines()])


def shortest_names(file_path):
    with open(file_path, "r") as f:
        f = sorted(f.readlines(), key=len)
        return "".join([name for name in f if len(name.strip()) == len(f[0])][::-1])


def create_length_file(file_path):
    with open(file_path, "r") as f1:
        with open("name_length.txt", "w") as f2:
            f2.write("".join(
                [str(len(name) - 1) + '\n' if name.endswith('\n') else str(len(name)) for name in f1.readlines()]))


def show_name(file_path, length):
    with open(file_path, "r") as f:
        return "".join([name for name in f.readlines() if len(name) == length + 1])


def main():
    print(longest_name("names.txt"))
    print(sum_len_names("names.txt"))
    print(shortest_names("names.txt"))
    print(create_length_file("names.txt"))
    print(show_name("names.txt", int(input("enter name length: "))))


if __name__ == "__main__":
    main()
