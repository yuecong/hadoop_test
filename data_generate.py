import uuid
NUM_LINE = 1000 * 277777 #to generate 10GB data
NUM_LINE = 1000 * 300000 #to generate 10GB data
NUM_LINE = 100

for i in range(0,NUM_LINE):
    print(uuid.uuid4())
