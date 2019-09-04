#!/bin/python3

import os
import sys
from collections import defaultdict

if __name__ == '__main__':
    road_nodes, num_road_edges = map(int, input().split())

    # road_from = [0] * road_edges
    # road_to = [0] * road_edges
    # road_weight = [0] * road_edges
    
    road_edges = [[sys.maxsize for i in range(road_nodes)] for j in range(road_nodes)]
    for l in range(road_nodes):
        road_edges[l][l] = 0
    for road_itr in range(num_road_edges):
        road_from, road_to, road_weight = map(int, input().split())
        road_from = road_from -1
        road_to = road_to - 1
        road_edges[road_from][road_to] = road_weight
        # if road_edges[road_from][road_to] == sys.maxsize:
        #     road_edges[road_from][road_to] = road_weight
        # else:
        #     road_edges[road_from][road_to] = min(road_edges[road_from][road_to], weight)
        
    for itr in range(road_nodes):
        for x in range(road_nodes):
            for y in range(road_nodes):
                if road_edges[x][itr] + road_edges[itr][y] <= road_edges[x][y] and (road_edges[x][itr] != sys.maxsize or road_edges[itr][y] != sys.maxsize):
                    road_edges[x][y] = road_edges[x][itr] + road_edges[itr][y]
    
    q = int(input())

    for q_itr in range(q):
        xy = input().split()

        x = int(xy[0]) - 1

        y = int(xy[1]) - 1
        
        
                
                
        if road_edges[x][y] == sys.maxsize:
            print('-1')
        else:
            print(road_edges[x][y])
