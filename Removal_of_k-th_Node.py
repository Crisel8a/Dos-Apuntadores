"""Given the head of a singly linked list and an integer k, remove the k-th node from
the end in one traversal and return the new head. If k is invalid, return the original list."""


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep):
    while node:
        print(node.data, end="")

        node = node.next

        if node:
            print(sep, end="")


#
# Complete the 'removeKthNodeFromEnd' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER k
#


#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeKthNodeFromEnd(head, k):
    # head representa el primer nodo de la lista.
    #
    # Si head es None, significa que la lista está vacía.
    # Si k es negativo, la posición no es válida.
    # En ambos casos devolvemos la lista sin modificarla.
    if head is None or k < 0:
        return head

    # fast será el apuntador que avanzará primero.
    fast = head

    # slow terminará ubicado en el nodo que debemos eliminar.
    slow = head

    # previous guardará el nodo que se encuentra antes de slow.
    # Lo necesitamos para poder desconectar a slow de la lista.
    previous = None

    # Adelantamos fast exactamente k posiciones.
    #
    # Por ejemplo, con k = 3:
    #
    # Inicio: fast está en 5
    # Paso 1: fast está en 6
    # Paso 2: fast está en 7
    # Paso 3: fast está en 8
    for _ in range(k):
        fast = fast.next

        # Si fast llega a None durante este proceso,
        # significa que k es demasiado grande.
        #
        # Por ejemplo, en una lista de 4 nodos,
        # k = 4 es inválido porque las posiciones válidas
        # son 0, 1, 2 y 3.
        if fast is None:
            return head

    # Ahora movemos fast y slow una posición a la vez.
    #
    # Nos detenemos cuando fast esté en el último nodo.
    # En ese momento, slow estará en el nodo que se elimina.
    while fast.next is not None:
        # fast avanza una posición.
        fast = fast.next

        # Antes de mover slow, guardamos su posición actual.
        # Este será el nodo anterior a slow.
        previous = slow

        # slow también avanza una posición.
        slow = slow.next

    # Si previous continúa siendo None, significa que slow
    # nunca avanzó y todavía está en la cabeza.
    #
    # Por tanto, debemos eliminar la cabeza.
    if previous is None:
        # La nueva cabeza será el segundo nodo.
        return head.next

    # Para eliminar slow, hacemos que el nodo anterior
    # apunte directamente al nodo siguiente de slow.
    #
    # Antes:
    # previous → slow → slow.next
    #
    # Después:
    # previous ───────→ slow.next
    previous.next = slow.next

    # Devolvemos la cabeza de la lista modificada.
    return head


if __name__ == "__main__":
    head_count = int(input().strip())

    head = SinglyLinkedList()

    for _ in range(head_count):
        head_item = int(input().strip())
        head.insert_node(head_item)

    k = int(input().strip())

    result = removeKthNodeFromEnd(head.head, k)

    print_singly_linked_list(result, "\n")
    print()
