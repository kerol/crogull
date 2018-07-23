# coding: utf-8
class Management:

    def __init__(self, argv):
        self.argv = argv

    def commands(self):
        return {
            'runserver': self.cmd_runserver,
            'help': self.cmd_help,
        }

    def execute(self):
        try:
            cmd = self.argv[1]
        except IndexError:
            cmd = 'help'
        if cmd not in self.commands():
            cmd = 'help'
        func = self.commands()[cmd]
        func()

    def cmd_runserver(self):
        from .app import app
        app.run()

    def cmd_help(self):
        print('available commands: python manage.py')
        for cmd in self.commands():
            print('- {}'.format(cmd))


def execute_from_command_line(argv):
    management = Management(argv)
    management.execute()
