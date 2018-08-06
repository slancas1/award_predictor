The training algorithm we used is a genetic algorithm which trains on 2016 Oscars data, and consists of the following steps:
1.	Initial Population: An initial set of 1000 parameter sets for the fitness function will be randomly generated to make the “population” of parameters.
2.	Fitness Function: After assigning a score based on the algorithm above to each movie, the algorithm will sort by that movie score. The fitness function in this case gives the parameter set a higher fitness the closer the actual winner and nominees are to the front of the list with a slightly higher weight on the winner. The fitness also gets lowered if the predicted winner and/or nominees are not the true winner/nominees.
3.	Parent Selection:  Select two parents from the population using a weighted random selection based on the fitness score to generate children parameter sets.
4.	Child Generation: Each pair of parent parameter sets generates two children. We perform a uniform crossover with the parameters of the parents to generate the two children parameter sets.
5.	Mutation: At each generation of a new child, the child has a 20% chance to introduce a mutation which offsets the value of randomly chosen parameters by a random number between -3 and 3.
6.	Replacement: Repeat steps 3-5 until the number of children generated is 30% of the original population. Replace the 30% of parameter sets in the population with the lowest fitness scores with the children.
7.	Optimization: Repeat steps 2-6 until the population is fit enough (i.e. a convergence). We had the algorithm run for 700 generations to ensure convergence.
 
This algorithm allows us to optimize the weights we use for our predictor since a parameter set is “rewarded” for better matching the true results of the past Oscar award show.

