# logic is in parent directory
import logic

# enable importing from parent directory
import sys
sys.path.append('../logic')


def solve(file_name):
    lines = logic.read.read_input(file_name)

    current = 0
    for line in lines:
        current += 0
    return current
