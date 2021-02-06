package game;

import java.util.*;

public class Rook extends Piece
{
    public Rook(char x, int y, boolean color, String name){super(x, y, color, name);}

    public boolean canMove(char x, int y)
    {
        if( this.x - x == 0 || this.Y_CHANGED - y == 0 )
        {
            return true;
        }
        return false;
    }

    public static boolean canMove(Piece p, char x, int y)
    {
        if( p.x - x == 0 || p.Y_CHANGED - y == 0 )
        {
            return true;
        }
        return false;
    }

    public boolean checkWay(ArrayList<Piece> pieces, char x, int y)
    {
        int xShift = 0;
        int yShift = 0;

        if( this.x - x == 0 || this.Y_CHANGED - y == 0 )
        {
            if( this.x - x != 0 )
            {
                xShift = (this.x - x) / Math.abs(x - this.x);
            }

            if( this.Y_CHANGED - y != 0 )
            {
                yShift = (this.Y_CHANGED - y) / Math.abs(y - this.Y_CHANGED);
            }
            int i = 1;
            boolean flag = true;

            while( this.x != (char)(x + i * xShift) || this.Y_CHANGED != y + i * yShift )
            {
                if( checkTaken(pieces, (char)(x + i * xShift), y + i * yShift) != null && !(checkTaken(pieces, (char)(x + i * xShift), y + i * yShift) instanceof King) )
                {
                    flag = false;
                }
                i++;
            }
            return flag;
        }
        else
        {
            return false;
        }
    }


    public static boolean checkWay(Piece p, ArrayList<Piece> pieces, char x, int y)
    {
        int xShift = 0;
        int yShift = 0;

        if( p.x - x != 0 || p.Y_CHANGED - y != 0 )
        {
            if( p.x - x != 0 )
            {
                xShift = (x - p.x) / Math.abs(x - p.x);
            }

            if( p.Y_CHANGED - y != 0 )
            {

                yShift = (y - p.Y_CHANGED) / Math.abs(y - p.Y_CHANGED);
            }
            int i = 1;

            while( x != (char)(p.x + i * xShift) || y != p.Y_CHANGED + i * yShift )
            {
                if( checkTaken(pieces, (char)(p.x + i * xShift), p.Y_CHANGED + i * yShift) != null && !(checkTaken(pieces, (char)(p.x + i * xShift), p.Y_CHANGED + i * yShift) instanceof King) )
                {
                    return false;
                }
                i++;
            }
            return true;
        }
        else
        {
            return false;
        }
    }
}