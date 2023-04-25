# CISC-851-Evolutionary-Computng


### Abstract
Hyperparameter tuning is a crucial step in building neural network models such as LSTM (Long Short-Term Memory), as it significantly affects their performance. A wide range of hyperparameters need to be optimized to achieve optimal model performance. However, optimizing hyperparameters in a high-dimensional space is a challenging task that requires extensive computational resources and expertise. In this project, we use Random Search, Bayesian Optimization, and Genetic Algorithm, three different methods to tune the hyperparameters of LSTM networks. Four hyperparameters are selected for tuning, namely the number of hidden units, learning rate, number of epochs, and input length. To evaluate the performance of these hyperparameter tuning methods, we use the IMDB movie review dataset, which consists of 50,000 reviews with an equal number of positive and negative labels. Our study aims to provide insights into the effectiveness and efficiency of methods for optimizing hyperparameters in LSTM networks. Our findings suggest that Genetic Algorithm produced the best results, with an accuracy of 0.88. By comparing the results obtained from these different search methods, we identified the most suitable approach for tuning the hyperparameters of LSTM networks, thereby enhancing their performance in various tasks. 

### Files
1. Code/Bayesian_and_Random_.ipynb : contains the results of the algorithm generated from the random search and the bayesian optimization methods.
2. Code/gentic.py: contains code  for  genetic algorithm.
3. Code/GA.ipynb: contains the implementation of genetic algorithm on our LSTM network.


### How to Run

1. It is recommended to use google colab instead of local environment.
2. Upload the ipynb file and run the scripts.
