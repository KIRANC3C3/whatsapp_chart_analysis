import re # re means regular expression
import pandas as pd
def total(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{1,2}\s-\s'
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    # creating dataframe
    df = pd.DataFrame({'user_messages': messages, 'message_data': dates})
    # convert message_data frame
    df['message_data'] = pd.to_datetime(df['message_data'], format='%d/%m/%Y, %H:%M - ')
    df.rename(columns={'message_data': 'dates'}, inplace=True)
    users = []
    messages = []
    for message in df['user_messages']:
        entry = re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            # messages.append(re.split('[\n]',entry[2]))
            messages.append(entry[2])
        else:
            users.append('group notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df['month_num'] = df['dates'].dt.month
    df['year'] = df['dates'].dt.year
    df['month_name'] = df['dates'].dt.month_name(locale='English')

    df = df.drop(columns='user_messages', axis=1)
    return df


