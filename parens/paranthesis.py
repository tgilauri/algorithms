def generate(cur, opened, closed, n, result: list):
    if len(cur) == 2 * n:
        result.append(cur)
        return
    if opened < n:
        generate(cur + "(", opened + 1, closed, n, result)
    if closed < opened:
        generate(cur + ")", opened, closed + 1, n, result)


def parens(n):
    _result = []
    generate("", 0, 0, n, _result)
    return _result


input_file = open('./input.txt', 'r')
amount = int(input_file.read().strip())
input_file.close()

result = parens(amount)

output_file = open('./output.txt', 'w')
output_file.write("\n".join(result))
output_file.close()
