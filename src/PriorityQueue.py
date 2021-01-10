class PriorityQueue:
    """This class represents prioritised queue."""

    def __init__(self):
        self.__pq = []

    def pop(self) -> object:
        """
        This function is responsible to return the first element in the queue and remove it.
        @return the first element in the queue.
        """
        return self.__pq.pop(0)[1]

    def push(self, element: object):
        """
        This function is responsible to put a new element in its correct order in the queue.
        @:param element - the element implemented into the queue.
        """
        self.__pq.append((element.get_tag(), element))

    def is_empty(self) -> bool:
        """
        This function is responsible to return True iff the queue is empty else returns false.
        @:return True iff the queue is empty else returns false.
        """
        if len(self.__pq) == 0:
            return True
        return False

    def remove(self, element: object):
        """
        This function is responsible to remove a given element from the priority queue.
        @:param element - the given element to remove.
        @:returns -1 iff the removal of the element failed.
        """
        try:
            return self.__pq.remove((element.get_tag(), element))

        except:
            return -1

    def get_key(self, item):
        """
        This function is responsible to return the element's key in the tuple.
        @:param item - the given element.
        @:return the element's key.
        """
        return item.get_tag()

    def __sizeof__(self):
        return len(self.__pq)
