#Riwk Sen

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        return (self.top == None)

    def __len__(self): 
        if self.isEmpty() == True:
            return 0
        else:
            count = 1
            entry = self.top
            while entry.next != None:
                count += 1
                entry = entry.next
            return count

    def push(self,value):
        nn = Node(value)
        if self.isEmpty() == True:
            self.top = nn
        else:
            nn.next = self.top
            self.top = nn
        return None

     
    def pop(self):
        if self.isEmpty() == True:
            return None
        else:
            top_stack = self.top
            self.top = self.top.next
            return top_stack
    
    def peek(self):
        return self.top


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        try:
            txt = float(txt)
            if isinstance(txt, float):
                return True
        except:
            return False







    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * ( ( 5 + -3 ) ^ 2 + ( 1 + 4 ) )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( ( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * ( -5 + 3 ) ^ 2 + ( 1 + 4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
        '''

    def is_number(string):
        try:
            float(string)
            return True
        except ValueError:
            return False

        # YOUR CODE STARTS HERE
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        accept_operands = '+-*/^'
        list_of_char = txt.split()
        print(list_of_char)
# SOMETHING IS WRONG WITH MY PARENTHESIS
        for k in range(len(list_of_char)):
            if .is_number(list_of_char[k]) == True:
                list_of_char[k] = float(list_of_char[k])
            else:
                continue



    
        postfix_str = ''

        for i in range(len(list_of_char)):

            print(f"i: {list_of_char[i]}")
            print(postfixStack)
            print(postfix_str)
            
            
            if list_of_char[i] == '(':
                print("open parenthesis")
                nn = Node(list_of_char[i])
                if postfixStack.isEmpty() == True:
                    postfixStack.top = nn
                else:
                    nn.next = postfixStack.top
                    postfixStack.top = nn
            elif list_of_char[i] == ')':
                print("close parenthesis")
                
                while postfixStack.top != None:
                    if postfixStack.top not in ['(']:
                        postfix_str = postfix_str + str(postfixStack.pop().value) + ' '
                    else:
                        break
                postfixStack.pop()
                print(postfixStack)
                    
            elif isinstance(list_of_char[i],float):
                print("number case")
                nn= Node(list_of_char[i])
                if i == (len(list_of_char) - 1):
                    postfix_str = postfix_str + str(list_of_char[i]) + ' '
                elif isinstance(list_of_char[i+1],float):
                    return None    
                else:
                    postfix_str = postfix_str + str(list_of_char[i]) + ' '
                
            elif list_of_char[i] in accept_operands:
# NEED TO ADD CHECK IN THE BEGINNING TO MAKE SURE NO CONSECUTIVE OPERANDS OR OPERATORS
                print("operand")
                
                if list_of_char[i] == '+' or list_of_char[i] == '-':
                    print("2nd operand")
                    if postfixStack.isEmpty() == True:
                        print("1st route")
                        nn = Node(list_of_char[i])
                        postfixStack.top = nn
                    else:
                        print("2nd route")
                        while postfixStack.top != None:
                            if postfixStack.isEmpty() == True:
                                break
                                
                            elif postfixStack.top.value == '(':
                                print("correct if taken")
                                postfixStack.pop()
                                print(postfixStack)
                                
                                break

                            elif postfixStack.top.value in ['*', '/', '+', '-', '^']:
                                print(f"entered this if: {postfixStack.top}")
                                postfix_str = postfix_str + str(postfixStack.pop().value) + ' '
                                
                            else:
                                print("no criteria met")

                                return None
                        if postfixStack.isEmpty() == True:
                            print("empty")
                            nn = Node(list_of_char[i])
                            postfixStack.top = nn
                            
                        else:
                            print("not empty")
                            print(postfixStack)
                            nn = Node(list_of_char[i])
                            postfixStack.push(nn)
                            print(postfixStack)
                        
                       
                            
                        
                elif list_of_char[i] == '*' or list_of_char[i] == '/':
                    print("3rd operand")
                    if postfixStack.isEmpty() == True:
                        nn = Node(list_of_char[i])
                        postfixStack.push(nn)
                    elif postfixStack.top.value == '+' or postfixStack.top.value == '-':
                        nn = Node(list_of_char[i])
                        postfixStack.push(nn)
                    else:
                        
                        
                        nn= Node(list_of_char[i])
                        if postfixStack.isEmpty() == True:
                            nn = Node(list_of_char[i])
                            postfixStack.push(nn)
                        else:
                            while postfixStack.top != None:
                                if postfixStack.top.value not in ['+','-','(','*','/']:
                                    postfix_str = postfix_str + postfixStack.pop() + ' '
                                else:
                                    break
                            nn = Node(list_of_char[i])
                            postfixStack.top.next = nn
                            postfixStack.top = nn
                else:
                    print("4th operand")
                    if postfixStack.isEmpty() == True:
                        nn = Node(list_of_char[i])
                        postfixStack.top = nn
                    elif postfixStack.top.value == '+' or postfixStack.top.value == '-' or postfixStack.top.value == '*' or postfixStack.top.value == '/':
                        nn = Node(list_of_char[i])
                        postfixStack.top.next = nn
                        postfixStack.top = nn
                    else:
                        while postfixStack.top.value != '(' or postfixStack.top == None or postfixStack.top.value == '^':
                            postfix_str = postfix_str + postfixStack.pop() + ' '
                        nn= Node(list_of_char[i])
                        if postfixStack.isEmpty() == True:
                            nn = Node(list_of_char[i])
                            postfixStack.top = nn
                        else:
                            nn = Node(list_of_char[i])
                            postfixStack.top.next = nn
                            postfixStack.top = nn
                        

            else:
                print("None case")
                return None

        
        while postfixStack.top != None:
            postfix_str = postfix_str + postfixStack.pop().value + ' '

        postfix_str = postfix_str[0:(len(postfix_str)-1)]

        if postfix_str[-1] == '(':
            postfix_str = postfix_str[0:(len(postfix_str)-2)]

        return postfix_str
                
                


    @property
    def calculate(self):
        '''
            Required: calculate must call postfix
                      calculate must create and use a Stack to compute the final result as shown in the video lecture
            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( ( ( 10 - 2 * 3 ) ) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * ( 3 - 2.45 * ( 4 - 2 ^ 3 ) ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 + 2 * ( 5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + ( 3.0 ) * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 / 3 ) ) - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate

            # For extra credit only. If not attemped, these cases must return None
            >>> x.setExpr('( 3.5 ) ( 15 )') 
            >>> x.calculate
            52.5
            >>> x.setExpr('3 ( 5 ) - 15 + 85 ( 12 )') 
            >>> x.calculate
            1020.0
            >>> x.setExpr("( -2 / 6 ) + ( 5 ( ( 9.4 ) ) )") 
            >>> x.calculate
            46.666666666666664
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression

        # YOUR CODE STARTS HERE
        pass

