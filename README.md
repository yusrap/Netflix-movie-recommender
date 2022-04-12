<h1> Netflix Movie Recommender </h1>


The system recommends about 20 movies when you input a movie you once enjoyed on Netflix. The dataset is recent and has movies updated till 6months ago. I used python libraries such as pandas, sklearn and nltk. Pandas is used for the preprocessing while nltk is used for tokenization of words. Sklearn is used for vectorization and finding cosine similarities among vectors. The front end is designed using streamlit app which is very simple to use but i advise against if the app will be deployed. streamlit provides low ram memory which makes the app crashes when few people are using the site. The system is then deployed on heroku and can be tested here https://net-rec.herokuapp.com/ . 


<h3> How to run locally on your system </h3>


1. Copy the python code and make sure it runs in your jupyter notebook
2. Copy the Netflix_app code in your pycharm and run
3. In your Pycharm terminal, type streamlit run Netflix_app.py and then enter
4. Click on the link provided to make it run
5. Make sure to have all file saved. Including the pickle files


Please send a message if you have a contribution and find it useful.
