# RandomWalk-Visualiser
A random walk is known as a random process which describes a path including a succession on random steps, each with direction and distance. As expected, this has been adapted and used to be a mathematical model of the stock market and its evolution to a random walk. 

A thing to note here is that, this particular project does not have any financial implications and is not for testing out on the underlying funds of the stock market. This was a beginner project for me to learn about Random Walks. There would be upcoming projects that use this as a base to expand into the financial side of things, which is ultimately the end goal for me. 

**Implementation Details**

Using the __init__ function, I have ensured that the default number of points to be considered for this experiment would be ‘5,000’ (This can changed in the random_walk_visualisation.py according to your convenience). I have made sure that the starting points for both x and y would be (0,0). 

Coming to the actual steps, I have given it both direction (-1, 1) and distance. I have rejected moves that do not go anywhere, to ensure progress. Focusing on the visualisation, I have gone ahead with a scatter point to accurately show the variety of the steps. Additionally, I have also added a gradient, start point and end point to track the steps.  
