class CountingValleys:

    def count_valleys(self, arr):
        valley_counter = 0
        sea_level=0
        down = False
        for char in arr:
            if char == 'D':
                sea_level -= 1
            if char == 'U':
                sea_level += 1
            if char == 'D' and sea_level < 0:
                down = True
            if down and sea_level == 0:
                valley_counter += 1
                down = False
        return valley_counter