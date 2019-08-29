import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print("Hello! Let\'s explore some US cities bikeshare data!\n")

    while True:
        city = input("Would you like to visualize data for Chicago, New York City or Washington?\n").lower()
        if city.lower() not in ('chicago', 'new york city', 'washington'):
        #if city not in CITY_DATA.keys():
            print("Sorry, {} is not a valid city. Please type again by entering either 'Chicago', 'New York City' OR 'Washington' again".format(city))
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("which month would you like to analyze? | (e.g. for january, please input [1])\n")
        if month.lower() not in ('1','2','3','4','5','6'):
            print ("please enter the correct input. | (e.g. for january, please input [1])\n")
        else:
            break

    #while True:
        #month = input("Which month? January, February, March, April, June or all?\n").lower()
        #months = ['january', 'february', 'march', 'april', 'may', 'june','all']
        #if month not in months:
            #print("Sorry, {} is not a valid month. Please type again by entering again".format(month))
            #continue
        #else:
            #break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("which day of week shall we analyze?\n")
        if day.lower() not in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
            print ("please enter the correct input.\n")
        else:
            break
    """while True:
        day = input("Which day? Please type a day M, T, W, Th, F, Sa, Su, A for All.\n")
        days = {'M':'Monday','T':'Tuesday','W':'Wednesday','Th':'Thursday','F':'Friday','Sa':'Saturday','Su':'Sunday','A':'All'}
        if day not in days.keys():
            print("Sorry, {} is not a valid day. Please type a day using one of the following values: M, T, W, Th, F, Sa, Su, A for All.".format(day))
            continue
        else:
            break
    """
    print('-'*50)
    return city, month, day


"""
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable

    if month !='all':
        months = ['1', '2', '3', '4', '5', '6']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable

    if day !='all':
    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    #TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is", common_month)

    # TO DO: display the most common day of week

    common_day_of_week = df['day_of_week'].mode()[0]
    print("{} is the most common day".format(common_day_of_week))

    # TO DO: display the most common start hour

    df["hour"] = df["Start Time"].dt.hour
    common_start_hour = df["hour"].mode()[0]
    print("{} is the most common hour".format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def station_stats(df):
    #"""Displays statistics on the most popular stations and trip."""

    print('Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("{} is the most commonly used start station".format(common_start))

    # TO DO: display most commonly used end station

    common_end = df['End Station'].mode()[0]
    print("{} is the most commonly used end station".format(common_end))

    # TO DO: display most frequent combination of start station and end station trip

    #most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    #print("The most commonly used start station and end station : {}, {}".format(most_common_start_end_station[0],most_common_start_end_station[1]))
    df['Trip'] = df['Start Station'] + "-" + df['End Station']
    common_trip = df['Trip'].mode()
    print("{} is most frequent combination of start station and end station trip".format(common_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_duration = df['Trip Duration'].sum()
    print("Total travel time:",total_duration)

    # TO DO: display mean travel time

    average_duration = df['Trip Duration'].mean()
    print("Average travel time:",average_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print("Counts of user types:",user_types)

    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print("Counts of gender:",gender_types)
    else:
        print('No gender data is found')

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        birth_year_earliest = df['Birth Year'].min()
        birth_year_recent = df['Birth Year'].max()
        birth_year_common = df['Birth Year'].mode()[0]
    else:
        print('No age data is found')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

def display_data(df):
    user_input = input('\nWould you like to see individual raw data?\nPlease enter yes or no\n').lower()
    if user_input in ('yes', 'y'):
        i = 0
        while True:
            print(df.iloc[i:i+5])
            i += 5
            more_data = input('Would you like to see more data? Please enter yes or no: ').lower()
            if more_data not in ('yes', 'y'):
                break






def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
           break


if __name__ == "__main__":
    main()
