# Naïve Bayes Classifier for NBA Players

![banner](https://github.com/jacquelinekclee/naivebayes_nba_players/blob/main/nba_players.jpeg)

[SOURCE](https://medium.com/325-sports/top-5-nba-goats-791078488f22)

# Table of contents

- [Background](#background)
- [The Statistics](#the-statistics)
- [Statistics Source](#statistics-source)
- [The methodology](#the-methodology)
- [Goal](#goal)
- [Usage](#usage)
- [Findings](#findings)
- [Legality](#legality)
- [Source Files](#source-files)

## Background
As someone who has been playing basketball since the second grade and has been a Warriors fan since birth, the NBA and basketball in general has always held a special place in my heart. There are several questions in the world of basketball that will forever be debated such as: 
- Has basketball become a positionless sport, where you don't need to play the sport with the traditional point guard, shooting guard, small forward, power forward, and center?
- Who is the GOAT (greatest of all time)?
- Has the game really changed over the years?
- Do the numbers truly never lie? 

Using data and the Naïve Bayes approach to classification, I seek to find answers to these questions. Using a Naïve Bayes classifier, I will use statistics from nearly 19,000 players' seasons from 1980-2017. I will then test my classifier using statistics from the 2018-19 season (the most recent "normal" NBA season) and the current season's statistics to see if the numbers can answer any of the sport's burning questions.

[(Back to top)](#table-of-contents)

## The Statistics
The NBA tracks almost 50 different statistics for every player in the league. For the purposes of this project, I will only use statistics that must be greater than or equal to 0 since using Gaussian naïve Bayes only works for positive values. Additionally many of the statistics are dependent on each other, and for naïve Bayes to work, we must naïvely assume that the features (statistics) are independent. Furthermore, many statistics are often unknown to most basketball fans, so using only the common statistics will make the most sense for everyone. 
Here are some basic definitions of the statistics I will be using in my classifier:
- True shooting percentage (TS%): a metric that demonstrates how efficiently a player shoots the ball. Takes into consideration field goals, 3-pointers, and free throws (unlike other metrics like field goal percentage).
- Rebounds per game (RPG): a metric that shows how many total rebounds (both offensive and defensive) a player averages per game. 
- Assists per game (APG): a metric that shows how many total assists a player averages per game.
- Points per game (PPG): a metric that shows how many total points a player averages per game.
- Blocks per game (BPG): a metric that shows how many total blocks a player averages per game.
- Steals per game (SPG): a metric that shows how many total steals a player averages per game.

[(Back to top)](#table-of-contents)

## Statistics Source
The training data comes from [Kaggle](https://www.kaggle.com/drgilermo/nba-players-stats?select=Seasons_Stats.csv). The test data come from https://www.basketball-reference.com/.  

[(Back to top)](#table-of-contents)

## The Methodology:
This naïve Bayes classifier uses two different approaches. In one, I discretize the statistics, categorizing each statistic into their respective quartiles, and use the data with the traditional Bayes' Theorem:
$$ P(class | features) = P(features | class) * P(class) / P(features) $$
In the other approach, I used the statistics as they are (continuous data) and used Gaussian naïve Bayes where 
$$ p(x=v\mid C_{k})={\frac {1}{\sqrt {2\pi \sigma _{k}^{2}}}}\,e^{-{\frac {(v-\mu _{k})^{2}}{2\sigma _{k}^{2}}}}} $$

[(Back to top)](#table-of-contents)

Here are some quick definitions of terms used in this project:
* **[Bar](https://www.lexico.com/en/definition/bar)**: One line of lyrics. Detected by line break characters. Typically takes four beats.
* **[End rhymes](https://literarydevices.net/end-rhyme/)**: Rhymes that occur with the last word/syllables of a bar. Example: "I like greens / She likes beans" (greens and beans, the last word of each bar/line, rhyme).
* **[Exact rhyme](https://literarydevices.net/exact-rhyme/)**: When the vowel sound and final consonant of two words are phonetically the same, e.g. greens and beans.
* **[Vowel rhyme](https://www.thefreedictionary.com/vowel+rhyme)**: When the vowel sound of two words are phonetically the same, e.g. green and seem.
* **[Stop word](https://www.geeksforgeeks.org/removing-stop-words-nltk-python)**: A word that does not contribute much meaning, e.g. the, a, an. Search engines are programmed to ignore these words, and ignoring these words both save processing time and allow us to analyze lyrics more meaningfully.

[(Back to top)](#table-of-contents)

## Goal
As stated above, this project has some limitations in terms of the consistency of lyric data, the extent to which the packages/tools used can analyze rap lyrics, and the overall subjectivity of this topic. Ultimately, I started this project as a fun way to both explore one of my interests and utilize the skills and technical knowledge I have learned thus far. But, I certainly believe that the results of this project can give insight into how rap music has evolved over the years.

[(Back to top)](#table-of-contents)

## Usage

Please refer to the [Jupyter Notebook viewer](https://nbviewer.jupyter.org/github/jacquelinekclee/hiphop_nlp_webscrape/blob/master/Has%20Hip-Hop%20Gotten%20Worse_.ipynb) to view all the code and visualizations created during this project.

The [source files](#source-files) contain all the functions used to web scrape, process the text, and calcualte the metrics used for the project.

[(Back to top)](#table-of-contents)

## Findings
While all four metrics seemed to decline over the years, **% Unique Rhymes to All Rhymes** (number of unique rhymes / number of all rhymes) proved to be the metric with:
- The strongest correlation coefficient (-0.52)
- Lowest p-value (p = 0.003)

![scatter](https://github.com/jacquelinekclee/hiphop_nlp_webscrape/blob/master/rhymes_plot.png)

Even though what qualifies as "good music" will always be subjective, quantifying the quality of lyrics in these songs proved to be insightful. The generally weak relationships between each metric and year indicate that any "decline" in hip-hop/rap music may not be as strong as some would assume. 

As mentioned above, hip-hop has become the most popular genre of music. With this ever increasing popularity comes more commercial and lucrative opportunities, and such opportunities are not necessarily conducive to lyrically complex and intricately crafted songs. The genre becoming more commerical and marketable does not mean that there are no lyrically interesting songs being made. But, this trend may contribute to an oversaturated market, where mostly catchy, less intricate songs become popular.

Overall, this project gives evidence that hip-hop as a genre has not seen a dramatic decline. Instead, changing trends in the music industry and how the public consumes media may affect what types of songs become most popular, but not necessarily the skills of all rappers.  

[(Back to top)](#table-of-contents)
 
## Source Files
* [web_scrape.py](https://github.com/jacquelinekclee/hiphop_nlp_webscrape/blob/master/web_scrape.py)
  * Has all the functions used for web scraping and processing the HTML. It also processes the string (lyrics) so it's ready for analyzing the lyrics.
* [lyrics.py](https://github.com/jacquelinekclee/hiphop_nlp_webscrape/blob/master/lyrics.py)
  * Used to break down the string of lyrics into bars and words and calculate the word based metrics.
* [rhyme.py](https://github.com/jacquelinekclee/hiphop_nlp_webscrape/blob/master/rhyme.py)
  * Provides the functions used to calculate the rhyme-based metrics
  * The contents of this file are adopted from the dandelion package as laid out [here](https://github.com/DiegoVicen/dandelion). Edits made by me (jacquelinekclee) are denoted in the docstrings.
 
 ## Legality
 
 This personal project was made for the sole intent of applying my skills in Python thus far and as a way to learn new ones. It is intended for non-commercial uses only.
 
 Some issues with webscraping from AZLyrics arose as I was developing this project because the website detected an unusual amount of activity. An alternative to AZLyrics is
 [archive.org](https://archive.org/), a website that regularly stores archives for various webpages. Nonetheless, using the [Jupyter Notebook viewer](https://nbviewer.jupyter.org/github/jacquelinekclee/hiphop_nlp_webscrape/blob/master/Has%20Hip-Hop%20Gotten%20Worse_.ipynb) should not present any issues.
 
[(Back to top)](#table-of-contents)
