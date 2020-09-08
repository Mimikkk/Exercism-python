import re

FILE_TEXT = {
    "iliad.txt": """Achilles sing, O Goddess! Peleus' son;
His wrath pernicious, who ten thousand woes
Caused to Achaia's host, sent many a soul
Illustrious into Ades premature,
And Heroes gave (so stood the will of Jove)
To dogs and to all ravening fowls a prey,
When fierce dispute had separated once
The noble Chief Achilles from the son
Of Atreus, Agamemnon, King of men.\n""",
    "midsummer-night.txt": """I do entreat your grace to pardon me.
I know not by what power I am made bold,
Nor how it may concern my modesty,
In such a presence here to plead my thoughts;
But I beseech your grace that I may know
The worst that may befall me in this case,
If I refuse to wed Demetrius.\n""",
    "paradise-lost.txt": """Of Mans First Disobedience, and the Fruit
Of that Forbidden Tree, whose mortal tast
Brought Death into the World, and all our woe,
With loss of Eden, till one greater Man
Restore us, and regain the blissful Seat,
Sing Heav'nly Muse, that on the secret top
Of Oreb, or of Sinai, didst inspire
That Shepherd, who first taught the chosen Seed\n""",
}
from typing import *


def grep(pattern, flags, files):
    should_number_line: bool = '-n' in flags
    should_only_name_files: bool = '-l' in flags
    should_name_files: bool = len(files) > 1
    is_insensitive: bool = '-i' in flags
    is_full_match: bool = '-x' in flags
    is_invert: bool = '-v' in flags

    pattern = pattern.lower() if is_insensitive else pattern
    result = ''
    for file_name in files:
        file = FILE_TEXT[file_name]
        for (i, line) in enumerate(file.strip('\n').split('\n'), 1):
            search_line = (line.lower() if is_insensitive else line)
            match = pattern == search_line if is_full_match else pattern in search_line
            match = not match if is_invert else match

            if match:
                if should_only_name_files:
                    if f"{file_name}\n" not in result:
                        result += f"{file_name}\n"
                else:
                    result += (
                        f'{f"{file_name}:" if should_name_files else ""}{f"{i}:" if should_number_line else ""}{line}\n'
                    )
    return result
