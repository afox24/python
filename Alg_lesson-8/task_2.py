# Закодируйте любую строку из трех слов по алгоритму Хаффмана.

#str = "beep boop beer!"
string = "expelliarmus wingardium leviosa"
print("Исходная строка: " + string)

class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def root(self):
        return self.left, self.right

def get_haffman(node, code=""):
    if isinstance(node, str):
        return {node: code}

    a, b = node.root()

    result = {}
    result.update(get_haffman(a, code + "0"))
    result.update(get_haffman(b, code + "1"))

    return result

freq = {}
for num in string:
    if num not in freq:
        freq[num] = 0

    freq[num] += 1

tree = freq.items()

while len(tree) > 1:
    tree = sorted(tree, reverse=True, key=lambda x: x[1])
    num_1, count_1 = tree[-1]
    num_2, count_2 = tree[-2]
    tree = tree[:-2]
    tree.append((Node(num_1, num_2), count_1 + count_2))

encode_table = get_haffman(tree[0][0])

encode = []
for n in string:
    encode.append(encode_table[n])

print(f"Закодированная строка: {''.join(encode)}")
