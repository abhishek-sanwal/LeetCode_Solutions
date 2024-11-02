/**
 * @param {string} sentence
 * @return {boolean}
 */
var isCircularSentence = function(sentence) {
    
    return sentence.split(" ").reduce( function(check, word,index,arr){
        
        return check && (index !== arr.length-1 ? arr.at(index).at(-1) === arr.at(index+1).at(0) : arr.at(index).at(-1) === arr.at(0).at(0)) ;
        
    },true);
    
};