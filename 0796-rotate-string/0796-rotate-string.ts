function rotateString(s: string, goal: string): boolean {
    return s.length == goal.length && s.concat(s).includes(goal)
};