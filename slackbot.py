import requests
from slack_webhook import Slack

data = requests.get("https://www.coronavirus.in.gov/map/covid-19-indiana-universal-report-current-public.json")
data = data.json()

#MoCo cumsum stats
moco_covid_cumsum_count = data['metrics']['daily_statistics']['covid_cases'][52]
moco_covid_cumsum_deaths = data['metrics']['daily_statistics']['covid_deaths'][52]
#moco_covid_cumsum_tests = data['metrics']['daily_statistics']['covid_tests'][52]

#MoCo stats
moco_new_cases = data['metrics']['daily_statistics']['daily_delta_cases'][52]
moco_new_deaths = data['metrics']['daily_statistics']['daily_delta_deaths'][52]


slack = Slack(url='https://hooks.slack.com/services/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')

try:
    slack.post(text='Indiana just updated its COVID-19 dashboard. Here are the latest numbers for Monroe County:\n\nCumulative case count: ' + str(moco_covid_cumsum_count) + '\nCumulative deaths: ' + str(moco_covid_cumsum_deaths) + '\n\nThe county has seen ' + str(moco_new_cases) + ' cases and ' + str(moco_new_deaths) + ' deaths in the last day.')
    
except:
    slack.post(text='There\'s been an issue! @vivrao')