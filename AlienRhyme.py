class TrieNode(object):
    """
    Our trie node implementation. Very basic. but does the job
    """

    def __init__(self, char):
        self.char = char
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.counter = 1

    def __str__(self):
        return self.char + str(self.counter) + '_' + ','.join([str(child) for child in self.children])


def add(root, word):
    """
    Adding a word in the trie structure
    """
    node = root
    for char in word:
        found_in_child = False
        # Search for the character in the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found it, increase the counter by 1 to keep track that another
                # word has it as well
                child.counter += 1
                # And point the node to the child that contains this char
                node = child
                found_in_child = True
                break
        # We did not find it so add a new chlid
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # And then point node to the new child
            node = new_node
    # Everything finished. Mark it as the end of a word.
    node.word_finished = True


def find_prefix(root, prefix):
    """
    Check and return
      1. If the prefix exists in any of the words we added so far
      2. If yes then how may words actually have the prefix
    """
    node = root
    # If the root node has no children, then return False.
    # Because it means we are trying to search in an empty trie
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        # Search through all the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found the char existing in the child.
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                break
        # Return False anyway when we did not find a char.
        if char_not_found:
            return False, 0
    # Well, we are here means we have found the prefix. Return true to indicate that
    # And also the counter of the last node. This indicates how many words have this
    # prefix
    return True, node.counter


def remove_1_nodes(root):
    idx_to_remove = []
    for idx in range(len(root.children)):
        if root.children[idx].counter == 1:
            idx_to_remove.append(idx)
        else:
            root.children[idx] = remove_1_nodes(root.children[idx])

    for idx in reversed(idx_to_remove):
        root.children.pop(idx)

    return root


def find_number_of_pairs(root):
    if len(root.children) == 0:
        return 2

    n_of_pairs_in_children = sum([find_number_of_pairs(child) for child in root.children])
    if root.counter - n_of_pairs_in_children >= 2:
        return 2 + n_of_pairs_in_children
    else:
        return n_of_pairs_in_children


def construct_tree(words):
    root = TrieNode('*')
    for w in words:
        add(root, reversed(w))

    root = remove_1_nodes(root)
    return root


T = int(input())

for i in range(1, T + 1):
    N = int(input().strip())
    words = [input() for _ in range(N)]

    root = construct_tree(words)

    n_pairs = sum([find_number_of_pairs(child) for child in root.children])

    print('Case #{}: {}'.format(i, n_pairs))
