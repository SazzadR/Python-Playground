class Egg():

    def __init__( self, kind = 'fried' ):
        self.kind = kind

    def getKind( self ):
        return self.kind

def main():
    egg = Egg( 'scrambled' )
    print( egg.getKind() )

if __name__ == '__main__':
    main()
