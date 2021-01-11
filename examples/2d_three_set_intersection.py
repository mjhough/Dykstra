import numpy as np
import dykstra

# Define projection functions
def p_box(x,l,u):
    return np.minimum(np.maximum(x,l), u)

def p_ball(x,c,r):
    return c + (r/np.max([np.linalg.norm(x-c),r]))*(x-c)

def p_halfspace(x,a,b):
    return x - a*np.maximum(a.dot(x) - b,0)/a.dot(a)

# Generate projection functions
ball_c = [1,1]
ball_r = 2
pball = lambda x: p_ball(x,np.array(ball_c),ball_r)

box_l = np.array([-1,-1])
box_u = np.array([1,1])
pbox = lambda x: p_box(x,box_l,box_u)

a = [1,1]
bconst = 0.2
phalf = lambda x: p_halfspace(x,np.array(a),bconst)

# Use Dykstra's algorithm to project onto the intersection
#  np.random.seed(12)
start = np.random.uniform(low=-10,high=80, size=(2,))
x_pred = dykstra.project([pbox,pball,phalf], start, max_iter=10000, tol=1.0e-20)
print("Start:", start)
print("Pred:", x_pred)

if x_pred[0]+x_pred[1] <= 0.2 and (box_l[0] <= x_pred[0] <= box_u[0] and box_l[1] <= x_pred[1] <= box_u[1]) and ((x_pred[0]-1)**2 + (x_pred[1]-1)**2 <= 2**2):
    print("In constraint set")
else:
    # Print out constraints and values x_pred obtains to determine the error
    print(f'x+y = {x_pred[0]+x_pred[1]} (0.2), point: ({x_pred[0]},{x_pred[1]}), box upper: {box_u}, box lower: {box_l}, (x-1)^2+(y-1)^2 = {(x_pred[0]-1)**2 + (x_pred[1]-1)**2} (<=4)')
