import re


class CreditCardNoCheck:
    def check_if_valid_card_no(self, val):
        card_no_format_re = r"^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$"
        consecutive_no_re = r"no{4,}|[-?no]{5,}"

        matches = re.search(card_no_format_re, val)
        if matches is None:
            return False
        else:
            regex_matched_value = matches.group(0)
            if val == regex_matched_value:
                for i in range(10):
                    reg = consecutive_no_re.replace("no", str(i))
                    if bool(re.search(reg, regex_matched_value)):
                        return False
        return True
