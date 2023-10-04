"""
Template application
"""

from wolf_core import application


class Template(application.Application):
    """
    Notion2Latex
    """

    def __init__(self):
        super().__init__()

    def job(self):
        print("Starting job...")
        print("Finished job.")


def main():
    """

    This is the documentation for the method main().

    :returns: None
    """
    __import__("wolf_core.api")
    __import__("wolf.notion")
    app = Template()
    result = app.job()


if __name__ == "__main__":
    main()
