import numpy as np

from algebra.euclidean import compose


def rotate_x(data, angle):
    vector = np.array(data)
    theta = np.radians(angle)

    rotation = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])

    return rotation.dot(vector)



def rotate_y(data, angle):
    vector = np.array(data)
    theta = np.radians(angle)

    rotation = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return rotation.dot(vector)



def rotate_z(data, angle):
    vector = np.array(data)
    theta = np.radians(angle)

    rotation  = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])
    return rotation.dot(vector)


def rotate(data, angle):
    x = lambda point: rotate_x(point, angle)
    y = lambda point: rotate_y(point, angle)
    z = lambda point: rotate_z(point, angle)
    rotation = compose(z, y, x)
    return rotation(data)

def rotate_xy(data, angle):
    x = lambda point: rotate_x(point, angle)
    y = lambda point: rotate_y(point, angle)
    rotation = compose(y, x)
    return rotation(data)


def rotate_xz(data, angle):
    x = lambda point: rotate_x(point, angle)
    z = lambda point: rotate_z(point, angle)
    rotation = compose( z, x)
    return rotation(data)

def rotate_yz(data, angle):
    y = lambda point: rotate_y(point, angle)
    z = lambda point: rotate_z(point, angle)
    rotation = compose(z, y)
    return rotation(data)

