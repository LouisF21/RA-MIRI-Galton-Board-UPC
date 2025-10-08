#Galton Board
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
results = [] 
for n in [5, 10, 20, 50]:
    for N in [500, 2000, 10000, 50000]:
        # Parameters
        NumberLevels = n
        NumberBalls = N
        
        # Simulate Galton Board
        board = np.zeros(NumberLevels + 1)
        for _ in range(NumberBalls):
            right_steps = 0
            for _ in range(NumberLevels):
                if random.random() < 0.5:  
                    right_steps += 1
            board[right_steps] += 1 
                                
        prop_dis = board / NumberBalls
        
        # Normal distribution parameters
        mu = NumberLevels / 2
        sigma = np.sqrt(NumberLevels / 4)
        x = np.linspace(0, NumberLevels, 200)
        normal_pdf = norm.pdf(x, mu, sigma)

        #MSE
        normal_pdf_atk = norm.pdf(range(NumberLevels + 1), mu, sigma)
        mse = np.mean((prop_dis - normal_pdf_atk) ** 2)
        print("MSE:", mse)
        results.append((NumberLevels, NumberBalls, mse))
        
        # Plotting
        plt.bar(range(NumberLevels + 1), prop_dis, color='skyblue', label='Simulation')
        plt.plot(x, normal_pdf, color='black', label='Normal Dist')
        plt.xlabel("Number of levels k")
        plt.ylabel("Prob P(X=k)")
        plt.title(f"Galton-Board: k={NumberLevels}, N={NumberBalls}")
        plt.legend()
        plt.show()

print(results)