def announce(f):
    def wrapper():
        print("About to run the functioon...")
        f()
        print("Done with the function...")
    return wrapper

@announce
def hello():
    print("Hello, World!")

hello()