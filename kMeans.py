#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1
print("NAME: Grigor Sargsyan")
print()

#2
inputFile = open("input-data.txt", "r")
outputFile = open("output-data.txt", "w+")
k = int(input("Enter the number of clusters: "))
print()

#3
data = [float(x.rstrip()) for x in inputFile]

#4
centroids = dict(zip(range(k), data[0:k]))

clusters = dict(zip(range(k), [[] for i in range(k)]))

point_assignments = dict(zip(range(k), [[] for i in range(k)]))

old_point_assignments = dict()

real_point_assignments = dict(zip(data, [0 for i in range(len(data))]))

#5 Algorithm
def assign_to_clusters(data, clusters, centroids, point_assignments):  
    #Go through each point and it's index and find closest centroid
    for i in data:
        closest_index = 0
        dist_to_centroid = 100
        for j in centroids:
            if abs(i - centroids[j]) < dist_to_centroid:
                closest_index = j
                dist_to_centroid = abs(i - centroids[j])
        #by the end of this forloop we should know which centroid was it's best match
        #now assign the data val to it's chosen cluster 
        clusters[closest_index].append(i)
        #update point_assignments
        real_point_assignments[i] = closest_index

def assign_to_centroids(data, clusters, centroids):
    for x in clusters:
        clust_sum = sum(clusters[x])
        avg = float(clust_sum / len(clusters[x]))
        centroids[x] = min(clusters[x], key=lambda y:abs(y-avg))

counter = 0
while point_assignments != old_point_assignments:
    #a
    old_point_assignments = point_assignments
    
    #b Place each point in the closest cluster
    assign_to_clusters(data, clusters, centroids, point_assignments)
    
    #c Update the locations of centroids of the k cluster
    assign_to_centroids(data, clusters, centroids)
    
    #d
    point_assignments = clusters
    #reset clusters for next iteration
    clusters = dict(zip(range(k), [[] for i in range(k)]))
    #print out current k-means cluster configurations
    counter += 1
    print("Iteration %d" % counter)
    for x in point_assignments:
        print("%d [%s]" % (x, str(point_assignments[x]).strip("[]")))
    print()

#6
newline_counter = 0
for x in real_point_assignments:
    print("Point %s in cluster %d" % (str(x).rstrip("0"), real_point_assignments[x]))
    #prevents empty line from being printed at the end of output file
    newline_counter += 1
    if newline_counter < len(data):
        outputFile.write("Point %s in cluster %d\n" % (str(x).rstrip("0"), real_point_assignments[x]))
    else:
        outputFile.write("Point %s in cluster %d" % (str(x).rstrip("0"), real_point_assignments[x]))     

inputFile.close()
outputFile.close()


# In[ ]:




