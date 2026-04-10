def main():
    n = int(input("how many note do you have?: "))
    notes = []
    for i in range(n):
        val = int(input("write the note note: "))
        notes.append(val)
    average = sum(notes) / len(notes)
    print("the average of notes is: ", average)


if __name__ == '__main__':
    main()