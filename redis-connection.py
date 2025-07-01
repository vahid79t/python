import redis
import time
count=0
pool = redis.ConnectionPool(host="192.168.1.75", port=6379, db=0)
redis = redis.Redis(connection_pool=pool)

# for i in range(1,5):
#     key='key{}'.format(i)
#     value='value{}'.format(i)
#     redis.set(key,value)
# r = redis.Redis()
# r.flushdb()
# bool = True
try:
    while bool:
        count+=1
        # time.sleep(1)
        key='key{}'.format(count)
        value='value{}'.format(count)
        print(key)
        print(value)
        redis.set(key,value)
except KeyboardInterrupt:
    pass
