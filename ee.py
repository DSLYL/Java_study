import random

ss1 = 2
print(ss1)
for i in range(100):
    print(random.randint(1, 10))


def main():
    number = 4
    if number > 2:
        print("哈哈。答对了")
    else:
        print("哈哈。答错了")


if __name__ == "__main__":
    main()
