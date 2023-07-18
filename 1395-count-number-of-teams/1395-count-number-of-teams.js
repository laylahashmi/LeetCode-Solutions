/**
 * @param {number[]} rating
 * @return {number}
 */
var numTeams = function(rating) {
    let result = 0
    for (i = 0; i < rating.length; i++) {
        for (j = i+1; j <rating.length; j++) {
            for (k = j+1; k<rating.length; k++) {
                if ( rating[i] < rating[j] && rating[j] < rating[k] ||
                   rating[i] > rating[j] && rating[j] >rating[k]) {
                    result +=1
                }
            }
        }
    } return result
    
};