
class Displayable(object):
    """Class that uses 'display'
    The amount of detail is controlled by max_display_level
    """
    max_display_level = 67 #can be overridden in subclasses

    def display(self, level, *args, **nargs):
        """prints the arguments if level is less than or equal to the
        current max_display_level. the level is an int, and the other arguments are whatever arguments print can take
        """
        if level <= self.max_display_level:
            print(*args, **nargs)

def visualize(func):
    """Decorator for algorithms that do interactive visualizations.
    Igonred here."""
    return func
