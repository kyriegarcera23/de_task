from app import daily_runtime
import schedule
import time
class Main():
    def __init__(self):
        pass

    def process(self):
        try:
           daily_runtime.Import_ToDB().run_task()
        except Exception as error:
            print(error)
