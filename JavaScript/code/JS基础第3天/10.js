function getScoreLevel(score) {
    if (score < 60) 
        return 'E';
    if (score < 70)
        return 'D';
    if (score < 80)
        return 'C';
    if (score < 90)
        return 'B';
    return 'A';
}

console.log(getScoreLevel(78));