dic = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

parentheses = input("input: ").strip()

for i in range(len(parentheses)):
    if parentheses[i] in dic:
        stack = [parentheses[i]]
        for j in range(i + 1, len(parentheses)):
            if parentheses[j] in dic:
                stack.append(parentheses[j])
            elif stack and parentheses[j] == dic[stack[-1]]:
                stack.pop()
            else:
                break
        if not stack:
            print(f"valid parentheses")
            break
else:
    print("invalid parentheses")
