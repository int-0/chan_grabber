chan_grabber
============

Uses API from popular chan board to grab all images.


This version is for test only!! Program API is quick & dirty!!


How it works
============

chan_grabber send request to chan API and retrieve all comments structure.
In this pass it makes a list of all images (including replies if you want).

After that, send HTTP request for each image, one by one.

Easy...
