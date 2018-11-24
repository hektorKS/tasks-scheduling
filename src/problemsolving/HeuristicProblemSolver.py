from problem.Problem import Problem


# sBest ← s0
# bestCandidate ← s0
# tabuList ← []
# tabuList.push(s0)
# while (not stoppingCondition())
# 	sNeighborhood ← getNeighbors(bestCandidate)
# 	for (sCandidate in sNeighborhood)
# 		if ( (not tabuList.contains(sCandidate)) and (fitness(sCandidate) > fitness(bestCandidate)) )
# 			bestCandidate ← sCandidate
# 		end
# 	end
# 	if (fitness(bestCandidate) > fitness(sBest))
# 		sBest ← bestCandidate
# 	end
# 	tabuList.push(bestCandidate)
# 	if (tabuList.size > maxTabuSize)
# 		tabuList.removeFirst()
# 	end
# end
# return sBest

class HeuristicProblemSolver:

    @staticmethod
    def solve(problem: Problem):
        pass