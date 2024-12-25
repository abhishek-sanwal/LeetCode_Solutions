/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function largestValues(root: TreeNode | null): number[] {
    
    if(!root) return [];
    
    const maxList = [];
    
    const que = [root];
    
    while(que.length > 0){
        maxList.push(Number.MIN_SAFE_INTEGER);
        
        const length = que.length;
        
        for(let index = 0; index < length;++index){
            
            const node = que.shift();
            
            maxList[maxList.length-1] = Math.max(maxList.at(-1), node.val);
            node.left && que.push(node.left);
            node.right && que.push(node.right);
        }
        
    }
    
    return maxList;
    
    
    
    
};