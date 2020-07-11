class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        is_one_up = False
        result = ""
        if len_a >= len_b:
            for i in range(-1, -(len_a + 1), -1):
                if -i > len_b:
                    other_num = "0"
                else:
                    other_num = b[i]
                if is_one_up:
                    if a[i] == other_num:
                        result += "1"
                        if a[i] == "1":
                            is_one_up = True
                        else:
                            is_one_up = False
                    else:
                        result += "0"
                        is_one_up = True

                else:
                    if a[i] == other_num:
                        if a[i] == "1":
                            is_one_up = True
                        else:
                            is_one_up = False
                        result += "0"
                    else:
                        result += "1"
                        is_one_up = False
        else:
            for i in range(-1, -(len_b + 1), -1):
                if -i > len_a:
                    other_num = "0"
                else:
                    other_num = a[i]
                if is_one_up:
                    if b[i] == other_num:
                        result += "1"
                        if b[i] == "1":
                            is_one_up = True
                        else:
                            is_one_up = False
                    else:
                        result += "0"
                        is_one_up = True

                else:
                    if b[i] == other_num:
                        if b[i] == "1":
                            is_one_up = True
                        else:
                            is_one_up = False
                        result += "0"
                    else:
                        result += "1"
                        is_one_up = False

        if is_one_up:
            result += "1"
        return result[::-1]
