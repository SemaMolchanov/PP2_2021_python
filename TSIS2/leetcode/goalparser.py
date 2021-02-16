class Solution:
    def interpret(self, command: str) -> str:
        o = command.replace('()', 'o')
        al = o.replace('(al)', 'al')
        return al
