try:
    file = open("testFile.txt", "w")
    file.write("Written to file")
except TypeError:
    print("Ypu have a type error")
except OSError:
    print("You have an OS error")

finally:
    print("I am always going to run") 