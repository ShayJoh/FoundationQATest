'''
Note:
In order to run the script, one must install Pandas via pip3

pip3 install pandas

'''


import pandas as pd

# Turn 'finished' etc into constants

# Define as many cases as possible
eb_df = pd.read_csv('processed_output.csv')
eb_df_started = eb_df[eb_df['Result']=='started']
eb_df_finished = eb_df[eb_df['Result']=='finished']
eb_df_message = eb_df[eb_df['Result']=='message']
eb_df_without = eb_df[eb_df['Result']=='without']
eb_df_build = eb_df[eb_df['Result']=='build']
eb_df_failed = eb_df[eb_df['Result']=='failed']
eb_df_ios_fail = eb_df[   (eb_df['Platform']=='iOS') & (eb_df['Result']=='failed') ]
eb_df_and_fail = eb_df[   (eb_df['Platform']=='Android') & (eb_df['Result']=='failed') ]
eb_df_build_fail = eb_df[   (eb_df['Platform']=='Build') & (eb_df['Result']=='failed') ]
eb_df_ios_started = eb_df[   (eb_df['Platform']=='iOS') & (eb_df['Result']=='started') ]
eb_df_and_started = eb_df[   (eb_df['Platform']=='Android') & (eb_df['Result']=='started') ]
eb_df_and_finished = eb_df[   (eb_df['Platform']=='Android') & (eb_df['Result']=='finished') ]
eb_df_ios_finished = eb_df[   (eb_df['Platform']=='iOS') & (eb_df['Result']=='finished') ]

# Define grouping by Project
group_by_proj = eb_df.groupby('Project')

# Define sets created by Result and Platform (ie, the unique names used)
setR = set(eb_df['Result'])
setP = set(eb_df['Platform'])

#RE DO ALL CALCS AS THE FOLLOWING
'''
calcs = {
    'perFinished': (eb_df_finished, eb_df['Result']),
}

def do_calc(d1, d2):
    return round(len(d1) / len(d2) * 100, 2)

results = {}
for result_name, data in calcs.items():
    results[result_name] = do_calc(*data)
'''

# Define % of various use cases
perFinished = round(len(eb_df_finished) / len(eb_df['Result']) * 100, 2)
perFinishedios = round(len(eb_df_ios_finished) / len(eb_df_ios_started) * 100, 2)
perFinishedand = round(len(eb_df_and_finished) / len(eb_df_and_started) * 100, 2)
perFailed = round(len(eb_df_failed) / len(eb_df['Result']) * 100, 2)
perFailedios = round(len(eb_df_ios_fail) / len(eb_df_failed) * 100, 2)
perFailedand = round(len(eb_df_build_fail) / len(eb_df_failed) * 100, 2)

# Grouping by project name (index), and counting all associated Failures
projects_failed = group_by_proj['Result'].apply(
    lambda x: (x=='failed').sum()
    ).reset_index(name='Failed Count')

# Display Results
print("\nPercentage of projects finished: ", perFinished,"%")
print("Percentage of attempts failed: ", perFailed,"%")
print("Percentage of failed Builds were iOS: ", perFailedios,"%")
print("Percentage of failed builds were Android: ", perFailedand,"%")
print("Percentage of iOS Builds that finished: ", perFinishedios,"%")
print("Percentage of Android Builds that finished: ", perFinishedand,"%\n")

# Print Project that has failed the most, and print sorted projects that have failed more than 5 times
# in descending order
print("\nProject that failed the most: \n", projects_failed[projects_failed['Failed Count'] == max(projects_failed['Failed Count'])])
print("\nProjects that failed >5 times: \n", projects_failed[projects_failed['Failed Count'] > 5].sort_values(['Failed Count'], ascending=False))


# How Many Failed? Done
# Failure Rate? Done
# Success Rate? Done
# Most common Platform Failed? Done
# Most common Project Failed? Done

