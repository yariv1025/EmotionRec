from src.FrameProvider import FrameProvider
from src.FrameSaver import FrameSaver
import threading
from src.emotic_loop import EmoticLoop
import src.gui
import tkinter as tk
from src.statistics_data_loader import Statistics


def app():
    """
    TODO: ??
    """
    exit_flag = True

    # locks creation
    p_lock = threading.Lock()
    c_lock = threading.Lock()
    locks = [p_lock, c_lock]

    fp = FrameProvider(0)
    statistics = Statistics()
    window = tk.Tk()

    # Create a gui window and pass it to the Application object
    gui = src.gui.App(window, "AttentivnessRec", statistics, exit_flag, fp)

    thread_saver = FrameSaver(2, fp, locks, gui, exit_flag)
    emotic_loop = EmoticLoop(3, fp, locks, gui, exit_flag)

    thread_saver.start()
    emotic_loop.start()
    gui.start()


app()
