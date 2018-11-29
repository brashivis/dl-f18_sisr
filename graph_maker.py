#!/usr/bin/python3

import sys
import matplotlib.pyplot as plt

def graph(filename, title):
    with open(filename) as f:
        line = f.readline()
        iters = []
        losses = []
        count = 0
        while (line != ''):
            if (line[0] == '[') and (line[1:6] != "Epoch") and (line[1:6] != "DIV2K"):
                count += 16
                iters.append(count)
                losses.append(float(line.split('\t')[1][6:-1]))
            line = f.readline()
    
    plt.xlabel("Iterations")
    plt.ylabel("MSE Loss")
    plt.title("{} Training Loss".format(title.capitalize()))
    plt.plot(iters, losses)
    plt.savefig("{}.png".format(title))

if __name__ == "__main__":
    print("Graphing {} and saving as {}.png".format(sys.argv[1], sys.argv[2]))
    graph(sys.argv[1], sys.argv[2])