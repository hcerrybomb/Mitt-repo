with open("C:\\Users\\wista002\\Mitt-repo\\Mitt-repo\\python-development\\stf\\stf-IT2\\reelle-datasett\\rektangeler.txt") as f:
    for linje in f:
        sidekanter = linje.rstrip().split(',')
        print(sidekanter)
    