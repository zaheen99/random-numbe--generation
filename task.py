from time import time

#get values from os
def get_values():
    x1 = x2 = 0
    while not x1 and  not x2:
        #print
        try:
            x1, x2 = int(str(time()-int(time()))[-1]), int(str(time()-int(time()))[-2])
        except ValueError:
            get_values()
    return x1, x2
#return random number and ensure relationship of seeds
#series of values is known as seeds
def values_validation(module,iteration):
    relation=0
    while not relation:
        multiplier, seed = get_values()
        #validity check
        relation = 0 <= iteration < module and 0 <= seed < module  and multiplier in [1,3,7,9]
    return multiplier, seed


    
#seed method of random instance (main method)
def generate(module, iteration):
    multiplier, seed = values_validation(module,iteration)
    output = [seed]
    current_iterate = -1
    switch = False

    while current_iterate != seed and current_iterate != 0:
        if not switch:
            current_iterate = (seed * multiplier) + iteration
            switch=True
        else:
            current_iterate = (current_iterate * multiplier) + iteration
            if current_iterate > module:
                current_iterate %= module
            output.append(current_iterate)

    result = int(str(''.join([str(i) for i in output]))[-1])
    return result


max_list=[]  #initialise a list
min_list=[]  #initialise a minimum list
j=10
i=0
conditions=True
rounds=100
while conditions:
    n = generate(j,i)
    if n >= 5:
        if len(max_list)<73:
            max_list.append(n)

        else:
            if len(min_list)<27:
                min_list.append(n)
        if len(max_list) == 73 and len(min_list) == 27:
            conditions=False

# here is length of maximum  list
len_max=len(max_list)
print("the length of maximum list is {}".format(len_max))

# here length of minimum list
len_min=len(min_list)
print("The length of minimum list is {}".format(len_min))
print("\n")
print("maximum list:--\n\n{}".format(max_list))

print("-----------------------------------------------------------------------------")
print("------------------------------------------------------------------------------")

print("minimum_list:--\n\n{}".format(min_list))
            
