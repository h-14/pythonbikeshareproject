import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    #Todo accessing keys from dictionary 
    city_list = list(CITY_DATA.keys())
            
    while True:
        city = input("Enter Valid city name:").lower()
        if city in city_list:
            break;
        else:
            print("enter Valid city name: 'new york city' / 'chicago'/ 'washington'")
            
            
        

    # TO DO: get user input for month (all, january, february, ... , june)
    #month = input("Enter valid month:").lower()
    month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']    
    while True:
        month = input("Enter valid month name:").lower()
        if month in month_list:
            break;
        else:
            print("valid month: 'all'/ 'january'/ 'february'/ 'march'/ 'april'/ 'may'/ 'june'")
            


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']    
    while True:
        day = input("Enter valid day:").lower()
        if day in day_list:
            break;
        else:
            print("enter Valid month name: 'all'/ 'monday'/ 'tuesday'/ 'wednesday'/ 'thursday'/ 'friday'/ 'saturday'/               'sunday'")
            
    
    


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['Trip'] = df['Start Station'] + " - " + df['End Station']

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    print (df['month'].mode()[0])


    # TO DO: display the most common day of week
    print (df['day_of_week'].mode()[0])


    # TO DO: display the most common start hour
    print (df['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
 # TO DO: display most commonly used start station
    print (df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print (df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    print (df['Trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
     
    #df['A'].corr(df['B'])
    
    print(" sum --" , travel_time)
    print(" mean --" , mean_travel_time)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    

    print("Counts of User Types --\n", user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df.index:
        print("Counts of User Types --\n", df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.index:
        print("earliest year of birth --", df['Birth Year'].min())
        print("most recent year of birth --", df['Birth Year'].max())
        print("most common year of birth --", df['Birth Year'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def correlation_stats(df):
    """ Display correlation between the columns. """
    print('\nCalculating Correlation Stats...\n')
    start_time = time.time()
    correlation_stats = df.corr()
    print("Correlation between the columns -- \n", correlation_stats)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
           
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        correlation_stats(df)
        
        print ("Analysing data for .... {},{},{}".format(city,month,day))

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
