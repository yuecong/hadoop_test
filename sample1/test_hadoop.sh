#!/bin/sh
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.3.0-cdh5.1.0.jar \
-file ./mapper.py -mapper ./mapper.py \
-file ./reducer.py -reducer ./reducer.py \
-input /user/hadoop/sample1/input/* \
-output /user/hadoop/sample1-output
