# ANALYSING TINDER DATA

## WHY? 

Ever wondered how good your tinder game really is? 
Here I am to show you the truth. I have created a script that analyses your tinder data, so you do not have to. 
You can either download the script and run it, or look at my code and make it yourself  ~~and maybe improve it~~. 

## HOW?
First you need to download your [tinder data.](https://account.gotinder.com/login?from=%2Fdata)

While waiting for that to show up in your email, get python ready. Maybe it is not important, but if you want to know
I used the IDE PyCharm to write my code. 

__Version: Python 3.7.3__

###### Libraries
To both run the script and write it on your own, you need a few libraries. 

- JSON
- Pandas
- Numpy 
- Matplotlib 

If you need help downloading the libraries. [This link](https://packaging.python.org/tutorials/installing-packages/) is helpful.

#### Running the script 
I will show how to do it via the terminal on Mac OS X, but if you have another OS [this link](https://www.cs.bu.edu/courses/cs108/guides/runpython.html) might be helpful! 

Open the terminal and write python + where you are storing the script. 
Looks something like this: 

```
python /Users/alinaeriksson/Desktop/tinder_script.py
```

The script will start and ask for where you are storing your data file. 
```
Enter filepath for tinder.json on your computer here:
```

And **of course** write back the file path. The file that you are interested in is the tinder.json. 

I would write something like this: 

```
/Users/alinaeriksson/Documents/Database/tinder.json
```

***Press enter and you got yourself some interesting numbers!*** 

If you have any questions, or just want to compare data, I can be reached at alina.eriksson@hyperisland.se
