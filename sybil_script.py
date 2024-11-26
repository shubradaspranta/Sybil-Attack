import random 
import hashlib

#Generate unique Sybil Identities
def generate_identity():
    seed = str(random.random()).encode('utf-8')
    identity = hashlib.sha256(seed).hexdigest()
    return identity


#Simulate sending messages
def send_message(target_node, identity):
    print(f"Sybil node {identity} sending message to {target_node}")


#Main Sybil Attack Simulation 
def sybil_attack(target_node, num_of_sybil_nodes):
    sybil_nodes = [generate_identity() for _ in range(num_of_sybil_nodes)]
    
    for identity in sybil_nodes:
        send_message(target_node, identity)


#Example 
sybil_attack("192.168.1.1", 10) #Here "192.168.1.1 is" the target node and "10" is the number of sybil identity which will be created 