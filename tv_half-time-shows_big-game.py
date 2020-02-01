import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


def load_data():
    """ We load the .csv files and then print the first 5 rows """

    halftime_musicians_df = pd.read_csv('halftime_musicians.csv')
    super_bowls_df = pd.read_csv('super_bowls.csv')
    tv_df = pd.read_csv('tv.csv')

    print(halftime_musicians_df.head())
    print(super_bowls_df.head())
    print(tv_df.head())

    return halftime_musicians_df, super_bowls_df, tv_df


def inspect(halftime_musicians_df, super_bowls_df, tv_df):
    """ We print information about the data to have further insights about the
        missing data in the dataframes """

    print(halftime_musicians_df.info())
    print(super_bowls_df.info())
    print(tv_df.info())


def combined_points(super_bowls_df):
    """ We plot a histogram of the combined_points column """

    plt.hist(super_bowls_df['combined_pts'], color='blue')

    """ We add labels and title to the histogram """

    plt.xlabel('Combined points')
    plt.ylabel('Number of Super Bowls')
    plt.title('Histogram of combined points')
    plt.show()

    """ We print the highest and lowest scores """
    print(super_bowls_df[super_bowls_df['combined_pts'] > 70])
    print(super_bowls_df[super_bowls_df['combined_pts'] < 25])


def difference_points(super_bowls_df):
    """ We plot a histogram of the combined groups column """

    plt.hist(super_bowls_df['difference_pts'], color='red')

    """ We add labels and title to the histogram """

    plt.xlabel('Points Difference')
    plt.ylabel('Number of Super Bowls')
    plt.title('Histogram of difference of points')
    plt.show()

    """ We select the data where the difference on points was 1
        and also greater than 35 """

    print(super_bowls_df[super_bowls_df['difference_pts'] == 1])
    print(super_bowls_df[super_bowls_df['difference_pts'] <= 35])


def regression_line(super_bowls_df, tv_df):
    """ We combine the tv dataframe with the super bowl dataframe """

    games_tv = pd.merge(tv_df[tv_df['super_bowl'] > 1], super_bowls_df, on='super_bowl')

    """We plot a regression line"""

    sns.regplot(x="difference_pts", y="share_household", data=games_tv)
    plt.show()


def tv_line_plots(tv_df):
    # Create a figure with 3x1 subplot and activate the top subplot
    plt.subplot(3, 1, 1)
    plt.plot(tv_df['super_bowl'], tv_df['avg_us_viewers'], color="#648FFF")
    plt.title('Average Number of US Viewers')

    # Activate the middle subplot
    plt.subplot(3, 1, 2)
    plt.plot(tv_df['super_bowl'], tv_df['rating_household'], color="#DC267F")
    plt.title('Household Rating')

    # Activate the bottom subplot
    plt.subplot(3, 1, 3)

    plt.plot(tv_df['super_bowl'], tv_df['ad_cost'], color="#FFB000")
    plt.title('Ad Cost')
    plt.xlabel('SUPER BOWL')

    # Improve the spacing between subplots
    plt.tight_layout()
    plt.show()


def most_extreme_game_outcomes(super_bowls_df):
    """ This filters the super bowl data frame to show only rows where the
        difference on points is less or equal to 3 """

    extreme = super_bowls_df[super_bowls_df['difference_pts'] <= 3]
    print(extreme[['date', 'team_winner', 'team_loser', 'difference_pts']])


def main():
    halftime_musicians_df, super_bowls_df, tv_df = load_data()
    inspect(halftime_musicians_df, super_bowls_df, tv_df)
    combined_points(super_bowls_df)
    difference_points(super_bowls_df)
    regression_line(super_bowls_df, tv_df)
    tv_line_plots(tv_df)
    most_extreme_game_outcomes(super_bowls_df)


if __name__ == "__main__":
    main()
