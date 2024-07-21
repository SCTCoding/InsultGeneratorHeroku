#!/usr/bin/env python3

from flask import Flask, jsonify, request, render_template_string
import random

app = Flask(__name__)

nouns =  ["airhead", "ass", "babbler", "birdbrain", "blabbermouth", "blockhead", "blunderer", "bonehead", "boob", "buffoon", "cabbagehead", "chatterbox", "chucklehead", "chump", "clod", "clown", "dill", "dimbulb", "dimwit", "dingbat", "dipstick", "dodo", "dolt", "doofus", "dork", "drongo", "dummy", "dunce", "fathead", "fool", "gabber", "galoot", "gibberer", "gibberish", "goober", "goof", "goofball", "goon", "half-wit", "halfwit", "idiot", "ignoramus", "imbecile", "jabberwocky", "jackass", "jerk", "jester", "joker", "jokester", "klutz", "knucklehead", "lamebrain", "loon", "loony", "lout", "moron", "muddlehead", "muffinhead", "muttonhead", "nincompoop", "ninny", "nitwit", "numbskull", "numskull", "oaf", "pea-brain", "pinhead", "plonker", "prat", "rattlebrain", "scatterbrain", "schmuck", "simpleton", "tomfool", "turkey", "twaddle", "twerp", "twit", "wackjob", "wally", "weasel", "whacko", "yahoo", "zany"]
adj = ["absurd", "awkward", "batty", "bizarre", "bonkers", "clumsy", "corny", "cranky", "daffy", "dangling", "dimwitted", "dizzy", "dotty", "droll", "eccentric", "erratic", "fanciful", "far-fetched", "featherbrained", "foolish", "gabby", "giddy", "goofy", "harebrained", "hilarious", "idiotic", "insane", "jabbering", "jocular", "jolly", "kooky", "loony", "loopy", "ludicrous", "madcap", "maniacal", "moist", "moronic", "nonsensical", "nutty", "oddball", "offbeat", "outlandish", "ooze", "peculiar", "preposterous", "plop", "pompus", "quaint", "quirky", "quizzical", "raucous", "ridiculous", "sappy", "screwball", "silly", "tacky", "tactless", "unhinged", "unusual", "verbose", "wacky", "waggish", "youthful", "zany", "zesty"]

last_responses = []

def store_response(response):
    if len(last_responses) >= 10:
        last_responses.pop(0)
    last_responses.append(response)

@app.route('/', methods=['GET'])
def main():
    word1 = random.choice(adj)
    word2 = random.choice([item for item in adj if item != word1])
    word3 = random.choice(nouns)
    response = f'{word1} {word2} {word3}'

    store_response(response)

    table_rows = ''.join(f'<tr><td>{r}</td></tr>' for r in last_responses)
    html_table = f'''
    <h1>{response}</h1>
    <br>
    <table border="1">
        <thead>
            <tr><th>Last 10</th></tr>
        </thead>
        <tbody>
            {table_rows}
        </tbody>
    </table>
    '''
    
    return render_template_string(html_table)

@app.route('/api', methods=['GET'])
def getInsult():
    word1 = random.choice(adj)
    word2 = random.choice([item for item in adj if item != word1])
    word3 = random.choice(nouns)
  
    data = [word1, word2, word3]

    store_response(' '.join(data))
        
    return jsonify(data)

@app.route('/last10', methods=['GET'])
def get_last_10_responses():
    return jsonify(last_responses)

@app.errorhandler(400)
def bad_request(error):
    response = jsonify({'error': 'Bad Request', 'message': str(error)})
    response.status_code = 400
    return response

if __name__ == '__main__':
    main()
