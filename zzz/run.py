
def numberOfWays(arr):
    ret = 0
    count_z, count_zo, count_o, count_oz = 0, 0, 0, 0
    
    for num in arr:
        if num == '1':
            count_zo += count_z
            count_o += 1
            ret += count_oz
        elif num == '0':
            count_oz += count_o
            count_z += 1
            ret += count_zo
            
    return ret


if __name__ == "__main__":
    print(sortOrders(['m8 fhc mig zqv\r', 'a8 fhc mig zqv anc\r', 'c8 fhc mig zqv anc dfg\r', 'b8 fhc mig zqv anc dfg rbgf ytr ytr abc\r', 'd8 fhc mig zqv anc dfg rbgf\r', 'e8 fhc mig zqv anc dfg rbgf ytr tyu\r', 'f8 fhc mig zqv anc dfg rbgf ytr\r']))
    