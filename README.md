# Kind of Stupid Apache Joshua Client

This is a really simple demonstration of consuming an [Apache Joshua](https://joshua.apache.org/) API.

To use:
```bash
python3 joshua_client.py
```

The script as it is will only translate the Holy Words but the ```translate``` can be changed to use any string.

*Note that the Apache Joshua endpoint referenced in the script is severely broken and doesn't actually translate
anything. However, it should still be indicative how how to consume the API.*

## API

Apache Joshua exposes a [subset of the Google Translate API](https://cwiki.apache.org/confluence/display/JOSHUA/RESTful+API).

Request:
```bash
$ curl "localhost:5674/translate?meta=list_weights&q=cifra+inferior+a+lo+que+predec%C3%ADan+las+encuestas+%2C+que+pronosticaban+de+mas+del+60+%25+de+participaci%C3%B3n+electoral+.&q=yo+quiero+taco+bell"
```

Response:
```json
{
  "data": {
    "translations": [
      {
        "translatedText": "Figure less than what the polls predicted, claiming more than 60 % of electoral participation.",
        "raw_nbest": [
          {
            "hyp": "figure less than what the polls predicted , claiming more than 60 % of electoral participation .",
            "totalScore": -8.429729
          }
        ]
      },
      {
        "translatedText": "I want taco bell",
        "raw_nbest": [
          {
            "hyp": "i want taco bell",
            "totalScore": -3.8622975
          }
        ]
      }
    ]
  },
  "metadata": [
    "weights tm_custom_0\u003d0.000 tm_pt_0\u003d0.004 tm_pt_1\u003d0.029 tm_pt_2\u003d0.002 tm_pt_3\u003d0.325 tm_pt_4\u003d0.106 tm_pt_5\u003d0.087 OOVPenalty\u003d0.006 WordPenalty\u003d-0.090 lm_0\u003d0.221 Distortion\u003d0.094 PhrasePenalty\u003d-0.002 lm_1\u003d0.034"
    ]
}
```
