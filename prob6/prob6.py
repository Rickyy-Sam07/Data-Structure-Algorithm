'''
There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.

Return the chair number that the friend numbered targetFriend will sit on.

 

Example 1:

Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
Output: 1
Explanation: 
- Friend 0 arrives at time 1 and sits on chair 0.
- Friend 1 arrives at time 2 and sits on chair 1.
- Friend 1 leaves at time 3 and chair 1 becomes empty.
- Friend 0 leaves at time 4 and chair 0 becomes empty.
- Friend 2 arrives at time 4 and sits on chair 0.
Since friend 1 sat on chair 1, we return 1.
Example 2:

Input: times = [[3,10],[1,5],[2,6]], targetFriend = 0
Output: 2
Explanation: 
- Friend 1 arrives at time 1 and sits on chair 0.
- Friend 2 arrives at time 2 and sits on chair 1.
- Friend 0 arrives at time 3 and sits on chair 2.
- Friend 1 leaves at time 5 and chair 0 becomes empty.
- Friend 2 leaves at time 6 and chair 1 becomes empty.
- Friend 0 leaves at time 10 and chair 2 becomes empty.
Since friend 0 sat on chair 2, we return 2.
'''




class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Store the arrival and leaving time of the targetFriend.
        # We'll use this later to check when the targetFriend arrives and leaves.
        target_time = times[targetFriend]

        # Sort the 'times' list by arrival time (the first element in each sublist).
        # Sorting ensures we process friends in the order they arrive at the party.
        times.sort(key=lambda x: x[0])

        # Get the total number of friends.
        n = len(times)

        # Initialize a list to track the time each chair becomes free.
        # Each index in 'chair_time' corresponds to a chair.
        # Initially, all chairs are available (set to 0).
        chair_time = [0] * n

        # Iterate through each friend in the sorted 'times' list.
        # 'time' represents the arrival and leaving times for each friend.
        for time in times:
            # Check each chair to find the first available chair for the current friend.
            # We loop through all available chairs (0 to n-1).
            for i in range(n):
                # If the chair 'i' is available when the friend arrives (i.e., chair_time[i] <= arrival time):
                if chair_time[i] <= time[0]:
                    # Assign this chair to the friend and update the time when the chair will become free.
                    # The chair becomes free when the friend leaves, so set chair_time[i] to the leaving time.
                    chair_time[i] = time[1]

                    # If this current friend is the targetFriend (i.e., the friend whose arrival and leaving
                    # time matches 'target_time'), then return the index of the chair they're sitting on.
                    if time == target_time:
                        return i  # 'i' is the chair number

                    # Once a chair is assigned to the current friend, we break out of the inner loop
                    # since there's no need to check other chairs.
                    break

        # In case no chair is found (which shouldn't happen based on the problem constraints), return 0.
        return 0
