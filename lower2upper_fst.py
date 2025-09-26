# lower2upper_fst.py
# Simulates an FST that converts lowercase letters to uppercase

def lower2upper_fst(word):
    current_state = 0
    output = []

    print("\nFST Transitions:")
    for ch in word:
        next_state = current_state + 1
        if ch.islower():
            output_symbol = ch.upper()
        else:
            output_symbol = ch
        print(f"{current_state} --{ch}/{output_symbol}--> {next_state}")
        output.append(output_symbol)
        current_state = next_state

    print(f"{current_state} [final]")
    print("\nOutput string:", "".join(output))

if __name__ == "__main__":
    word = input("Enter a string: ")
    lower2upper_fst(word)

