class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_length(self):
        temp = self
        count = 0

        while temp:
            count += 1
            temp = temp.next

        return count

    def convert_in_array(self):
        a = []
        temp = self

        while temp:
            a.append(temp.value)
            temp = temp.next

        return a

    def print_list(self):
        current = self
        while current:
            print(current.value)
            current = current.next


def removeConsecutiveSumTo0(node):
    nums = node.convert_in_array()
    print("array ", nums)
    for k in range(2, len(nums) + 1):
        #print("Analisando {} posicoes do array".format(k))

        l_num = len(nums)
        i = 0
        while i < l_num:
            #print("   posicao inicial {} valor {}".format(i, nums[i]))

            j = i+1
            while j < l_num:
                #print("      posição j {} com soma {}".format(nums[j:j+k-1], sum(nums[j:j+k-1])))
                if nums[i] + sum(nums[j:j+k-1]) == 0:
                    #print("         *** encontrado nas posições {} e {} com {}".format(i, j, i+len(nums[j:j+k-1])))

                    z = i + len(nums[j:j+k-1])
                    while z >= i:
                        nums.pop(z)
                        z -= 1
                        l_num -= 1
                    #print("         *** array resultante {}".format(nums))
                j += 1
            i += 1

    for i in nums:
        r_node = Node(i)

    return r_node


if __name__ == '__main__':
    node = Node(10)
    node.next = Node(5)
    node.next.next = Node(-3)
    node.next.next.next = Node(-3)
    node.next.next.next.next = Node(1)
    node.next.next.next.next.next = Node(4)
    node.next.next.next.next.next.next = Node(-4)
    node = removeConsecutiveSumTo0(node)
    while node:
        print(node.value),
        node = node.next
    # 10
