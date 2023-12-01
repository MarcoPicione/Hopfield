#!/usr/bin/env python

import numpy as np
import tkinter as tk
import random
import numbers_dict
import matplotlib.pyplot as plt

# GRAPHICS

def create_circle(canvas, x0, y0, x1, y1, fill):
    if fill:
        canvas.create_oval(x0, y0, x1, y1, outline='black', width = 2, fill='black')
    else:
        canvas.create_oval(x0, y0, x1, y1, outline='black', width = 2)

def plot_stuff(width, num, initial, active):

    if np.sum(active) > 0: active = -1 * active

    # Calculus
    space = 10
    margin = 50
    blank = 50

    n = int(np.sqrt(num))
    dim = int((width - blank - space * (n - 1) - 2 * margin) / n)
    step = dim + space

    # Draw
    root = tk.Tk()
    canvas = tk.Canvas(root, width = width * 2, height = width)
    canvas.pack()

    index = 0
    for j in range(0, n):
        for i in range(0, n):
            create_circle(canvas, margin + step * i, margin + step * j, margin + step * i + dim, margin + step * j + dim, initial[index]+1)
            index +=1

    hole = width + blank
    index = 0
    for j in range(0, n):
        for i in range(0, n):
            create_circle(canvas, hole + margin + step * i,margin + step * j, hole + margin + step * i + dim, margin + step * j + dim, active[index]+1)
            index +=1

    canvas.create_line(width-2*margin+space, (width - margin) / 2, width+margin+blank-space, (width - margin) / 2, arrow=tk.LAST)

    root.mainloop()

# NETWORK    

class hopfield(object):
    def __init__(self, size, dt = None, tau = None, temperature = None, learningRate = None, alpha = None):
        self.size = size
        if learningRate is None: learningRate = 1
        self.learningRate = learningRate
        if tau is None: tau = 1
        self.tau = tau
        if dt is None: dt = 1
        self.dt = dt
        if temperature is None: temperature = 0
        self.temperature = temperature
        if alpha is None: alpha = 1
        self.alpha = alpha

        self.weights = np.zeros((size, size))
        self.patterns = []
        self.state = np.zeros(size)
        self.state_rounded = np.zeros(size)
        self.collective_variable = []
        
    def add_pattern(self, pattern):
        self.weights = (self.weights + np.outer(pattern, pattern)) * self.learningRate
        self.patterns.append(pattern)
        for i in range(self.size):
            self.weights[i][i] = 0
        
    def activation(self, i):
        return self.act(np.dot(self.weights[i], self.state))

    def update(self, iterations, state):

        self.state = state.astype(np.float64)
        for it in range(iterations):
            for i in range(self.size):
                self.state[i] =  self.state[i] - ((self.state[i] - self.activation(i)) * self.dt / self.tau) + np.sqrt(2 * self.temperature * self.dt) * np.random.normal()
            self.collective_variable.append(self.evaluate_collective_variable())

        self.state_rounded = np.where(self.state>=0, 1, -1)

    def act(self, x):
        return np.tanh(x)
    
    def distance(self, a, b):
        return np.linalg.norm(a-b)

    def evaluate_collective_variable(self):
        return -1 *np.exp(-self.distance(self.patterns[0], self.state) / self.alpha) + 1 * np.exp(-self.distance(self.patterns[1], self.state) / self.alpha)


# MAIN

def main():

    n = 9
    h = hopfield(n, temperature=0.15, dt=1/100)
    d = numbers_dict.d

    h.add_pattern(d['one'+str(n)])
    h.add_pattern(d['two'+str(n)])
    # h.add_pattern(d['three'+str(n)])
    # h.add_pattern(d['four'+str(n)])
    # h.add_pattern(d['five'+str(n)])
    # h.add_pattern(d['six'+str(n)])
    # h.add_pattern(d['seven'+str(n)])
    # h.add_pattern(d['eight'+str(n)])
    # h.add_pattern(d['nine'+str(n)])

    state = []
    for i in range(n):
        state.append(random.choice([-1, 1]))
    state = np.array(state)

    # state = d['nine81']

    h.update(100000, state)

    width = 400
    plot_stuff(width, n, state, h.state_rounded)

    plt.figure()
    plt.plot(range(len(h.collective_variable)), h.collective_variable)
    plt.xlabel('Iteration')
    plt.ylabel('Collective variable')
    plt.show()


if __name__== '__main__':
    main()

# -1exp(-dist1 alpha) + 1exp(-dist2 alpha)
    


