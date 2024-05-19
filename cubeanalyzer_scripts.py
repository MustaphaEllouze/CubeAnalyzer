import argparse

from cubeanalyzer.card_data.cards_parser import CardsParser

class ScriptsLauncher:

    @classmethod
    def parse_args(cls, )->None:
        parser = argparse.ArgumentParser(
            prog='Cube Analyzer scripts',
            description='Script that launches several data analyzing functions for MtG Cubes.',
        )

        parser.add_argument(
            '-c', '--cards',
            help='Add cards from the cards meta-language file in the data file.',
            action='store_true',
        )

        parser.add_argument(
            '-d', '--decks',
            help='Add decks from the decks meta-language file in the decks file.',
            action='store_true',
        )

        parser.add_argument(
            '-g', '--games',
            help='Add games from the game meta-language file in the games file.',
            action='store_true',
        )

        parser.add_argument(
            '-C', '--compile',
            help='Compile the data from the games to compute new elo for cards.',
            action='store_true',
        )

        parser.add_argument(
            '-i', '--id',
            help='Prints the possible ID for the given card name.'
        )

        return parser.parse_args()
    
    @classmethod
    def run_scripts(cls, )->None:
        arguments = ScriptsLauncher.parse_args()

        if arguments.cards : CardsParser.parse_metafile()

if __name__ == '__main__':
    ScriptsLauncher.run_scripts()