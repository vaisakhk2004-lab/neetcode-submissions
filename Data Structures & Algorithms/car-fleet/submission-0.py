class Solution:
    def carFleet(self, target, position, speed):
        fleets=[]
        for p,s in sorted(zip(position,speed),reverse=True):
            time=(target-p)/s
            if not fleets or  time>fleets[-1]:
                fleets.append(time)
        return len(fleets)
        
        