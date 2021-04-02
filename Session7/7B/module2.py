# -*- coding: utf-8 -*-

from functools import lru_cache
import math
import module1
'''
    This is a polygon class which has been designed to perform the following functions
    It initializes a Polygon object by taking input as edge and circumradius
    then it creates a sequence for all the Area versus Permmeter for all the Convex Polygons
    It also returns the Polygon with maximum area to perimeter ratio
'''
class RegularPolygonCustomSequence:


    def __init__(self, edge,circumradius):
        '''
        where initializer takes in:
        number of vertices for largest polygon in the sequence
        common circumradius for all regular strict polygons
        '''
        self.edge, self.circumradius = edge,circumradius

    def __len__(self):
        '''
        Length for an arithmetic range which is created
        '''
        return self.edge

    def __getitem__(self,n):
        '''
        This method helps to create the virtual sequence
        '''
        if isinstance(n, int):
            if n < 0 or n > self.edge:
                raise IndexError
            else:
                if n < 2 :
                    return 0
                else:
                    return RegularPolygonCustomSequence._efficiency(n,self.circumradius)
    def __repr__(self):
        '''
        Represents the method properly
        '''
        return '{}({}, {})'.format(
            type(self).__name__, self.edge, self.circumradius)

    @staticmethod #Static methods are methods that are bound to a class rather than its object.
    @lru_cache() #powers of 2
    def _efficiency(edge,circum_radius):
        '''
        Calculates the Area to Perimeter ratio for the Polygons
        '''
        n_vertices = edge
        #print(n_vertices)
        edgeLength= 2 * circum_radius * math.sin((math.pi/n_vertices))
        apothem =  circum_radius * math.cos((math.pi/n_vertices))
        area= 0.5 * n_vertices * edgeLength * apothem
        perimeter = n_vertices * edgeLength
        return round(area/perimeter,5)
     
    def _max_eff(self,seq_list):
        '''
        Returns the Polygon with maximum Area to Perimeter ratio
        '''
        return f' The Maximum ratio is for the Polygon {seq_list.index(max(seq_list)) } and the ratio is {max(seq_list)}'


