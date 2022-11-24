import click
import pandas as pd

@click.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('--verbose', '-v', is_flag=True, help='Verbose mode.')
def main(filename, verbose):
    '''Simple program that imputes NULL values in a csv.'''
    if verbose:
        click.echo('In verbose mode!')
    df = pd.read_csv(filename)
    if df.isnull().values.any():
        click.echo('There are NULL values in the dataframe.')

if __name__ == '__main__':
    main()