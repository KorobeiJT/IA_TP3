class BDI:
    beliefs=[(0,0),0] #position and state
    desire=1 #0 do nothing - 1 vacuum - 2 pick up jewel 
    intent=0 #0 do nothing - 1 vacuum - 2 move non informed - 3 move informed - 4 pick up jewel