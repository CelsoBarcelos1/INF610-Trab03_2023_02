# this code is to plot the graphs of Complexity of each paradgmas

from main import W_Activity_Selection
import random
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.style.use('classic')
    # GRÁFICOS PARA ANÁLISE DE COMPLEXIDADE:
    n = 51
    activities = [(1, 4, 3)]; # [(start time, end time), ...] of activities
    list_BT = np.zeros(n-1)
    list_DP = np.zeros(n-1)
    list_greedy = np.zeros(n-1)

    for i in range(1, n): # increase activities array
        start, end = round(random.uniform(0, 20)), round(random.uniform(0, 20)) 
        while start == end: # avoid start = end
            start, end = round(random.uniform(0, 20)), round(random.uniform(0, 20))
        if start > end:
            start, end = end, start
        
        activities.append((start, end, end - start))
        
        WAS =  W_Activity_Selection(activities)
        solution_DP, count_DP = WAS.Dyn_Programming()
        solution_greedy, count_G = WAS.Greedy()
        solution_back, count_B = WAS.Backtracking()

        list_BT[i - 1] = count_B
        list_DP[i - 1] = count_DP
        list_greedy[i - 1] = count_G

    plt.plot(np.arange(1, n), list_BT)
    plt.plot(np.arange(1, n), list_DP)
    plt.plot(np.arange(1, n), list_greedy)

    plt.legend(['Backtracking', 'Dynamic Programming', 'Greedy'], loc=0)
    plt.xlabel("Tamanho da Entrada (n)")
    # plt.xticks(np.arange(1,n))
    plt.grid()
    plt.ylabel("N° vezes Op. Básica é executada [C(n)]")
    plt.tight_layout()
    plt.savefig("3paradgimas.png", dpi=600)

    plt.figure()

    plt.plot(np.arange(1, n), list_DP)
    plt.plot(np.arange(1, n), list_greedy)

    plt.legend(['Dynamic Programming', 'Greedy'], loc=0)
    plt.xlabel("Tamanho da Entrada (n)")
    plt.grid()
    plt.ylabel("N° vezes Op. Básica é executada [C(n)]")
    plt.tight_layout()
    plt.savefig("zoom_image.png", dpi=600)
    plt.show()

if __name__ == "__main__":
    main()
