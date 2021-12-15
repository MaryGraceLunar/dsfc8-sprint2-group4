### Example Flask sklearn app

To generate `iris_classifer.joblib` run `train_model.py`.

Then run:

`python app.py`.

Deploy to Heroku with:

```
heroku login

heroku git:remote -a <name of your app>

git push heroku main
```
