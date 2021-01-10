from NodeData import Node
from GeoLocation import GeoLocation


class EdgeData:
    """
    This class represents the set of operations applicable on a
    directional edge(src,dest) in a (directional) weighted graph.
    """

    def __init__(self, src: int, dest: int, weight: float = 0, info: str = ""):
        self.__src = src
        self.__dest = dest
        self.__weight = weight
        self.__info = info

    def get_src(self) -> int:
        """
        This function is responsible to return the id of the source node of this edge.
        @return: the id of the source node of this edge.
        """
        return self.__src

    def get_dest(self) -> int:
        """
        This function is responsible to return the id of the destination node of this edge
        @return: the id of the destination node of this edge.
        """
        return self.__dest

    def get_weight(self) -> float:
        """
        This function is responsible to return the weight of this edge (positive value).
        @return: the weight of this edge.
        """
        return self.__weight

    def get_info(self) -> str:
        """
        This function is responsible to return the remark (meta data) associated with this edge.
        @return: the remark (meta data) associated with this edge.
        """
        return self.__info

    def set_info(self, info: str):
        """
        This function is responsible to allows changing the remark (meta data) associated with this edge.
        @param info - the new remark (meta data) associated with this edge.
        """
        self.__info = info

    def __str__(self) -> str:
        """
        This function is responsible to return the edge data in a string format.
        @return the edge data in a string format.
        """
        return "src: %d, dest: %d, weight: %f" % (self.__src, self.__dest, self.__weight)

    def __repr__(self):
        return str(self)
