import hellomodule

def main():
    print("Hello, World!")
    hellomodule.ModuleHelloWorld()


if __name__ == "__main__":
    print("hello-04.py directory")
    print(dir())
    print(__name__)
    print("hellmodule.py directory")
    print(dir(hellomodule))
    print(hellomodule.__name__)
    main()