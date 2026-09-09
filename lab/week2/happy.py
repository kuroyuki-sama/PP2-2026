def birth(name):
    print("안녕하세요")
    print(name + " 님의 생일을 축하합니다.")
    return None

def test():
    birth("승균")
    birth("권우")
    birth("찬승")
    birth("강민")

def test2():
    names = ["승균", "권우", "찬승", "강민"]
    for name in names:
        birth(name)

def test3():
    birth(3.1415)
    birth(100)
    birth([1,2,3])

if __name__ == "__main__":
    # test()
    # test2()
    test3()
