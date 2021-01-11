# Dykstra's algorithm

[![PyPI version](https://badge.fury.io/py/Dykstra.svg)](https://badge.fury.io/py/Dykstra)

This repo implements Dykstra's projection algorithm. Not to be confused with Dijkstra's shortest path algorithm.

Dykstra's algorithm solves the projection problem, i.e. finding the closest feasible point to any given point that may not be feasible,
onto the intersection of finitely many closed convex sets in a Hilbert space.

Given finitely many closed convex sets `C[i]`, we define the intersection of these sets as `S = intersect(C[0], C[1], ...)`. Then for an input point `x0`
that may or may not be feasible, Dykstra maps this point to the nearest point in `S`.

The code implementation of this is a function `dykstra.project(P,x0,max_iter=1000,tol=1e-6)` that takes in as inputs a list of projection functions and the point to project, and
returns the closest feasible point.

This version of Dykstra's algorithm uses the robust stopping criteria introduced in [3].

### Installation
You can install using pip:
```
pip install dykstra
```

### Usage and examples
```
import dykstra # import package

...

# call the projection function
x_pred = dykstra.project(x0,[p1,p2,...])
```
For a more detailed example see the examples folder.


References:
```
[1] Dykstra R.L., 1983. An algorithm for restricted least squares regression.
[2] Boyle J.P., Dykstra R.L., 1986. A Method for Finding Projections onto the Intersection of Convex Sets in Hilbert Spaces.
[3] Birgin E.G., Raydan M., 2004. Robust stopping criteria for Dykstra's algorithm.
```
