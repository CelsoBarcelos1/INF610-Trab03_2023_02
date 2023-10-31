# - Task > Determine the maximum hours of activities from the length of input lists

class W_Activity_Selection():
    def __init__(self, arr):
        self.arr = arr
    

    def Backtracking(self):
        """ Backtracking Approach """
        Total_hours = 0

        global solution, s, count_BT
        count_BT = 0
        arr = sorted(self.arr, key = lambda x: x[1])
        solution = list() 
        s = 0
        self.helperBackTracking(arr, [], 0, len(self.arr), 0, 0)
        
        for activity in solution:
            Total_hours += activity[2]
        
        return Total_hours, count_BT

    def helperBackTracking(self, arr, List, count, List_Size, last_idx, Sum_values):
        global solution, s, count_BT

        count_BT += 1
        if count == List_Size:
            if s < Sum_values: 
                solution = List
                s = Sum_values
        else:            
            if Sum_values!= 0:  # para saber se existe alguma atividade na lista
                if arr[count][0] >= arr[last_idx][1]:
                    self.helperBackTracking(arr, List + [arr[count]], count + 1, List_Size, count, Sum_values+ arr[count][1] - arr[count][0])  
            else:
                self.helperBackTracking(arr, List + [arr[count]], count + 1, List_Size,  count,  Sum_values + arr[count][1] - arr[count][0])   #1         
            self.helperBackTracking(arr, List, count + 1, List_Size, last_idx, Sum_values)


    def Dyn_Programming(self):
        """ Dynamyc Programming Approach """  
        count = 0 # number that Basic Operations was realized  
        N = len(self.arr) #  number of activities
        activities = sorted(self.arr, key=lambda x: x[1]) # Sort the activities by finish times

        OPT = [0] * (N + 1) # table Dynamic Programming with zeros
        q = [0] * N

        # Compute q values for each activity
        for j in range(1, N):
            i = j - 1
            count +=1
            while i >= 0 and activities[i][1] > activities[j][0]:
                i -= 1
            q[j] = i
        # print('q',q)

        # =====>  DYNAMIC PROGRAMMING TABLE:
        for j in range(1, N + 1):
            count +=1
            OPT[j] = max(activities[j - 1][2] + OPT[q[j - 1] + 1], OPT[j - 1])
        
        return OPT, count
    
    
    def Greedy(self):
        """ Gredy Approach """ 
        count = 0    
        Total_hours = 0   
        activities = sorted(self.arr, key=lambda x: x[2], reverse = True) # Sort activities in descending order of duration (weight) in descending order)
        selected_activities = [activities[0]]  # Initialize with the most time-consuming and heaviest activity

        for activity in activities[1:]:
            # Check if the current activity conflicts with the selected ones
            conflict = False
            for selected_activity in selected_activities:
                count += 1
                if activity[0] < selected_activity[1] and activity[1] > selected_activity[0]:
                    conflict = True
                    break
            # If no conflict, add the activity to the selected list
            if not conflict:
                selected_activities.append(activity)
                
        for activity in selected_activities:
            Total_hours += activity[2]

        return Total_hours, count
    

if __name__ == '__main__':    
    activities = [(1, 4), (5, 8), (7, 15), (8, 10)]
    list_activities = [(start, end, end - start) for start, end in activities]

    WAS = W_Activity_Selection(list_activities)
    solution_DP, count_DP = WAS.Dyn_Programming()
    solution_greedy, count_G = WAS.Greedy()
    solution_back, count_B = WAS.Backtracking()
    

    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('  ---- > BACKTRACKING APROACH: <---- ')
    print(f'Maximum hours worked => {solution_back} hours.')
    print(f'Number of times the Basic operation was performed => {count_B} times')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('  ---- > DYNAMIC PROGRAMMING APROACH: <---- ')
    print(f'Maximum hours worked => {solution_DP[-1]} hours.')
    print(f'Table of Dynamic Programming => {solution_DP}')
    print(f'Number of times the Basic operation was performed => {count_DP} times')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
    
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('  ---- > GREEDY APROACH: <---- ')
    print(f'Maximum hours worked => {solution_greedy} hours.')
    print(f'Number of times the Basic operation was performed => {count_G} times')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')
