from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.views.generic import View
from .models import faculty_info
from subject.models import subjects
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

import operator
# Create your views here

from .forms import Infoform


def facultyinfo(request):
    form = Infoform(request.POST or None)

    if form.is_valid():
        form.save()
    return render(request, "faculty/faculty.html")


class Faculty_priority(View):
    template = 'faculty/Facultysubjectselection-4.html'
    x = subjects.objects.all()
    print(x)
    data = serializers.serialize('json', x)

    def get(self, request):
        # print(self.data)
        return render(request, self.template, {'data': self.data})


from collections import defaultdict


# This class represents a directed graph using adjacency matrix representation
class Graph:

    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)
        # self.COL = len(gr[0])

    '''Returns true if there is a path from source 's' to sink 't' in 
    residual graph. Also fills parent[] to store the path '''

    def BFS(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

                    # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False

    # Returns tne maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * (self.ROW)

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

                # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while (v != source):
                u = parent[v]
                print(v, end=' ')
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
            print('\n')

        return max_flow

    # Create a graph given in the above diagram


def subject_assign(request):
    teachers = faculty_info.objects.order_by('-designation')
    subject = subjects.objects.all()

    list = []
    x = []
    for i in range(len(teachers) + len(subject) + 2):
        x.append(0)

    for i in range(len(teachers) + len(subject) + 2):
        list.append(x[:])

    for i in range(len(teachers)):
        if teachers[i].designation == 'professor':
            list[0][i + 1] = 2
        elif teachers[i].designation == 'associate professor':
            list[0][i + 1] = 3
        else:
            list[0][i + 1] = 4

    # assume there is a class priority :

    # for x in teachers:
    #

    for s in subject:
        subject_id = s.pk
        print(s.name)
        print(s.pk)
        for x in s.faculty.all():
            faculty_id = x.pk
            print(x.pk)
            print(len(subject) + faculty_id)
            list[subject_id][len(subject) + faculty_id - 6] = 1

    for x in teachers:
        if x.designation == 'professor':
            list[len(subject) + x.pk - 6][len(teachers) + len(subject) + 1] = 2
        elif x.designation == 'associate professor':
            list[len(subject) + x.pk - 6][len(teachers) + len(subject) + 1] = 3
        else:
            list[len(subject) + x.pk - 6][len(teachers) + len(subject) + 1] = 4

    print(list)
    teachers = faculty_info.objects.order_by('-designation')
    print(teachers)
    print(subject)

    g = Graph(list)

    source = 0;
    sink = len(teachers) + len(subject) + 1
    g.FordFulkerson(source, sink)

    return HttpResponse('working')





