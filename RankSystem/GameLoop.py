import threading
import time


class GameLoop(threading.Thread):
    def __init__(self,rank_service):
        self.rank_service = rank_service
        self.rank_service_running = True
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        while self.rank_service_running:
            time.sleep(1)
            self.rank_service.polling_value()

