from threading import Thread
from cron import addCron
def run():
	tlist = []
	t1 = Thread(target=addCron)
	tlist.append(t1)
	for t in tlist:
		t.start()
	for t in tlist:
		t.join()
if __name__ == '__main__':
	run()