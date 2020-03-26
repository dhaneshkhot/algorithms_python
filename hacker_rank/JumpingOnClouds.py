class JumpingOnClouds:

    def count_jumps(self, arr):
        jumps = 0
        arr_len = len(arr)
        i = 0
        while(True):
            if i+2 < arr_len:
                if arr[i + 2] == 0:
                    i = i + 2
                    jumps += 1
                else:
                    i += 1
                    jumps += 1
            else:
                i += 1
                jumps += 1
            if i+1 >= arr_len:
                break
        return jumps