def read_file(file_name):
    with open(file_name) as f:
        try:
            f.read()
            print('__CONTENT_START__This is the content from the file!__CONTENT_END__')
        except FileNotFoundError:
            print("__CONTENT_START____NO_SUCH_FILE____CONTENT_END__ ")
        # else:
        #     print("Number of lines in file: ", len(f.readlines()))
        # finally:
        #     print("Function done executing, weather number of lines in file was printed or not.")


# print(read_file("file_does_not_exist.txt"))
print(read_file("names.txt"))
