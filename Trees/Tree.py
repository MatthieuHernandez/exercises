class Node:
    Name = ""
    Nodes = []

    def __init__(self, nodes, verbose = 0):
        try:
            if len(nodes) == 0:
                return
            
            self.Name = nodes[0]
           
            if verbose:
                print("Creating", self.Name, "...")

            if (isinstance(nodes, list) and
                len(nodes) > 1 and
                isinstance(nodes[0], str) and
                isinstance(nodes[1], list)):
                nodes.pop(0)
                for node in nodes:
                    self.Nodes.append(Node(node, verbose))
                        
                if verbose:
                    print("Node", self.Name, "created.")
            else :
                if isinstance(nodes, list):
                    nodes.pop(0)
                    self.Nodes.append(Node(nodes, verbose))
                if verbose:
                    print("Leaf", self.Name, "created.")
                
                
        except:
            print("Cannont create node, invalid input.")

    def ComputeDeep(self):
        return 0
