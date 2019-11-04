import pandas as pd
import bson
import re
from pandas.io.json import json_normalize
from itertools import chain
from flask import Flask
import flask

app = Flask(__name__)

@app.route("/")
def home():


    def metrica():
        #with open('ConciertoExaAlans.bson','rb') as b:
        df = pd.read_json('Tweets.json', lines=True)
            #df = pd.DataFrame(bson.decode_all(b.read()))

        htags = json_normalize(df.entities)
        def htgs1 (lst):
            b = []
            for e in lst:
                b.append(e['text'])
            return (b)
        c = htags['hashtags'].apply(htgs1)
        e = list(chain.from_iterable(c))
        x = pd.Series(e)
        x = x.str.capitalize()
        y = x.value_counts()

        Retweet=str(df['retweet_count'].sum())
        Reply= str(df.reply_count.sum())
        Contributors = df.contributors.value_counts()
        Contributors = Contributors[:5]

        Tweets = df.shape[0]
        users = json_normalize(df.user)
        names = users.name
        user5 = names.value_counts()
        user5 = user5.to_frame()
        user5 = str(user5.head().index.tolist())
        Top5Users = user5

        influ = users[['name', 'followers_count', 'friends_count']].copy()
        influ = influ.sort_values('followers_count', ascending = False)
        influ = influ.drop_duplicates(subset ="name")
        influencers = str(influ.head().name.tolist())

        enguser=list(names.unique())
        Reach = str(len(enguser))
        y = y.to_frame()
        y = str(y.head().index.tolist())
        TopHashtags = y


        print('Total de Tweets: ', Tweets)
        print(' ')
        print ('Numero de Retwwets:', Retweet)
        print(' ')
        print ('Numero de Replies:', Reply)
        print(' ')
        print('Numero de Reachs:', Reach)
        print(' ')
        #print('No se tiene acceso a las Impresiones')
        #print('Top 5 Contribudores:', Contributors)

        print ('Top 5 Users: ' + Top5Users)
        print(' ')
        print ('Top 5 Hastags: ' + TopHashtags)
        print(' ')
        print ('Top Influncers: ' + influencers)

        #metrics = {}

        #for i in ('Tweets', 'Retweet', 'Reply', 'Reach', 'Contributors', 'Top5Users', 'TopHashtags'):
            #metrics[i] = locals()[i]
        #metrics = f

        return flask.jsonify({'Tweets': Tweets,'Retweet':Retweet, 'Reply':Reply, 'Reach':Reach,
                              'Top5Users':user5, 'TopInfluencers':influencers,'TopHashtags':TopHashtags})

    return metrica()

if __name__ == "__main__":
    app.run(debug=True)

