import random

if __name__ == "__main__":
    print("Here is a very thoughtful remark for today:")
    with open("remarks.txt") as f:
        print(random.choice(f.readlines()))
