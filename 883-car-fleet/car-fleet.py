class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed))

        result = []
        for pos, spd in cars:
            time = float(target - pos) / spd
            result.append(time)

        fleet = 0
        last_time = 0

        for i in range(len(result) - 1, -1, -1):
            if result[i] > last_time:
                fleet += 1
                last_time = result[i]

        return fleet