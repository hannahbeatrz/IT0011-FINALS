import os # imported os 
def create_table():
    if os.path.isfile('Products.txt'): #checks if path already exists
        with open('Products.txt', 'a') as file: #append if true
            file.write("id\tname\tin_stock\n")
    else:
        with open('Products.txt', 'w+') as file: #create new if false
                file.write("id\tname\tin_stock\n")

def fetch_products():
    products = []
    with open('Products.txt', 'r') as file:
        # next(file) # For skipping the header/column names
        for line in file:
            product = line.strip().split('\t')
            products.append(product)
    return products

def insert_product(id, name, in_stock):
    with open('Products.txt', 'a') as file:
        file.write(f"{id}\t{name}\t{in_stock}\n")

def delete_product(id):
    with open('Products.txt', 'r') as file:
        lines = file.readlines()
    
    # Reopen the file in write mode to overwrite the file
    with open('Products.txt', 'w') as file:
        for line in lines:
            # If the line does not start with the id to be deleted, write it back to the file
            if not line.startswith(f"{id}\t"):
                file.write(line)
            
            

def update_product(new_name, new_stock, id):
    with open('Products.txt', 'r') as file:
        lines = file.readlines()
    
    # Reopen the file in write mode to overwrite the file
    with open('Products.txt', 'w') as file:
        updated = False
        for line in lines:
            # If the line starts with the id to be updated, write the new values to the file
            if line.startswith(f"{id}\t"):
                file.write(f"{id}\t{new_name}\t{new_stock}\n")
                updated = True
            elif updated == False:
                file.write(line)
                updated = False
                
            
        
        
      

def id_exists(id):
    with open('Products.txt', 'r') as file:
        # next(file) # For skipping the header/column names
        for line in file:
            if line.startswith(f"{id}\t"):
                return True
    return False

# create_table()