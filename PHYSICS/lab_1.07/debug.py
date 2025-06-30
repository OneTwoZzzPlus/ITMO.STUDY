from meas import *

if __name__ == "__main__":
    Drawer().plot_dependency(
        1, 1,
        [Measurement(10, 1), Measurement(20, 2), Measurement(30, 3)],
        [Measurement(15, 1), Measurement(25, 2), Measurement(35, 3)]        
    )