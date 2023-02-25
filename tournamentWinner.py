
def tournamentWinner(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for i, comp in enumerate(competitions):
        
        homeTeam, awayTeam = comp
        winningTeam = homeTeam if results[i] == 1 else awayTeam

        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            print(scores)
            currentBestTeam = winningTeam

    return currentBestTeam

def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points