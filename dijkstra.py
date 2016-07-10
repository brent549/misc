#!/usr/bin/python

import sys
from pprint import pprint

def matrix_to_graphDict(src, dst, network):
   """convert matrix to graph dict"""
   graph_dict={}
   for i in xrange(len(network)):
      for j in xrange(len(network[i])):
         if network[i][j] > 0:
            if not i in graph_dict:
               #graph_dict[i] = []
               graph_dict[i] = {}
            graph_dict[i][j] = network[i][j]
            #graph_dict[i].append((j,network[i][j]))

   print "Matrix of network graph"
   pprint(network)
   print "graph of each node its next hop and weight"
   pprint(graph_dict)

   paths = find_paths(src,dst,graph_dict)

   print "possible paths from %s to %s" %(src, dst)
   pprint(paths)

   shortest_path(graph_dict,paths)

   return graph_dict

def shortest_path(graph_dict,paths):
   """Take a dict_graph of each node's neighbors and the weight
      and a matrix of possible paths
   """
   weights={}
   for src,dst_dict in graph_dict.items():
      for dst,weight in dst_dict.items():
         weights[(src,dst)] = weight
         weights[(dst,src)] = weight # need this for unidirectional graph
   pprint (weights)

   path_dict={}
   for path in paths:
      total=0
      for i in xrange(1,len(path)):
         src = path[i-1]
         dst = path[i]
         w   = weights[(src,dst)]
         total +=w
      print "%s %s" % (total,path)
      path_dict[total] = path

   w = sorted(path_dict)[0]
   print "** %s %s" % (w,path_dict[w])

   return (w,path_dict)


def find_paths(start,end,graph,path=[]):
   """ take a graphDict and determine all possible paths """
   path = path + [start]
   if start == end:
      return [path]
   if start not in graph:
      return []
   paths = []
   for vertex in graph[start]:
      if vertex not in path:
         extended_paths = find_paths(vertex,end,graph,path)
         for p in extended_paths:
            paths.append(p)
   return paths

src=4
dst=5
network=[[0, 2, 4, 8, 0, 0],
         [0, 0, 0, 9, 0, 0],
         [0, 0, 0, 0, 0, 10],
         [0, 0, 6, 0, 0, 10],
         [10, 10, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]

print matrix_to_graphDict(src,dst,network)
