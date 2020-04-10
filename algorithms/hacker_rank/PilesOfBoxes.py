from collections import OrderedDict


class PilesOfBoxes:
    def get_no_of_steps_to_move_boxes(self, boxesInPiles):
        od = OrderedDict()
        boxesInPiles.sort(reverse=True)
        for i in boxesInPiles:
            if i in od:
                count = od[i]
                od[i] = count + 1
            else:
                od[i] = 1

        dict_values = list(od.values())

        steps = [dict_values[0]]
        for k in range(1, len(dict_values) - 1):
            dict_values[k] = (dict_values[k - 1] + dict_values[k])
            steps.append(dict_values[k])

        return sum(steps)
