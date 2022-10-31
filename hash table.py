class hashtable:
    def __init__(self, items):
        self.bucket_size = len(items)
        self.buckets = [[] for i in range(self.bucket_size)]
        self.assign_buckets(items)

    def assign_buckets(self, items):
        for key, value in elements:
            hash_value = hash(key)
            index = hash_value % self.bucket_size
            self.buckets[index].append((key, value))
            
    def get_value(self, input_keys):
        hash_value = hash(input_keys)
        index = hash_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_keys:
                return(value)
