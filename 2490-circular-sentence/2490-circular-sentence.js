/**
 * @param {string} sentence
 * @return {boolean}
 */
var isCircularSentence = function(sentence) {
    
    return sentence.split(" ").reduce( function(check, word,index,arr){
        
        return check && (index !== arr.length-1 ? arr[index].at(-1) === arr[index+1][0] : arr[index].at(-1) === arr[0][0]) ;
        
    },true);
    
};