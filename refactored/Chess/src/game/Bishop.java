package game;

import java.util.*;

public class Bishop extends Piece
{
    public Bishop(char x, int y, boolean color, String name){super(x, y, color, name);}

    public boolean canMove(char x, int y)
    {
        if( Math.abs(this.x - x) != 0 && Math.abs(this.Y_CHANGED - y) != 0 && Math.abs((float)(this.x - x) / (this.Y_CHANGED - y)) == 1 )
        {
            return true;
        }
        return false;
    }

    public static boolean canMove(Piece p, char x, int y)
    {
        if(  Math.abs(p.x - x) != 0 && Math.abs(p.Y_CHANGED - y) != 0 && Math.abs((float)(p.x - x) / (p.Y_CHANGED - y)) == 1 )
        {
            return true;
        }
        return false;
    }

    public static boolean checkWay(Piece p, ArrayList<Piece> pieces, char x, int y)
    {
        if( p.x - x == 0 )
        {
            return false;
        }

        if( p.Y_CHANGED - y == 0 )
        {
            return false;
        }
        int xShift = (x - p.x) / Math.abs(x - p.x);
        int yShift = (y - p.Y_CHANGED) / Math.abs(y - p.Y_CHANGED);
        int i = 1;

        while( x != (char)(p.x + i * xShift) && y != p.Y_CHANGED + i * yShift )
        {
            if( checkTaken(pieces, (char)(p.x + i * xShift), p.Y_CHANGED + i * yShift) != null && !(checkTaken(pieces, (char)(p.x + i * xShift), p.Y_CHANGED + i * yShift) instanceof King) )
            {
                return false;
            }
            i++;
        }
        return true;
    }

    public boolean checkWay(ArrayList<Piece> pieces, char x, int y)
    {
        int xShift = (x - this.x) / Math.abs(x - this.x);
        int yShift = (y - this.Y_CHANGED) / Math.abs(y - this.Y_CHANGED);
        int i = 1;
        while( x != (char)(this.x + i * xShift) && y != this.Y_CHANGED + i * yShift )
        {
            if( checkTaken(pieces, (char)(this.x + i * xShift), this.Y_CHANGED + i * yShift) != null && !(checkTaken(pieces, (char)(this.x + i * xShift), this.Y_CHANGED + i * yShift) instanceof King) )
            {
                return false;
            }
            i++;
        }
        return true;
    }
}