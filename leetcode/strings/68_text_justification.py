from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur_line = []
        num_letters = 0

        for word in words:
            if num_letters + len(word) + len(cur_line) <= maxWidth:
                cur_line.append(word)
                num_letters += len(word)
            else:
                total_spaces = maxWidth - num_letters
                if len(cur_line) == 1:
                    res.append(cur_line[0] + " " * total_spaces)
                else:
                    num_gaps = len(cur_line) - 1
                    space_per_gap = total_spaces // num_gaps
                    extra_spaces = total_spaces % num_gaps
                    line_parts = []
                    for i in range(num_gaps):
                        line_parts.append(cur_line[i])
                        line_parts.append(" " * (space_per_gap + (1 if i < extra_spaces else 0)))
                    line_parts.append(cur_line[-1])
                    res.append("".join(line_parts))
                cur_line = [word]
                num_letters = len(word)

        last_line = " ".join(cur_line)
        res.append(last_line + " " * (maxWidth - len(last_line)))
        return res
