# imdb_genrePredictor

Every day, over 164 million hours of videos are watched on Netflix globally. That is just one of the multiple video streaming services available in the market, and new entrants are still coming up. Even though the majority of these are Millennial and Gen-Z user, these services are equally famous among other generations. Considering this range of users, and the plethora of content available on these platforms, it has become imperative for these services to make it easier for the users to navigate these platforms and find content most suited to their individual taste. This still remains a key challenge as on average, American adults take 7.4 minutes to decide what to watch on a streaming service.

One of the most used feature while choosing video content is the genre. As such, it is important to ensure that the correct genres are assigned to a video. In this project, we aim to contribute to this task by training a model which takes the name and plot of a video as an input and then predicts the genres which seem relevant to that plot. Since a video can fall in more than one genre, we create a multi-label classification solution. We train this model on data available on the IMDb platform, which is considered as one of the best source of information related to films, television series, home videos, video games, and streaming content online.

This project has been done as a part of individual coursework in data engineering, and the main aim was the deployment of the model. As such, the ML model used is a basic Logistic regression model. 

You can try out the model in the jupyter notebook, callLambdaAPI.ipynb. The model API url is: https://gt70b3mq32.execute-api.eu-west-2.amazonaws.com/default/imdbgenres
