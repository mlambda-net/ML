from algebra.rotation_3d import rotate_xy, rotate_xz, rotate_yz, rotate, rotate_x, rotate_y, rotate_z
from algebra.euclidean import  normal_from_points,center_point
from plot.coordinates import AxisPlane
from plot.shape import Sphere, Cube, Point, Vector, Plane, Line, Polygon
from plot.viewer import Viewer


#https://technology.cpm.org/general/3dgraph/

def main():
    viewer = Viewer(size=[1920,1080])
    viewer.draw(Point(color='pink', size=5))
    #viewer.draw(Point([1,1,1], 10, color='red'))
    #viewer.draw(Point([2, 1, 1], 10, color='green'))

    #viewer.draw(Point([1, 0, 0], 10, color='yellow'))
    #viewer.draw(Point([0, 1, 0], 10, color='yellow'))
    #viewer.draw(Point([0, 0, 1], 10, color='yellow'))

    #viewer.draw(Sphere())
    #viewer.draw(Plane( orientation='x'))
    #viewer.draw(Plane( orientation='y'))
    #viewer.draw(Plane( orientation='z'))
    #viewer.draw(Vector( destination=[0,1,0]))


    facet = [
            [2, 1, 1],  # Vertex 0
            [2, -1, 1],  # Vertex 1
            [1, -1, 2],  # Vertex 2
            [1, 1, 2]  # Vertex 3
        ]


    viewer.draw(AxisPlane(axis='x'))

    rotated = [ rotate_y(face, 60) for face in facet]

    viewer.draw(Polygon(facet, color='blue'))
    viewer.draw(Polygon(rotated, color='red'))

    viewer.draw(Vector(origin=center_point(facet), destination= normal_from_points(facet)))
    viewer.draw(Vector(origin=center_point(rotated), destination=normal_from_points(rotated)))


    vector = [1,0,0]

    viewer.draw(Vector(destination=vector, color='red'))
    viewer.draw(Vector(destination=rotate_z(vector, 90), color='blue'))
    viewer.draw(Vector(destination=rotate_y(vector, 90), color='green'))



    #viewer.draw(Line([0,0,0], [1,1,1]))
    viewer.run()

if __name__ == '__main__':
    main()
