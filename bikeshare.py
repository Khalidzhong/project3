#导入项目会用到的库包
import time
import pandas as pd
import numpy as np

#建立字典，方便读取对应的文本
CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def input_mod(input_print, error_print, enterable_list, get_value):
    while True:
        ret = input(input_print)
        ret = get_value(ret)
        if ret in enterable_list:
            return ret
        else:
            print(error_print)

#输对应的数据（城市，月份，日期）
def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # 输入城市名字，仅限于 'Chicago'，'New York City','Washington'
    city = input_mod('Please input the city name : \n',
                    'Error!Please input the correct city name.',
                    ['Chicago', 'New York City', 'Washington'],
                    lambda x: str.title(x))

    # 输入月份，仅限于'All', 'January', 'February', 'March', 'April', 'May', 'June'
    month = input_mod('Please input the month name: \n',
                    'Error!Please input the correct month name.',
                    ['All', 'January', 'February', 'March', 'April', 'May', 'June'],
                    lambda x: str.title(x))

    # 输入日期，仅限于'All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday', 'Sunday'
    day = input_mod('Please input the day name: \n',
                    'Error!Please input the correct day name.',
                    ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Saturday', 'Sunday'],
                    lambda x: str.title(x))

    print('-'*40)
    return city, month, day


#根据输入的城市，月份，日期的数据进行筛选读取数据
def load_data(city, month, day):
    
    #使用read_csv读取数据
    df = pd.read_csv(CITY_DATA[city.title()])
    
    #将 Start Time列的数据类型改成datetime,方便后续数据处理
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #提取Start Time列的数据，并且新增month列和day_of_week列
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month.title() != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)+1
    if day.title() != 'All':
        df = df[df['day_of_week']== day.title()]
    
    return df

#统计最常出行的时间
def time_stats(df):
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # 最常出行月份
    popular_month = df['Start Time'].dt.month.mode()[0]
    print('Most Popular month:', popular_month)

    # 最常出行日期
    popular_day = df['Start Time'].dt.weekday_name.mode()[0]
    print('Most Popular day:', popular_day)


    # 最常出行小时
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most Popular hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#统计最受欢迎的站点
def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # 最受欢迎的开始站
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular start station:', popular_start_station)

    # 最受欢迎的结束站
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular end station:', popular_end_station)

    # 最受欢迎的路线
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    popular_combination = df['combination'].mode()[0]
    print('Most Popular combination:', popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#统计使用时间
def trip_duration_stats(df):
   
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # 总共使用时间
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travrl Time:', total_travel_time)


    # 平均使用时间
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travrl Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#统计使用的人群类型
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # 使用人群的类型
    counts_user_types = df['User Type'].groupby(df['User Type']).count()
    print(counts_user_types,'\n')

    # 使用人群的性别
    if 'Gender' in df:
        counts_of_gender = df['Gender'].groupby(df['Gender']).count()
        print(counts_of_gender,'\n')
    else:
        print('Gender data does not exist')


    # 使用人群的年龄分布
    if 'Birth Year' in df:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
        print('earliest year of birth:', earliest_birth)
        print('most recent year of birth:', recent_birth)
        print('most common year of birth:', common_birth)
    else:
        print('Birth data does not exist')


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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
