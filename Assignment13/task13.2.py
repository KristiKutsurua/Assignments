def main():
    line_numbers = [2, 8, 10, 13, 17]

    with open("text_file.txt", "w") as file:
        for i in range(1, 19):
            if i in line_numbers:
                file.write(f"text_file: Line {i}\n")
            else:
                file.write("\n")

if __name__ == "__main__":
    main()

