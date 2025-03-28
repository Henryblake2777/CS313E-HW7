"""
Student information for this assignment:

Replace Henry Blake with your name.
On my/our honor, Henry Blake, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: Hrb987
UT EID 2: Hrb987
"""


class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data instance variable, this node class has both
    a coefficient and an exponent instance variable, which is used to represent each
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended, which will we learn more
        # about in class on Monday 3/24. If you choose to use
        # a dummy node, comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        # self.dummy = Node(None, None)
        self.head = None

    # Insert the term with the coefficient coeff and exponent exp into the polynomial.
    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
        if coeff == 0:
            return
        node = Node(coeff, exp)
        if self.head is None:
            self.head = node
            return
        if node.exp > self.head.exp:
            node.next = self.head
            self.head = node
            return
        current = self.head
        previous = None
        while current:
            if current.exp == node.exp:
                current.coeff += node.coeff
                if current.coeff == 0:
                    if previous:
                        previous.next = current.next
                    else:
                        self.head = current.next
                        current.next = None
                return
            if current.exp < node.exp:
                node.next = current
                previous.next = node
            previous = current
            current = current.next
        previous.next = node


    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        if not p:
            return self
        current = p.head
        while current:
            self.insert_term(current.coeff, current.exp)
            current = current.next
        return self


    # Multiply a polynomial p with the polynomial and return the product as a new linked list.
    def mult(self, p):
        result = LinkedList()
        current = self.head
        while current:
            pcurrent = p.head
            while pcurrent:
                coeff = current.coeff * pcurrent.coeff
                exp = current.exp + pcurrent.exp
                result.insert_term(coeff, exp)
                pcurrent = pcurrent.next
            current = current.next
        return result


    # Return a string representation of the polynomial.
    def __str__(self):
        polynomial = ''
        current = self.head
        while current:
            polynomial += f'({current.coeff}, {current.exp}) + '
            current = current.next
        return polynomial[0:-3]



def main():
    # read data from stdin (terminal/file) using input() and create polynomial p

    # read data from stdin (terminal/file) using input() and create polynomial q

    # get sum of p and q as a new linked list and print sum

    # get product of p and q as a new linked list and print product
    poly1 = LinkedList()
    poly2 = LinkedList()
    len_poly1 = int(input())
    for i in range(len_poly1):
        line = input().split()
        poly1.insert_term(int(line[0]), int(line[1]))
    input()
    len_poly2 = int(input())
    for i in range(len_poly2):
        line = input().split()
        poly2.insert_term(int(line[0]), int(line[1]))
    print(poly1.add(poly2))
    print(poly1.mult(poly2))




if __name__ == "__main__":
    main()
