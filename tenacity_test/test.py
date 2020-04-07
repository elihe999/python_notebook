from tenacity import retry,stop_after_attempt
import random
# import requests

@retry(stop=stop_after_attempt(3))
def do_something_unreliable():
    print( "count" )
    if random.randint(0, 10) > 1:
        raise IOError("Unstable status, try again")
    else:
        print("Get stable result")



res = do_something_unreliable()
print(res)
