from src.index import is_valid_triangle

def main():
    a, b, c = map(int , input().split())
    print(is_valid_triangle(a, b, c))
if __name__ == '__main__':
    main()