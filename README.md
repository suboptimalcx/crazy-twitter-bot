# BABYS FIRST TWITTER BOT

A simple twitter bot i created for fun using twitters free API v2. 

---

## FEATURES

- reposts tweets containing certain keywords  
- replies to tweets with a custom message (Automated replies may violate X's TOS!!! this feature is included for learning purposes!!)
- chooses a randomly selected line from a text file and tweets it

---

## HOW TO USE

### PREREQUISITES

1. generate your API keys on the x developer portal, make sure to select Read and Write permissions!
2. install required python packages:
   ```bash
   pip install tweepy python-dotenv
   ```
3. create a `.env` file in the project root containing your API credentials:
   ```
   CONSUMER_KEY=your_consumer_key
   CONSUMER_SECRET=your_consumer_secret
   ACCESS_TOKEN=your_access_token
   ACCESS_TOKEN_SECRET=your_access_token_secret
   ```
4. run and go nuts

---