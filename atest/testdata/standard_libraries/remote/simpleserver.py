import sys
from SimpleXMLRPCServer import SimpleXMLRPCServer


class SimpleServer(SimpleXMLRPCServer):

    def __init__(self, port=8270):
        SimpleXMLRPCServer.__init__(self, ('localhost', int(port)))
        self.register_function(self.get_keyword_names)
        self.register_function(self.run_keyword)
        self.serve_forever()

    def get_keyword_names(self):
        return ['Passing', 'Failing', 'Traceback', 'Returning', 'Logging']

    def run_keyword(self, name, args):
        if name == 'Passing':
            return {'status': 'PASS'}
        if name == 'Failing':
            return {'status': 'FAIL', 'error': ' '.join(args)}
        if name == 'Traceback':
            return {'status': 'FAIL', 'traceback': ' '.join(args)}
        if name == 'Returning':
            return {'status': 'PASS', 'return': ' '.join(args)}
        if name == 'Logging':
            return {'status': 'PASS', 'output': '\n'.join(args)}


if __name__ == '__main__':
    SimpleServer(*sys.argv[1:])
