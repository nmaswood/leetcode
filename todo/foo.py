            if node1.left or node2.left:
                q.append(['left', node1.left, node2.left, new_node])

            if node1.right or node2.right:
                q.append(['right', node1.right,node2.right, new_node])


11
22
3
