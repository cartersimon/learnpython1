# https://www.youtube.com/watch?v=HGOBQPFzWKo&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&start_radio=1&t=181s
# Intermediate Python Programming Course (freecodecamp.org)

# Logging
import logging                                  # 5 diff log levels

# to adjust default display behaviour of log msgs...
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s')
# above doesn't seem to be working for me, check docs/other tutorials

#logging.debug('debug msg')                      # not printed by default
#logging.info('info msg')                        # not printed by default
#logging.warning('warning msg')                  # printed
#logging.error('error msg')                      # printed
#logging.critical('critical msg')                # printed

# by default the logger is called the "root" logger
# to log in other modules, best practice is not to use "root"
# create your own module logger
import logging_helper

# 2:26:07