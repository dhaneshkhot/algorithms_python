class TimeConversion:

    def time_conversion(self, s):
        am_pm = s[8:10]
        time = s[0:8]

        hr = int(time.split(":")[0])

        if am_pm == "PM" and (1 <= hr < 12):
            hr = hr + 12
            converted_time = str(hr) + time[2:]
        elif am_pm == "AM" and hr == 12:
            converted_time = "00" + time[2:]
        else:
            converted_time = time

        return converted_time
