'''Write a set of Python classes that can simulate an Internet application
 in which one party, Alice, is periodically creating a set of packets that 
 she wants to send to Bob. An Internet process is continually checking if
  Alice has any packets to send, and if so, it delivers them to Bob’s 
  computer, and Bob is periodically checking if his computer has a packet 
  from Alice, and, if so, he reads and deletes it.'''
import random, time, threading

class Internet:
	'''Internet'''
	def __init__(self, status=False):
		self.status = status

	def check_packet(self):
		'''computer checks itself if it has a packet'''
		if len(self.packet)>0:
			return True
		else:
			return False

	def delete_packet(self):
		'''Need to change it, so it completely clears value'''
		self.packet = []

	def send_packet(self, pc1, pc2):
		if len(pc2.packet)>0:
			pc2.packet.append(pc1.packet)
		else:
			pc2.packet = pc1.packet
		print(f'Sending....a new packet:{pc2.packet} to {pc2.name}......')
		pc1.delete_packet()

class Computer(Internet):
  	'''Computer'''

  	def __init__(self, name):
  		'''Create a new computer instance.
  		name - the name of the person it belongs to
  		packet - the packet it created/received
		packets_received - number of packets received by the object
		packets_created - number of packets created by the object
  		'''
  		self.name = name
  		self.packet = []
  		self.packets_created = 0
  		self.packets_received = 0

  	def create_packet(self):
  		if not self.packet==None:
  			new_packet = random.sample(range(0, 101), 3)
  			self.packet.append(new_packet)
  		else:
  			self.packet = random.sample(range(100), 3)
  		self.packets_created += 1

  	def read_packet(self):
  		'''Checks if there is a packet. If there is prints it and then deletes it'''
  		if self.packet:
  			print(f'{self.name} - Reading packet...... Packet found: {self.packet}')
  			self.packets_received += 1
  			self.delete_packet()
  		else:
  			print(f'{self.name} - Reading packet...... Packet found: {self.packet}')

'''Create Alice and Bob computers'''
alice = Computer('Alice')
bob = Computer('Bob')
network = Internet()
i = 1
'''Alice creates a packet'''
while i <= 10:
	if i%2==0:
		alice.create_packet()
		'''If alice has a packet, it gets sent to bob'''
		print('\n')
	if alice.packet:
		print(f'Alice has a packet ready: {alice.packet}')
		network.send_packet(alice, bob)
		print('\n')
	'''If bob has a packet, he reads it and then deletes it.'''
	if i%3==0:
		bob.read_packet()
		print('\n')
	i+=1

print(f'Alice created {alice.packets_created} packets.' )
print(f'Bob received {bob.packets_received} packets.' )













