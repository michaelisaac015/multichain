from Savoir import Savoir

class Blockchain(object):


    @staticmethod
    def initialize():
        rpcuser = 'multichainrpc'
        rpcpasswd = 'bxWt3gLGaTJQ5mPQBp2bjERsVJSLhwjRu9WpJcSL2bs'
        rpchost = 'localhost'
        rpcport = '8346'
        chainname = 'chain01'
        api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)
        return(chainname)