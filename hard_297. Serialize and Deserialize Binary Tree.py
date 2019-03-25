
class Codec:

    def serialize(self, root):
        output, queue = [], [root]
        while queue:
            element = queue.pop(0)
            if element:
                output.append(element)
                queue.extend(filter(lambda x: x, (element.left, element.right)))

        return str(output)

    def deserialize(self, data):
        if data:
            parsed_data, ptr = [i.strip() for i in data[1:-1].split(',')], 0
            hashmap = {0 : TreeNode(int(parsed_data[0]))}

            for idx, char in enumerate(parsed_data):
                if char != 'None':
                    node = hashmap[idx]
                    ptr += 1
                    if parsed_data[ptr] is not 'None':
                        node.left = TreeNode(int(parsed_data[ptr]))
                        hashmap[ptr] = node.left
                    ptr += 1
                    if parsed_data[ptr] is not 'None':
                        node.right = TreeNode(int(parsed_data[ptr]))
                        hashmap[ptr] = node.right
                root = root or node

            return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
