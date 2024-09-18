import numpy as np


from functools import reduce


def compose(*functions):
    def composed_function(arg):
        return reduce(lambda acc, f: f(acc), reversed(functions), arg)

    return composed_function

def rotate_x(data, angle):
    vector = np.array(data)
    theta = np.radians(angle)  # 45 degrees

    # Define the 3D rotation matrix around the x-axis
    rotation = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])

    return rotation.dot(vector)


def normalize(vector):
    v = np.array(vector)
    norm = np.linalg.norm(v)
    return v / norm

def normal(data):
    v = np.array(data)

def normal_vector(a, b):
    u = np.array(a)
    v = np.array(b)
    return np.cross(u, v)

def plane(data):
    points = np.array(data)
    centroid = np.mean(points, axis=0)
    center = points - centroid
    _, _, vh = np.linalg.svd(center)
    #The normal vector to the plane is the last row of V^T (vh.T)
    _normal = vh[-1]
    A, B, C = _normal
    D = -np.dot(_normal, centroid)
    return A, B, C, D

def normal_from_plane(plane):
    A, B, C, _ = plane
    n = np.array([A, B, C])
    return  n / np.linalg.norm(n)

normal_from_points = compose( normal_from_plane, plane)



def center_point(points):
    v = np.array(points)
    return np.mean(v, axis=0)
