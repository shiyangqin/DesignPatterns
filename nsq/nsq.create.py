import nsq
import tornado.ioloop
import time


def pub_message():
    writer.pub('test_topic', time.strftime('%H:%M:%S'), finish_pub)


def finish_pub(conn, data):
    print data


writer = nsq.Writer(['10.255.175.48:4150'])
tornado.ioloop.PeriodicCallback(pub_message, 1000).start()
nsq.run()
