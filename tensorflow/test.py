import tensorflow as tf


def main():
    hello = tf.constant('Hello')
    sess = tf.Session()
    sess.run(hello)
    a = tf.constant(10)
    b = tf.constant(10)
    sess.run(a + b)
    sess.close()

if __name__ == '__main__':
    main()
