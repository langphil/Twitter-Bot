*Use this py script to tweet to a twitter account with content located in a .txt file.*

1) Enter in Twitter auth details in tweet.py.

2) Place content in text.txt (each individual tweet should go on a new line).

3) Setup a cron job on your RPI (if this is what you are using) to run at a set time.

4) Every time a tweet is sent a +1 number will be written to counter.save.

5) Eavery time a new tweet is sent counter.save will be read to work out what line to tweet.
