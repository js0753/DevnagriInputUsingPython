def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    from pynput.mouse import Listener
except ImportError:
    install('pynput')
    from pynput.mouse import Listener
import logging

logging.basicConfig(filename="mouse_log.txt",level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_click(x,y,button,pressed):
    if pressed:
        logging.info("({0},{1})".format(x,y))

with Listener(on_click=on_click) as listener:
    listener.join()
