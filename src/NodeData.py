from GeoLocation import GeoLocation


class Node:
    """
    This class represents the set of operations applicable on a
    node (vertex) in a (directional) weighted graph.
    """

    def __init__(self, key: int, info: str = "none", tag: int = 0, weight: float = 0, location: GeoLocation = GeoLocation()):
        self.__key = key
        self.__info = info
        self.__tag = tag
        self.__weight = weight
        self.__location = location
        self.__neighbors = []
        self.__dest = []

    def add_neighbor(self, key: int):
        """
        This function is responsible to append a new neighbor key into the neighbor list.
        @:param key - the neighbor id.
        """
        self.__neighbors.append(key)

    def add_dest(self, key: int):
        """
        This function is responsible to append a new destination key into the destination list.
        @:param key - the destination id.
        """
        self.__dest.append(key)

    def remove_neighbor(self, key: int):
        """
        This function is responsible to remove a neighbor key into the neighbor list.
        @:param key - the neighbor id.
        """
        self.__neighbors.remove(key)

    def remove_dest(self, key: int):
        """
        This function is responsible to remove a destination key into the destination list.
        @:param key - the destination id.
        """
        self.__dest.remove(key)

    def get_dest(self) -> list:
        """
        This function is responsible to return the destination list associated with this node as destination.
        @:return the destination list (id) associated with this node.
        """
        return self.__dest

    def get_neighbors(self) -> list:
        """
        This function is responsible to return the neighbors list associated with this node as source.
        @:return the neighbors list (id) associated with this node.
        """
        return self.__neighbors

    def get_key(self) -> int:
        """
        This function is responsible to return the key (id) associated with this node.
        @:return the key (id) associated with this node.
        """
        return self.__key

    def get_location(self) -> GeoLocation:
        """
        This function is responsible to return the location of this node.
        @:return the location associated with this node.
        """
        return self.__location

    def set_location(self, location: GeoLocation):
        """
        This function is responsible to change this node's location.
        @param location - new location (position) of this node.
        """
        self.__location = location

    def get_weight(self) -> float:
        """
        This function is responsible to return the weight of this node.
        @:return the weight associated with this node.
        """
        return self.__weight

    def set_weight(self, weight: float):
        """
        This function is responsible to change the weight associated with this node.
        @param weight - the new weight in the node.
        """
        self.__weight = weight

    def get_info(self) -> str:
        """
        This function is responsible to return the remark (meta data) associated with this node.
        @:return the remark (meta data) associated with this node.
        """
        return self.__info

    def set_info(self, info: str):
        """
        This function is responsible to change remark (meta data) associated with this node.
        @param info - the new remark (meta data) in the node.
        """
        self.__info = info

    def get_tag(self) -> int:
        """
        This function is responsible to return temporal data (aka color: e,g, white, gray, black / 0, 1, 2),
        which can be used be algorithms.
        @:return the tag associated with this node.
        """
        return self.__tag

    def set_tag(self, tag: int):
        """
        This function is responsible to setting the "tag" value for temporal marking an node.
        @:param tag - the new tag value associated with this node.
        """
        self.__tag = tag

    def __str__(self):
        """
        This function is responsible to return the node data in a string format.
        @return the node data in a string format.
        """
        return str(self.__key)
        #return "ID: %d, info: %s, tag: %d, weight: %f, location: %s" \
        #       % (self.__key, self.__info, self.__tag, self.__weight, str(self.__location))

    def __repr__(self):
        return str(self)

