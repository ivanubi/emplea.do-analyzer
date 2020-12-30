## Emplea.do Analyzer
Small CLI tool that scraps all job posts from emplea.do, then it counts the presence of different technologies on each of the posts.

## File Structure
```
.
├── /data/
│   ├── /results/                # Directory where results are saved after running calculate.py.
│   ├── /source/                 # Directory where job posts soon-to-be-analyzed are saved.
│   │   ├── data.json            # Generated file after running 'python3 extract.py'. Contains all job posts from emplea.do in JSON format.
│   │   ├── technologies.json    # List of programming languages, frameworks...
├── extract.py                   # Web scraps every job on emplea.do. Just run it with 'python3 calculate.py'.
│   calculate.py                 # Counts the presence of every language/framework and saves the results on /data/results/ directory.
│   requirements.txt             # Project requirements. Install them with 'pip install -r requirements.txt'.
```

## How it works

It does 3 things:

1. Extracts all job posts from emplea.do then saves it to `/data/source/data.json`.

2. Takes a list of different type of programming languages, frameworks on `/data/source/technologies.json`
and tries to count and find those technologies using the regular expression `(^|[^a-zA-Z])WORD([^a-zA-Z]|$)` after normalizing the jobs posts to lower case.

3. Saves the results to `/data/results/` by year and category of technology.

### Categories
```
{
    "languages": [["javascript"], "html", "css", "python", "java", "c#", "php", "typescript", "c++", "kotlin", "ruby", ["assembly", "asm", "ensamblador"], "swift", "rust", ["objective-c", "objective c"], "scala", "perl", "haskell", "julia", "delphi", "dart"],
    "frontend": ["jquery", ["react", "reactjs", "react.js"], ["angular", "angularjs", "angular.js"], ["vue", "vuejs", "vue.js"], "svelte"],
    "frameworks": [["asp.net", "asp net", "net core", ".net core", "asp", "asp.net core", ".net"], ["express", "expressjs", "express.js"], "spring", "jsf", "grails", "django", "rails", "flask", "laravel", "symfony", "gatsby", "drupal", ["node", "nodejs", "node.js"], "wordpress"],
    "databases": ["mysql",["postgresql", "postgres", "postgre"], "microsoft sql", "sqlite", "mongodb", "redis", "mariadb", "firebase", ["elasticsearch", "elastic search"], "dynamodb", "cassandra", "couchbase"],
    "clouds": [["aws", "amazon web services", "amazon web service", "amazon cloud"], "azure", ["google cloud", "gc"]],
    "mobile": [["react native", "reactnative"], "flutter", ["cordova", "cordovajs", "cordova-js"], "phonegap", "ionic", "xamarin", "nativescript"]
}
```

## How to run it

1. Clone the repo with `git clone https://github.com/ivanubi/emplea.do-analyzer.git` 
2. Install requirements with `pip install -r requirements.txt`.
3. Extract all emplea.do's job posts with `python3 extract.py' (note: this will send more than 1200 requests in just a few seconds to emplea.do).
4. Count the presence of all languages, frameworks... by running `python3 calculate.py`.
5. Check out the results at `/data/results`.

# Results
You can checkout the raw results without even running the script by looking into the `/data/results/` directory or by looking to these beautiful graphics.

### Programming languages:
<img src="https://imgur.com/rivlMF3.png" height="400" />
<img src="https://imgur.com/9wkKeCu.png" height="400" />

### Backend:
<img src="https://imgur.com/3bmVUtG.png" height="400" />
<img src="https://imgur.com/2lElY8J.png" height="400" />

### Frontend:
<img src="https://imgur.com/nfm76Yt.png" height="400" />
<img src="https://imgur.com/7gIP5Un.png" height="400" />

### Databases:
<img src="https://imgur.com/00vMAwQ.png" height="400" />
<img src="https://imgur.com/FBJbJjo.png" height="400" />

### Clouds:
<img src="https://imgur.com/L335Z27.png" height="400" />
<img src="https://imgur.com/6xwV2PR.png" height="400" />

### Mobile hybrid development:

<img src="https://imgur.com/BP1olEJ.png" height="400" />
<img src="https://imgur.com/6e8CKdR.png" height="400" />
