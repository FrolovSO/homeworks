for seq in range(100):
    if seq % 3 == 0 and seq % 5 == 0:
        print("FuzzBuzz")
    elif seq % 3 == 0:
        print("Fuzz")
    elif seq % 5 == 0:
        print("Buzz")
    else:
        print(seq)
