import json
import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Start by asking about the path

path = input('Enter filepath for tinder.json on your computer here:')

open_tinder = open(path, 'r')
loading_tinder = json.load(open_tinder, encoding= 'utf-8')

app_opens = pd.DataFrame.from_dict(loading_tinder['Usage'])

first_date = app_opens['app_opens'].index[0]
last_date = app_opens['app_opens'].index[-1]

dti = pd.date_range(first_date, last_date, freq='D')
dates = pd.Series(dti.format(str))


all_dates = {'app_opens': {},
             'matches': {},
             'messages_received': {},
             'messages_sent': {},
             'swipes_likes': {},
             'swipes_passes': {},
             }

for date in  dates:
    all_dates['app_opens'][date] = 0
    all_dates['matches'][date] = 0
    all_dates['messages_received'][date] = 0
    all_dates['messages_sent'][date] = 0
    all_dates['swipes_likes'][date] = 0
    all_dates['swipes_passes'][date] = 0


# And create a Dataframe from the above dictionary
tinder_data_all_dates = pd.DataFrame.from_dict(all_dates)

#Add the 2 above dictionaries
tinder_data = pd.concat([app_opens, tinder_data_all_dates], sort= False)
# Remove duplicates
tinder_data = tinder_data.loc[~tinder_data.index.duplicated(keep='first')]
# Sort it
tinder_data.sort_index(inplace=True)



sum_of = tinder_data.sum(axis = 0)
maxim = tinder_data.max()

# Here are some calculations I know I will use many times
def percentage_ratio(fac1, fac2):
    per  = round(((fac1 / fac2) * 100), 2)
    return per


def division(fac1, fac2):
    div = round((fac1 / fac2), 2)
    return div

total_swipes = sum_of['swipes_likes'] + sum_of['swipes_passes']
ratio_likes = percentage_ratio(sum_of['swipes_likes'], total_swipes)
ratio_passes = percentage_ratio(sum_of['swipes_passes'], total_swipes)
matches_to_likes = percentage_ratio(sum_of['matches'],sum_of['swipes_likes'])
messages_ratio = percentage_ratio(sum_of['messages_sent'], (sum_of['messages_received'] + sum_of['messages_sent']))

daily_sent = division(sum_of['messages_sent'],sum_of['app_opens'])
daily_swipes = division(total_swipes,sum_of['app_opens'])
daily_right = division(sum_of['swipes_likes'],sum_of['app_opens'])
daily_left = division(sum_of['swipes_passes'], sum_of['app_opens'])
daily_matches = division(sum_of['matches'], sum_of['app_opens'])



#Lets start the analysis!

print ('\n--------------HERE IS YOUR TINDER DATA---------------\n\nSWIPES-----------------------')


print('The total amount of swipes you did during your tinderperiod is', total_swipes, 'swipes.'
      '\nOf your total swipes you right swiped', ratio_likes,  '% \nand swiped left ', ratio_passes,
      '% \nOf all of your right swipes, you matched with ', matches_to_likes, '%. \nWhich results in a total of '
      , sum_of['matches'], ' matches.'
      )

print('\nMESSAGES-------------------- \nWhen it comes to your messages, here are your stats:'
      '\n\nYou sent ', sum_of['messages_sent'], 'messages. \nAnd received ', sum_of['messages_received'], ' messages'
      '\nThat means you sent ', messages_ratio, '% of all your messages')

print('\nGENERAL------------------------'
      '\nFor everytime you opened the app you... \n...sent ', daily_sent , 'messages.'
      '\n...swiped on ', daily_swipes, ' people.'
      ' (Right swipes: ', daily_right, ', Left swipes: ', daily_left, ')'
      '\n...matched with ', daily_matches, ' people.')

print('\nMAX-----------------------------'
      '\nWow one can almost say you are addicted. These are your highest numbers:\n',
      maxim['swipes_passes'],'left swipes \n',
      maxim['swipes_likes'], 'right swipes \n',
      maxim['matches'], 'matches\n',
      maxim['messages_sent'], 'messages sent'
      '\n\nDoes it feel like any number is too high?\n------------------- THAT WAS ALL ------------------')


# Creating a plot with different interesting subplots
fig, axs = plt.subplots(2,2)
fig.suptitle('My Tinder Data', fontsize=14, fontweight='bold')

#Plot for how many right swipes I did and with how many I matched with
axs[0,0].plot(tinder_data['matches'])
axs[0,0].plot(tinder_data['swipes_likes'])
axs[0,0].title.set_text('Swipes to Matches Ratio')
axs[0,0].legend(('Macthes', 'Right Swipes'))
axs[0,0].set(ylabel = '[n]', xticks = [tinder_data.index[1], tinder_data.index[-1]],
            xticklabels = [tinder_data.index[1], tinder_data.index[-1]])

# Plot for how many messages I sent and received
axs[0,1].plot(tinder_data['messages_sent'])
axs[0,1].plot(tinder_data['messages_received'])
axs[0,1].legend(('Sent', 'Received'))
axs[0,1].title.set_text('Messages Sent/ Received ratio')
axs[0,1].set(ylabel = '[n]', xticks = [tinder_data.index[1], tinder_data.index[-1]],
            xticklabels = [tinder_data.index[1], tinder_data.index[-1]])

#Plot showing if there is correlation between right swipes and matches
axs[1,0].scatter(tinder_data['messages_sent'], tinder_data['messages_received'], color = 'k')
axs[1,0].title.set_text('Correlation between messages sent and received')
axs[1,0].set(xlabel = 'Messages Sent', ylabel = 'Messages Received')
z = np.polyfit(tinder_data['messages_sent'], tinder_data['messages_received'], 1)
p = np.poly1d(z)
axs[1,0].plot(tinder_data['messages_sent'],p(tinder_data['messages_sent']), 'k')
axs[1,0].spines['top'].set_visible(False)
axs[1,0].spines['right'].set_visible(False)

n = np.arange(len(app_opens))

axs[1,1].bar(n, app_opens['swipes_passes'], color='r', edgecolor='white', width = 1)
axs[1,1].bar(n, app_opens['swipes_likes'],  bottom= app_opens['swipes_passes'],
             color='g', edgecolor='white', width=1)
axs[1,1].title.set_text('Distribution of likes/passes of total swipes')
axs[1,1].set(xlabel = 'Daily Swipes', ylabel = '[n]', xticks = [], xticklabels = [])
axs[1,1].legend(('Swipes Passes', 'Swipes Likes'))

plt.show()



