import sys
import curses
from curses_game_screen import GameScreen

def main(screen):
    
    # Make new Game
    s = GameScreen(screen)
    
    # s.board.board[0][0].player = s.board.P1 #1
    # s.board.board[0][1].player = s.board.P1 #2
    # s.board.board[0][2].player = s.board.P0 #3
    # s.board.board[1][0].player = s.board.P0 #4
    # s.board.board[1][1].player = s.board.P2 #5
    # s.board.board[1][2].player = s.board.P2 #6
    # s.board.board[2][0].player = s.board.P0 #7
    # s.board.board[2][1].player = s.board.P0 #8
    # s.board.board[2][2].player = s.board.P0 #9
    
    # Game Loop
    while s.game_is_running:
        
        # If splash screen
        if s.screen_mode == s.SPLASH_SCREEN_MODE:
            
            # Show splash screen
            s.draw_splash_screen()
        
        # if game screen
        elif s.screen_mode == s.GAME_SCREEN_MODE:
            
            # Show the score and game board
            s.draw_game_screen()
        
            # game ready? (which player goes first)
            if s.game_is_ready():
                
                # game rounds (until round over)
                if s.round_over():
                    
                    # play another round?
                    s.play_again()
                    
                else:
                    
                    # (current player makes a move)
                    s.player_turn()
        
        # if quit screen
        elif s.screen_mode == s.QUIT_SCREEN_MODE:
            
            # show the quit confirmation screen
            s.draw_quit_game_screen()

        # Check for key presses
        s.game_is_running = s.key_events()

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        sys.exit(1)
    finally:
        print "Thanks for playing!"