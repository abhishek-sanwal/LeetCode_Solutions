/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var rotateString = function(s, goal) {
    
    return s.length == goal.length && s.concat(s).includes(goal)
};