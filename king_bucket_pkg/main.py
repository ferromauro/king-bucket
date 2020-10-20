from kb import KingBucket
import time
kb = KingBucket()
kb.create_bucket('provamauro')
time.sleep(3)
kb.delete_bucket('provamauro')