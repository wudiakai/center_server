import time
import os
import threading


def runSyncScheduled():
    TIME_INTERVAL = 30 * 60  #30 minutes
    os.system("sh ./markdown/sync.sh")
    threading.Timer(TIME_INTERVAL, runSyncScheduled).start()


def startMarkdownSync():
    runSyncScheduled()