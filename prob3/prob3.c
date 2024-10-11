//Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

//Example 1:

//Input: timePoints = ["23:59","00:00"]
//Output: 1
//Example 2:

//Input: timePoints = ["00:00","23:59","00:00"]
//Output: 0

int min(char* time){  //
    int hour;
    int min;

    sscanf(time ,"%d:%d" ,&hour , &min );
    return (hour*60 + min);
}

    
int findMinDifference(char** timePoints, int timePointsSize) {
    int mdiff = 1440;
    int value[timePointsSize];
    for(int i = 0 ; i<timePointsSize ; i++){
        value[i] = min(timePoints[i]);

    }
    for(int j =0 ; j<timePointsSize ; j++){
        for(int k = j+1 ; k<timePointsSize ; k++ ){
            int diff = abs(value[j] - value[k]);
            if(diff>720){
                diff = 1440 - diff;
                
            }
            if(diff<mdiff){
                mdiff = diff;
            }
            }
            
        }
        return mdiff;
        
    }
    