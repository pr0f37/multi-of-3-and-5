def main(N: int) -> int:
    return sum(i for i in range(N) if i % 3 == 0 or i % 5 == 0)


if __name__ == "__main__":
    T: int = int(input("How many test cases?\n"))
    for N in [int(input()) for _ in range(T)]:
        print(main(N))
