# Judge ⚖️ 
![judge (1)](https://user-images.githubusercontent.com/41021374/88198064-eccce880-cc60-11ea-8356-c86f7caddac8.png)


![GitHub](https://img.shields.io/github/license/arthtyagi/judge?style=flat-square)
[![codebeat badge](https://codebeat.co/badges/4c2604cd-3940-40e6-83e9-8ec2ed3eeab4)](https://codebeat.co/projects/github-com-arthtyagi-judge-master)
![Discord](https://img.shields.io/discord/723603615582912512?color=black&logo=discord&logoColor=white)
![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/arthtyagi/judge/django)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/arthtyagi/judge)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/django)
[![Downloads](https://pepy.tech/badge/django-judge)](https://pepy.tech/project/django-judge)
[![Downloads](https://pepy.tech/badge/django-judge/month)](https://pepy.tech/project/django-judge/month)
[![Downloads](https://pepy.tech/badge/django-judge/week)](https://pepy.tech/project/django-judge/week)

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/arthtyagi/judge)

![image](https://user-images.githubusercontent.com/41021374/88192318-0454a300-cc5a-11ea-9b2a-1baa9597b957.png)

An online judge built with Python and the Django framework to test cases against your solution. A better version of this is to be implemented in DomeCode. Check out the sponsor links and help fund DomeCode.

I'm trying to build an online judge to allow users of DomeCode to practice coding problems online. DomeCode is a project of mine in the making that allows people to learn code by practicing,participating in DomeCode's forum and using the resources compiled from all over the internet and woven together to create a one-stop experience for programmers.

**The autograder for DomeCode is also being built on top of this with more ramifications and a few more features for the first release. But in actuality, this is the underlying piece of code in the most minimalistic way.**

**Tl,dr; This package just compares your solution text to the actual solution for the question. It just adds some ease of use to that task. You need to add the solutions to your questions from the admin and that's it, you're done. The use will upload their solution in the text form, this library will compare those two solutions and grade accordingly.**

Update : **Now we just use the Judge0 RapidAPI at DomeCode, might consider building an alternative to it.**

## Why? 🤔

To put it simply, adding a compiler like Cloud9 IDE or Sphere online judge is gonna cost me some bucks so initially I plan on building an in-house solution to allow users to practice coding problems like they did on Google Kickstart before 2019 or the way Coursera's autograder does. I hope this works out since the concept is sound as per my understanding.

## How to use this? 💡

- Add “coder” to your INSTALLED_APPS setting like this:
```
INSTALLED_APPS = [
    ...
    'coder',
]
```
Include the polls URLconf in your project urls.py like this:

`path('coder/', include('coder.urls')),`
Run python manage.py migrate to create the polls models.

- Run the migrations!
- Run the server. And get on your [`localhost:8000/admin`](https://localhost:8000/admin/)
- You will notice the coder app and it's models quite like this :
![image](https://user-images.githubusercontent.com/41021374/88209550-7e902200-cc70-11ea-9860-7a9cf432514c.png)

- Create a new question. I included the RichTextEditor too so that should make it easier to include photos, symbols, charts and more.
![image](https://user-images.githubusercontent.com/41021374/88210496-ee52dc80-cc71-11ea-9f41-dc763fa61e9f.png)
![image](https://user-images.githubusercontent.com/41021374/88210743-47227500-cc72-11ea-86ae-16e5abe16969.png)

I just submitted the correct solution and as you can see, the autograder evaluated it as a correct answer.
![image](https://user-images.githubusercontent.com/41021374/88210883-7cc75e00-cc72-11ea-83da-943840635cf5.png)


- Yes, I know. I need to add a checkmark next to the question if it's evaluated correct but this is just to show that the autograder works and you can head back to the homepage of the website and submit your answer to the question! The possibilities tread as far as your imagination on how to use this. Modify this code to suit your purpose, it's MIT Licensing so have at it!

**Most importantly though, if you liked using this, STAR ⭐ and FORK 🍴 this repository. That would make me happier and I would feel motivated to add new exciting features to this.**

## How does the autograder work so blazingly fast?

If you actually used this, you might be wondering how does the autograder make the process so blazingly fast in comparision to other autograders that might take a while ( ~10-15 secs whereas this app does it within ~2-3 seconds ), the reason lies within the fact that it never actually reads from the disk while evaluating the user's solution, it directly reads from the memory and does not overwhelm the system either since text files are generally smaller.


## You should know this!

If this project actually gets a decent number of stars and forks, I will be implementing a few more core features to this including but not limited to :

- [X] ~~Search functionality 🔍~~

- [ ] Displaying whether the answer is correct in Question's submission panel. ✅

- [X] ~~Displaying whether the question attempted by the user is correct in the Question List View. ✅~~
![image](https://user-images.githubusercontent.com/41021374/88254206-1d993600-ccd2-11ea-99a1-0fd0d42dac81.png)

- [ ] Adding an actual compiler ( resource-heavy so well yeah it's expensive when run on the cloud ) 💸

- [ ] Better admin interface 🌟

- [X] ~~Rich text editing for coding problems to include pictures and more!✨~~ 

## Support this project 🤗 

Since I've already started to build this, I'm probably gonna learn to build a cloud based compiler as well and add it on this existing version of Online Judge/autograder to make it a full-fledged Online Judge to the likes of Sphere Online Judge. 

I intend to keep the source code absolutely open source forever for people to use and instead of paying services like Cloud9 IDE or Sphere Online Judge, this would allow users to implement this in the form a PyPi package ( will ship it soon ) and use it for their own applications and host it on AWS/GCP/Digital Ocean for slightly cheaper than you might with a pre built online judge to be embedded in your application.

This open source project is here to stay and be maintained so I would urge you to consider supporting this project by sponsoring it! Links included on the Github repo info panel.

Also checkout one of the other projects, [Geddit 🦄](https://github.com/arthtyagi/geddit) having base structural code for some of the features of DomeCode. 

## A word of thanks

I also want to thank the Django Developer Community all over the internet for being a good help when I got stuck.
