import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days = ['sunday','monday','thuseday','wednesday','thursuday','friday','saturday','all']
filters = ['month','day','both','none']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('      '+'-'*100)
    print('      \u01C0                                                                                                  \u01C0')
    print('      \u01C0                                Hello! Let\'s explore some US bikeshare data!                      \u01C0')
    print('      \u01C0                                                                                                  \u01C0')
    print('      \u01C0       ** This programe is desgined to calculate some statistics related to bike share systems    \u01C0 \n      \u01C0        for three major cities in the United States—Chicago, New York City, and Washington **     \u01C0')
    print('      \u01C0                                                                                                  \u01C0')
    print('      \u01C0                           << Note: Data for the first six months of 2017 >>                      \u01C0')
    print('      \u01C0                                                                                                  \u01C0')
    print('      \u01C0                                        Data provided by Motivate                                 \u01C0')
    print('      \u01C0                                                                                                  \u01C0')
    print('      \u01C0        Programe desgined by Yasser Galal             Cohort(18)             Nov.2021             \u01C0')
    print('      '+'-'*100)
    print()
    print()
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("What you like to see data for : Chicago, New York City or Washington? \n").lower()
  
    # Check user input in city
    while city not in CITY_DATA:
        city = input('Invaild Input , Please input one of three cities (Chicago, New York City or Washington) : \n').lower()       
    
    # get user input for filter options
    filter_options = input('What do you want to filter for Month , Day , Both or None? \n').lower()
    
    # Condational funcation to choose filter
    while filter_options not in filters :
        filter_options = input('Please select vaild filter choose ( Month , Day , Both or None) \n').lower()
    
    if filter_options == 'both' :
    
        # get user input for month (all, january, february, ... , june)
        month = input("Which month? ( All, January, February, ... , June ) \n").lower()
        while month not in months:
            month = input ('Invaild month , Please choose from January to June or all \n').lower()
            return month
        
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input ("Which day ? (All,Sunday,Monday,Thuseday,Wednesday,Thursuday,Friday,Saturday) \n").lower()
        while day not in days:
            day = input ('Invaild day , Please write correctly day name again \n')
            return day
 
    elif filter_options == 'month' :
        
        # get user input for month (all, january, february, ... , june)
        month = input("Which month? ( All, January, February, ... , June ) \n").lower()
        while month not in months:
            month = input ('Invaild month , Please choose from January to June or all \n').lower()
            
        day = 'all'
        
    elif filter_options == 'day' :
        
        # get user input for day of week (all, monday, tuesday, ... sunday)
         day = input ("Which day ? (All,Sunday,Monday,Thuseday,Wednesday,Thursuday,Friday,Saturday) \n").lower()
         while day not in days:
             day = input ('Invaild day , Please write correctly day name again \n')
             
         month = 'all'
    else:
         month = 'all'
         day = 'all'


    
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
    df['day_of_week'] = df['Start Time'].dt.day_name()

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
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
    # display the most common month
    df['month'] = df['Start Time'].dt.month_name()
    common_month = df['month'].mode()[0]
    print ('The most common month is {} \n'.format(common_month))
   
    # display the most common day of week
    df['day'] = df['Start Time'].dt.day_name()
    common_day = df['day'].mode()[0]
    print ('The most common day of week is {} \n'.format(common_day))
  
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print ('The most common start hour is {} \n'.format(common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_st = df['Start Station'].mode()[0]
    print ('The most commonly used as start station is {} \n'.format(common_start_st))
    
    # display most commonly used end station
    common_end_st = df['End Station'].mode()[0]
    print ('The most commonly used as end station is {} \n'.format(common_end_st))
    
    # display most frequent combination of start station and end station trip
    common_comb_st = df[['Start Station','End Station']].mode().loc[0]
    print ('The most commonly used Trip is from {} to {} \n'.format(common_comb_st[0],common_comb_st[1]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print ('Total Travel Time is {} seconds'.format(total_time))
    years_num = int(total_time // (60*60*24*365))
    total_time %= (60*60*24*365)
    months_num = int(total_time // (60*60*24*12))
    total_time %= (60*60*24*12)
    days_num = int(total_time // (60*60*24))
    total_time %= (60*60*24)
    hour_num = int(total_time // (60*60))
    total_time %= (60*60)
    min_num = int(total_time // 60)
    total_time %= 60
    sec_num = total_time
    if years_num != 0 :
        print ('\nThat represent   {} years , {} months , {} days , {} hours , {} minutes , {} seconds'.format(years_num,months_num,days_num,hour_num,min_num,sec_num))
    elif years_num == 0 and months_num != 0:
        print ('\nThat represent   {} months , {} days , {} hours , {} minutes , {} seconds'.format(months_num,days_num,hour_num,min_num,sec_num))
    elif years_num == 0 and months_num == 0 and days_num != 0:
        print ('\nThat represent   {} days , {} hours , {} minutes , {} seconds'.format(days_num,hour_num,min_num,sec_num))
    elif years_num == 0 and months_num == 0 and days_num == 0 and hour_num != 0:
        print ('\nThat represent   {} hours , {} minutes , {} seconds'.format(hour_num,min_num,sec_num))
    elif years_num == 0 and months_num == 0 and days_num == 0 and hour_num == 0 and min_num != 0:
        print ('\nThat represent   {} minutes , {} seconds'.format(min_num,sec_num))
    else :
        print ('\nThat represent   {} seconds'.format(sec_num))    
        
    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print ('\nMean Travel Time is {} seconds'.format(mean_time))
    years_num1 = int(mean_time // (60*60*24*365))
    mean_time %= (60*60*24*365)
    months_num1 = int(mean_time // (60*60*24*12))
    mean_time %= (60*60*24*12)
    days_num1 = int(mean_time // (60*60*24))
    mean_time %= (60*60*24)
    hour_num1 = int(mean_time // (60*60))
    mean_time %= (60*60)
    min_num1 = int(mean_time // 60)
    mean_time %= 60
    sec_num1 = mean_time
    if years_num1 != 0 :
        print ('\nThat represent   {} years , {} months , {} days , {} hours , {} minutes , {:.2f} seconds'.format(years_num1,months_num1,days_num1,hour_num1,min_num1,sec_num1))
    elif years_num1 == 0 and months_num1 != 0:
        print ('\nThat represent   {} months , {} days , {} hours , {} minutes , {:.2f} seconds'.format(months_num1,days_num1,hour_num1,min_num1,sec_num1))
    elif years_num1 == 0 and months_num1 == 0 and days_num1 != 0:
        print ('\nThat represent   {} days , {} hours , {} minutes , {:.2f} seconds'.format(days_num1,hour_num1,min_num1,sec_num1))
    elif years_num1 == 0 and months_num1 == 0 and days_num1 == 0 and hour_num1 != 0:
        print ('\nThat represent   {} hours , {} minutes , {:.2f} seconds'.format(hour_num1,min_num1,sec_num1))
    elif years_num1 == 0 and months_num1 == 0 and days_num1 == 0 and hour_num1 == 0 and min_num1 != 0:
        print ('\nThat represent   {} minutes , {:.2f} seconds'.format(min_num1,sec_num1))
    else :
        print ('\nThat represent   {:.2f} seconds'.format(sec_num1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users_count = df['User Type'].value_counts()
    print ('\n \nTotal number of user typs are the following \n{}'.format(users_count))
    
    # Display counts of gender
    if 'Gender' not in df.columns:
        print ('\n No Gender data is given for this country \n')
    else :
        gender_counts = df['Gender'].value_counts()
        print ('\n \nTotal number of Genders are the following \n{}'.format(gender_counts))
    
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print (' NO Birth Year data is given for this country \n')
    else :
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print()
        print()
        print ('The earliest year of birth year is : {} \n'.format(earliest_year))
        print ('The most recent year of birth year is : {} \n'.format(recent_year))
        print ('The most common year of birth year is : {} \n'.format(common_year))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data (df):
    """ Funcation to display 5 random sample of raw data as per input request"""
    
    print('\nCalculating Display Raw Data...\n')
    start_time = time.time()
    
    # User response to display 5 sample of raw data
    view_data = input("\nWould you like to view 5 rows of individual trip data? Enter yes or no? \n").lower()
    user_response = ['yes','no']
    sample = 0
    # Loop to display 5 raw data as per user input
    while view_data == 'yes':
          print(df.iloc[sample : sample+5])
          view_data = input("Do you wish to display more sample of data (yes or no)?: \n").lower()
          sample += 5
    # Check user response and display next 5 raw data if need
    while view_data not in user_response:
        view_data= input('Invaild input , Please write (yes or no) \n').lower()
        while view_data == 'yes':
            print(df.iloc[sample : sample+5])
            view_data = input("Do you wish to display more sample of data (yes or no)?: \n").lower()
            sample += 5
                      
                      
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
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
