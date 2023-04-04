# ex13 with exception handling for missing file
def main():
    print("Let's handle exceptions!")
    print("Run this WITHOUT the pelican file in the same directory.")
    try:
        with open('ERRORpelican.txt', 'r') as inF:
            for line in inF.readlines():
                if not line.isspace():
                    print(line.rstrip())
    except FileNotFoundError as e:
        print(f"Sorry! {e}")
    finally:
        print("Done.")
    print("Still in main().")
    print("Now try running it with the pelican file present.\n(Remove 'ERROR' from filename)")

if __name__ == "__main__":
    main()
