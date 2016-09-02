from lib.games import Game

def main():
    """
    Main entry point for Github Adventures
    """
    game = Game()
    game.setup_game()
    game.run()

if __name__ == '__main__':
    main()