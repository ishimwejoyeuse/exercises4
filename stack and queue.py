from collections import deque
print()
print("----------- stack operations--------------")
print()
print("______ task1_____________")
print('Practical (Rwanda): In MoMo, push ["Step1", "Step2", "Step3"]. Pop 2. Which step remains')
stack=[]
stack.append('step1')
stack.append('step2')
stack.append('step3')
print("the element in stack before popping two element:",stack)
stack.pop()
stack.pop()
print("after popping two steps the remaining step is:",stack)
print()
print("task2:Practical (Rwanda): UR pushes topicA,topicB,topicC. Undo 1. Which is left")
print()
stack=['topic A','topic B','topic C']
print("the element in stack before popping one topic:",stack)
stack.pop()
print()
print("the topic which is left after popping one topic is :",stack)
print()
print("--------task3:challenge-------------")
print('Challenge: Push ["1", "2", "3", "4"], pop twice. What remains')
print()
stack = [] #initialize an empty stack
stack.append(1)#push element onto stack 
stack.append(2)#push element onto stack 
stack.append(3)#push element onto stack 
stack.append(4)#push element onto stack 
print('the element in the stack before pop twice:',stack)#display an element in the stack
stack.pop()#remove an element from the stack
stack.pop()#remove another element from the stack
print('the remaing element in the stack is',stack)#print the remaining elements
print()
print('-----------task4:reflection-----------')
print()
print('why stack are unsuitable for queue in daily life')
print('------------------------------------------------')
print(' 1. Stacks: Follow the Last-In-First-out (LIFO) principle,')
print(' where the last element added is the first one tobe removed.')
print('2.Queue: follow the First-In-Last-Out (FIFO) principle,')
print('where the first element added is the first one to be removed')
print('In daily life queues are often used to manage tasks, request, or people in fair and orderly manner.')
print('Stack,on the other hand, are not suitable for queues in daily life because:')
print('.unfair ordering: stack would prioritize the most recent additions,')
print(' which could lead to unfair treatment of those who have been waiting longer.')
print('.In efficient management: stacks would require constant reordering to ensure fairness,')
print('which could lead to in efficiencies and confusion.')
print()
print('===============end of question 1============================')
print()
print("_______Q2.queue operations_______________")
print()
print(" task1:At BK ATM, 9 clients queue. After 5 served, who is front?")
print()
queue=list(range(1,10))
print("initial queue :",queue)
served_clients=5
remaining_queue =queue[served_clients:]
print("the remaining queue:",remaining_queue)

front_client = remaining_queue[0]
print("the client at the front:",front_client )
print()
print("task2: At Nyabugogo, 8 buses enqueue. Who is served second?")
print()
buses=list(range(1,9))
print("buses enqueue :",buses)
first_served = buses[0]
second_served = buses[1]
print("first bus served:",first_served)
print("second bus served:",second_served)
print('TASK3.Challenge: Queue vs stack for concert entry. Which works better?')
#queue approach
print('queue approach')
queue=[] #initialize an empty queue
queue=list(range(1,6))#push an element in stack by using loop
queue.append(6)#add person to the end of queue)
print(queue)
queue.pop(0)#remove person from the front of the queue
print(queue)
print()
#stack approach
print('stack approach')
stack=[] #initialize an empty stack
stack=list(range(1,6))#push an element in stack by using loop
stack.append(6)#add person to the top of the stack
print(stack)#display the person entered in the stack
stack.pop()#remove person from the top of the stack
print(stack)
print()
print('queue wark better in concert than stack becouse it follows the First-In-First-Out principle,'
      'ensuring that peaple enter in the concert in the order they arrived')
print()
print(' TASK4.:Reflection: Why FIFO keeps order at public events?')
print()
print('becouse:preserving temporal order: FIFO maintains the temporal order of arrival, ensuring that individuals who')
print('arrive first served first. This preserve the natural order of events and prevents chaos.')
print('Ensuring fairness and equity: FIFO ensure that everyone is treated equally and fairly, regardless of their')
print('social status, wealth, or influence. It eliminates favoritism and bias, promotion a sense of justice and equality.')
print('.Enabling efficient resource allocation')
print(' This result in a smooth, enjoyable, and fair experience for all participants.')
print(' Example: At concert, people waiting in line to buy tickets are served in the order they arrived (FIFO). This ensure that:')
print('1.those who arrived first get tickets first')
print('2.the line moves in a predictable and orderly manner')