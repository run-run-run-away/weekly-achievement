class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s = sum(skill)

        skill.sort()
        answer = 0
        target = skill[0] + skill[-1]
        
        for i in range(floor(len(skill) / 2)):
            s = skill[i] + skill[-1 - i]
            if s != target:
                return -1
            answer += skill[i] * skill[-1 - i]
        
        return answer