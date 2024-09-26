class Ghost:
  def __init__( self,name,color):
    self.name = name
    self.color = color
    self.is_transformed = False
    
  
  def move( self ):
    print( f'{self.name} is moving!')
  
  
  def touch( self, pacman):
    print( 'GAME OVER!' )
  