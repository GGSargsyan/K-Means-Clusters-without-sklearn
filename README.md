# K-Means-Clusters-without-sklearn
(View this README in raw format)
In python I wrote a k-means algorithm that would typically require using the sklearn library.

I completed this using Jupyter Notebook. To run the program use the two input-data.txt and output-data.txt files or 
feel free to use your own data so long as it's formatted the same way as my data.

This program takes in your source data and asks for a user defined number of clusters to create. The program will then
output each iteration of the points and the clusters they belonged to at that iteration. Finally, 
each data point will be printed with its cluster next to it line by line.

A normal output looks like this:
NAME: Grigor Sargsyan

Enter the number of clusters: 5

Iteration 1
0 [1.8]
1 [4.5, 6.5]
2 [1.1, 0.5]
3 [2.1, 3.2]
4 [9.8, 7.6, 11.32]

Iteration 2
0 [1.8, 2.1]
1 [4.5, 6.5]
2 [1.1, 0.5]
3 [3.2]
4 [9.8, 7.6, 11.32]

Iteration 3
0 [1.8, 2.1]
1 [4.5, 6.5]
2 [1.1, 0.5]
3 [3.2]
4 [9.8, 7.6, 11.32]

Point 1.8 in cluster 0
Point 4.5 in cluster 1
Point 1.1 in cluster 2
Point 2.1 in cluster 0
Point 9.8 in cluster 4
Point 7.6 in cluster 4
Point 11.32 in cluster 4
Point 3.2 in cluster 3
Point 0.5 in cluster 2
Point 6.5 in cluster 1
