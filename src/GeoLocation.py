class GeoLocation:
    """
    This class is responsible to represents the set coordinates applicable on
    nodes in a (directional) weighted graph.
    """

    def __init__(self, x: float = None, y: float = None, z: float = None):
        self.__x = x
        self.__y = y
        self.__z = z

    def get_x(self) -> float:
        """
        This function is responsible to return the X coordinate associated with this location.
        @:return the X coordinate associated with this location.
        """
        return self.__x

    def get_y(self) -> float:
        """
        This function is responsible to return the Y coordinate associated with this location.
        @:return the Y coordinate associated with this location.
        """
        return self.__y

    def get_z(self) -> float:
        """
        This function is responsible to return the Z coordinate associated with this location.
        @:return the Z coordinate associated with this location.
        """
        return self.__z

    def distance(self, location) -> float:
        """
        This function is responsible to return the distance between a given coordinates and the associated location.
        @:param location - given coordinates to measure the distance from.
        @:return the distance between a given coordinate and the associated location.
        """
        return ((self.__x - location.get_x()) ** 2 + (self.__y - location.get_y()) ** 2 + (self.__z - location.get_z()) ** 2) ** 0.5

    def __str__(self):
        """
        This function is responsible to return the coordinates in a string format.
        @return the coordinates in a string format.
        """
        return "X: %f, Y: %f, Z: %f" % (self.__x, self.__y, self.__z)

    def __repr__(self):
        return str(self)