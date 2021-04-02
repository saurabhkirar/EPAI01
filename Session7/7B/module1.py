import math

class RegularPolygon:  
    def __init__(self ,edge , circumradius):
        self.edge = edge
        self.circumradius = circumradius

    @property
    def edge(self):
        return self._edge

    @edge.setter
    def edge(self, edge):
        if edge <3:
            raise ValueError("Edge in a regular polygon  must be positive and be minimum 3 to form a closed figure")
        else:
            #print("I was called")
            self._edge = edge
    
    @property
    def circumradius(self):
        return self._circumradius

    @circumradius.setter
    def circumradius(self, circumradius):
        if circumradius <=0:
            raise ValueError("Circum radius must be positive")
        else:
            self._circumradius = circumradius
    @property     
    def interior_angle(self): #method
        return (self.edge - 2) * (180/self.edge)
    
    
    
    @property
    def edge_length(self):
        return 2 * self.circumradius * math.sin((math.pi/self.edge))

    @property
    def apothem(self):
            return self.circumradius * math.cos(math.pi/self.edge)
    
    @property
    def area(self):
        return (1/2) * self.edge * self.edge_length * self.apothem

    @property
    def perimeter(self):
        return (1/2) * self.edge * self.edge_length


    def __str__(self):
        return 'Polygon: edge={0}, circumradius={1}'.format(self.edge, self.circumradius)
    
    def __repr__(self):
        return 'Regular Polygon({0}, {1})'.format(self.edge, self.circumradius)

    def __eq__(self, other):
        if isinstance(other, RegularPolygon):
            return self.edge == other.edge and self.circumradius == other.circumradius
        
    def __gt__(self, other):
        if isinstance(other, RegularPolygon):
            if self.edge > other.edge:
                return "first object is greater than second object"
            else:
                return "first object is lesser than second object"
        else:
            raise NotImplementedError('cant be compared with other object types')