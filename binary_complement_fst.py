

def binary_complement_fst(word):
    current_state = 0
    output = []

    print("\nFST Transitions:")
    for ch in word:
        next_state = current_state + 1
        if ch == '0':
            output_symbol = '1'
        elif ch == '1':
            output_symbol = '0'
        else:
            output_symbol = ch  # keep non-binary characters unchanged
        print(f"{current_state} --{ch}/{output_symbol}--> {next_state}")
        output.append(output_symbol)
        current_state = next_state

    print(f"{current_state} [final]")
    print("\nOutput string:", "".join(output))

if __name__ == "__main__":
    word = input("Enter a binary string: ")
    binary_complement_fst(word)
